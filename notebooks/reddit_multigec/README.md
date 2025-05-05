### Reddit-MultiGEC

The multilingual GEC dataset is created in unsupervised fashion, using `GPT-4o-mini` and `o1-preview` for target generation.

Steps to reproduce:

1. Run `data_processing` part, refer to `notebooks/reddit_multigec/data_processing/README.md` for more details.
2. Run `synthetic_data_generation` part, refer to `notebooks/reddit_multigec/synthetic_data_generation/README.md` for more details.

Inputs, Configs, and Parameters:

- `datasets/reddit_multigec/reddit_multigec.csv` - Dataset from `data_processing` stage
- `parameters/reddit.batched.yaml` - Parameters for synthetic data generation
- `parameters/reddit.yml` - Parameters for data collection and moderation
- `datasets/reddit_multigec/pre_moderation_reddit_multigec.csv` - Output from `data_collection.ipynb` notebook, and input for `content_moderation.ipynb`
- `.env` - Env config with information like OpenAI API key

Temporary outputs:

- In `data_processing` part, after step 2 is run, we save results in `jsonb` format under `datasets/reddit_multigec/.nosync/*.jsonb`, the data will be used later in `reddit_batched_gec_aggregation.py`

Outputs:

- `datasets/reddit_multigec/pre_moderation_reddit_multigec.csv` - Unmoderated data after data collection
- `datasets/reddit_multigec/reddit_multigec.csv` - Moderated data after moderation