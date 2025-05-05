### Data Processing

Steps to reproduce: 

1. `data_collection.ipynb` - Run to start sampling from reddit, the subreddits and other parameters are defined in `parameters/reddit.yaml`. To change number of threads collected edit the notebook before execution.
2. `content_moderation.ipynb` - Run content moderation with `omni-moderation-latest` model on the collected data from reddit, to exclude sensitive samples.

Inputs and parameters:

- `parameters/reddit.yml` - Parameters for data collection and moderation
- `datasets/reddit_multigec/pre_moderation_reddit_multigec.csv` - Output from `data_collection.ipynb` notebook, and input for `content_moderation.ipynb` 

Outputs: 

- `datasets/reddit_multigec/pre_moderation_reddit_multigec.csv` - Unmoderated data after data collection
- `datasets/reddit_multigec/reddit_multigec.csv` - Moderated data after moderation