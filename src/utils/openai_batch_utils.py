import time
import os
from datetime import datetime

def submit_openai_batch(
    client,
    batch_filename,
    start_at,
    end_at,
    description_prefix:str,
    completion_window="24h",
):
    description=f"{description_prefix}-{start_at}:{end_at}"
    # Create input file for batch processing
    batch_input_file = client.files.create(
        file=open(batch_filename, "rb"),
        purpose="batch"
    )

    # Create the batch
    batch_metadata = client.batches.create(
        input_file_id=batch_input_file.id,
        endpoint="/v1/chat/completions",
        completion_window=completion_window,
        metadata={"description": description}
    )
    print(f"Batch submitted for processing: {batch_metadata.id}")

    return batch_metadata

def retrieve_openai_batch(
    client,
    batch_id: str,
    output_dir,
    start_at,
    end_at,
    description_prefix: str,
    retry_delay=1 * 60  # 15 minutes in seconds
):
    # Wait for processing to complete
    while True:
        retrieve_metadata = client.batches.retrieve(batch_id)
        if retrieve_metadata.status == "completed":
            break
        elif retrieve_metadata.status == "failed":
            raise RuntimeError("Batch processing failed")
        else:
            print(f"{datetime.now()}: waiting... {retry_delay / 60} more mins for batch {batch_id} to complete")
            time.sleep(retry_delay)

    # Retrieve output file content
    file_response = client.files.content(retrieve_metadata.output_file_id)

    # Write output to file
    output_filename = f"{output_dir}/{description_prefix}_output_{start_at}:{end_at}.jsonl"

    if os.path.exists(output_filename):
        os.remove(output_filename)

    for response in file_response.text.split("\n"):
        with open(output_filename, "a") as f:
            f.write(response + "\n")

    print(f"Batch processing output saved to: {output_filename}")

    return output_filename


