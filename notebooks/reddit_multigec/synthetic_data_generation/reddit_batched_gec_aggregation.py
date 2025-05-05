import os
import json
from typing import Union

import pandas as pd
from IPython.core.display_functions import display
from dotenv import load_dotenv
from omegaconf import OmegaConf
from openai import OpenAI

from src.prompts.reddit_multigec import (
    gec_aggregation_prompt_per_language
)
from src.utils.openai_batch_utils import retrieve_openai_batch
from src.utils.openai_batch_utils import submit_openai_batch
from src.utils.output_formatters import try_to_extract_dict_from_json_openai

root_directory_folder = "./"

load_dotenv(f"{root_directory_folder}.env")

parameters = OmegaConf.load(f"{root_directory_folder}/parameters/reddit.batched.yaml")
# Define parameters
output_dir = f"{root_directory_folder}/datasets/reddit/batched.nosync"  # Directory to save JSONL files
client = OpenAI(api_key=os.environ.get("OPEN_AI_API_KEY"))

reddit_df = pd.read_csv(f"{root_directory_folder}/datasets/reddit_multigec/reddit_multigec_aggregated_corrections.csv")

#%%

def prepare_jsonl_batches(
    df: pd.DataFrame,
    text_column: str,
    start_at: int,
    end_at: int,
    output_dir: str
):
    """
    Split the dataset into batches and save as JSONL files for batch processing.
    """
    filename = f"{output_dir}/reddit_batched_gec_aggregation_input_{start_at}:{end_at}.jsonl"
    multigec_output_file = f"{output_dir}/reddit_batched_multi_gec_output_{start_at}:{end_at}.jsonl"

    if os.path.exists(filename):
        os.remove(filename)

    multigec_outputs: list[str] = open(multigec_output_file, "r").read().split("\n")

    for i, multigec_output in zip(
        range(start_at, end_at + 1),
        multigec_outputs
    ):
        multigec_output = json.loads(multigec_output)["response"]["body"]["choices"][0]["message"]["content"]
        corrections: Union[dict, str] = try_to_extract_dict_from_json_openai(multigec_output)

        row = df.loc[i]
        prompt_template = gec_aggregation_prompt_per_language[row["language"]].template
        sample_id: int = str(i)
        sample_input_text: str = row[text_column]
        sample_request = {
            "custom_id": sample_id,
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": parameters.gec_aggregation.model_name,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt_template.format(
                            text=sample_input_text,
                            possible_corrections=corrections,
                            num_corrections=parameters.multi_gec.num_corrections
                        ),
                    }
                ],
                "temperature": parameters.gec_aggregation.temperature,
                "top_p": parameters.gec_aggregation.top_p,
            }
        }

        # Save the batch to a JSONL file
        with open(filename, "a") as f:
            f.write(json.dumps(sample_request) + "\n")

    print(f"Input request saved to: {filename}")

    return filename

gec_aggregation_batches: str = "gec_aggregation:\n"
for _, (s_at, e_at) in parameters.processing.batches.multi_gec.items():
    # Prepare batches
    reddit_df_subset = reddit_df.loc[s_at:e_at]
    batch_filename = prepare_jsonl_batches(
        df=reddit_df_subset,
        text_column="text",
        start_at=s_at,
        end_at=e_at,
        output_dir=output_dir
    )

    batch_metadata = submit_openai_batch(
        client=client,
        batch_filename=batch_filename,
        start_at=s_at,
        end_at=e_at,
        description_prefix="reddit-batched-gecaggregation"
    )
    gec_aggregation_batches += f"\t{batch_metadata.id}: [{s_at}, {e_at}]\n"

    print(f"Batch submitted for processing: {batch_metadata.id}")

print("")
print(gec_aggregation_batches)

#%%
from src.utils.openai_batch_utils import retrieve_openai_batch
for batch_id, (s_at, e_at) in parameters.processing.batches.gec_aggregation.items():
    output_file = retrieve_openai_batch(
        client=client,
        batch_id=batch_id,
        output_dir=output_dir,
        start_at=s_at,
        end_at=e_at,
        description_prefix="reddit_batched_gec_aggregation",
    )

#%%

import logging
from json import JSONDecodeError
from tqdm import tqdm
silver_file: str = f"{output_dir}/../reddit_silver_sample.csv"

logging.basicConfig(level = logging.INFO,format = '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s')

if not os.path.exists(silver_file):
    silver_df: pd.DataFrame = reddit_df
    silver_df.to_csv(silver_file, index=False)
else:
    silver_df = pd.read_csv(silver_file)

for _, (s_at, e_at) in tqdm(parameters.processing.batches.gec_aggregation.items(), desc="Batches progress"):
    multigec_output_file = f"{output_dir}/reddit_batched_multi_gec_output_{s_at}:{e_at}.jsonl"
    gecaggregation_output_file = f"{output_dir}/reddit_batched_gec_aggregation_output_{s_at}:{e_at}.jsonl"
    multigec_outputs: list[str] = open(multigec_output_file, "r").read().split("\n")
    gecaggregation_outputs: list[str] = open(gecaggregation_output_file, "r").read().split("\n")

    for gec_aggregation_output in gecaggregation_outputs:
        try:
            id = int(json.loads(gec_aggregation_output)["custom_id"])
            relative_element = id - s_at
            multi_gec_output = multigec_outputs[relative_element]

            multi_gec_output: dict[str] = json.loads(multi_gec_output)["response"]["body"]["choices"][0]["message"]["content"]
            multi_gec_output: Union[list[dict[str]], str] = try_to_extract_dict_from_json_openai(multi_gec_output)

            if isinstance(multi_gec_output, list):
                multi_gec_corrections: list[str] = [gec_output["correction"] for gec_output in multi_gec_output]

                silver_df.loc[id, "multi_gec_corrections"] = str(multi_gec_corrections)
            else:
                silver_df.loc[id, "multi_gec_corrections"] = None
                # silver_df.loc[id, "multi_gec_raw"] = multi_gec_output

            gec_aggregation_output: dict[str] = json.loads(gec_aggregation_output)["response"]["body"]["choices"][0]["message"]["content"]
            gec_aggregation_output: Union[dict[str], str] = try_to_extract_dict_from_json_openai(gec_aggregation_output)

            if isinstance(gec_aggregation_output, dict):
                gec_aggregation_correction: str = gec_aggregation_output["correction"]

                silver_df.loc[id, "gec_aggregation_correction"] = gec_aggregation_correction
            else:
                silver_df.loc[id, "gec_aggregation_correction"] = None
                # silver_df.loc[id, "gec_aggregation_raw"] = gec_aggregation_output
        except TypeError as e:
            logging.error(f"Got exception: {e} {type(e)}; Skipping: {id} {silver_df.loc[id, 'text']}")
        except JSONDecodeError as e:
            logging.error(e)

silver_df.index.name = "index"
silver_df.to_csv(silver_file, index=False)

silver_df = pd.read_csv(silver_file)
display(silver_df)
