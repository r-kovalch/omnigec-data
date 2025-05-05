import os
import json

import pandas as pd
from dotenv import load_dotenv
from omegaconf import OmegaConf
from openai import OpenAI

from src.prompts.reddit import (
    multi_gec_prompt_per_language
)
from src.utils.openai_batch_utils import retrieve_openai_batch
from src.utils.openai_batch_utils import submit_openai_batch

root_directory_folder = "./"

load_dotenv(f"{root_directory_folder}.env")

parameters = OmegaConf.load(f"{root_directory_folder}/parameters/reddit.batched.yaml")
# Define parameters
output_dir = f"{root_directory_folder}/datasets/reddit/batched.nosync"  # Directory to save JSONL files
client = OpenAI(api_key=os.environ.get("OPEN_AI_API_KEY"))

reddit_df = pd.read_csv(f"{root_directory_folder}/datasets/reddit_multigec/reddit_multigec.csv", index_col=0)
reddit_df.index = reddit_df.index.astype(int)

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
    filename = f"{output_dir}/reddit_batched_multi_gec_input_{start_at}:{end_at}.jsonl"

    if os.path.exists(filename):
        os.remove(filename)

    for i in range(start_at, end_at + 1):
        row = df.loc[i]
        prompt_template = multi_gec_prompt_per_language[row["language"]].template
        sample_id: int = str(i)
        sample_input_text: str = row[text_column]
        sample_request = {
            "custom_id": sample_id,
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": parameters.multi_gec.model_name,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt_template.format(
                            text=sample_input_text,
                            num_corrections=parameters.multi_gec.num_corrections
                        ),
                    }
                ],
                "temperature": parameters.multi_gec.temperature,
                "top_p": parameters.multi_gec.top_p,
            }
        }

        # Save the batch to a JSONL file
        with open(filename, "a") as f:
            f.write(json.dumps(sample_request) + "\n")

    print(f"Input request saved to: {filename}")

    return filename

for batch_id, (s_at, e_at) in parameters.processing.batches.multi_gec.items():
    # Prepare batches
    reddit_df_subset = reddit_df.loc[s_at:e_at]
    batch_filename = prepare_jsonl_batches(
        df=reddit_df,
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
        description_prefix="reddit-batched-multigec"
    )
    print(f"{batch_metadata.id}: [{s_at, e_at}]")

#%%

multi_gec_batches: str = "multi_gec:\n"
for batch_id, (s_at, e_at) in parameters.processing.batches.multi_gec.items():
    output_file = retrieve_openai_batch(
        client=client,
        batch_id=batch_id,
        output_dir=output_dir,
        start_at=s_at,
        end_at=e_at,
        description_prefix="reddit_batched_multi_gec",
    )
    multi_gec_batches += f"\t{batch_id}: [{s_at}, {e_at}]\n"

    print(f"Batch {batch_id}: {s_at, e_at} processing output saved to: {output_file}")

print()
print(multi_gec_batches)
