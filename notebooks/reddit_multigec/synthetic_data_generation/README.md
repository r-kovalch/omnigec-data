### Synthetic Data Generation

Steps to reproduce:
1. Make sure you defined variables in `.env` from `samples.env`
2. Run `reddit_batched_multi_gec.py` which would create three possible corrections, and save it under `datasets/reddit_multigec/.nosync/*.jsonb` files.
3. Run `reddit_batched_gec_aggregation.py` those jsonb chunks will be used here to aggregate multiple possible corrections into one, with outputting `datasets/reddit_multigec/reddit_multigec_aggregated_corrections.csv` file at the end.

Inputs, Configs, and Parameters:

- `datasets/reddit_multigec/reddit_multigec.csv` - Dataset from `data_processing` stage
- `parameters/reddit.batched.yaml` - Parameters for synthetic data generation
- `.env` - Env config with information like OpenAI API key

Temporary outputs:

- After step 2 is run, we save results in `jsonb` format under `datasets/reddit_multigec/.nosync/*.jsonb`, the data will be used later in `reddit_batched_gec_aggregation.py`

Outputs:

- `datasets/reddit_multigec/reddit_multigec_aggregated_corrections.csv` - Final dataset in feature-target format.
