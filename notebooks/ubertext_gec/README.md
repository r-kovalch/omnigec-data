### UberText-GEC

The GEC dataset is created in unsupervised fascion, from UberText 2.0 Social Media Corpora.

Steps to reproduce:

1. Download original dataset "UberText 2.0 Social Media Corpora" from [lang.org.ua](https://lang.org.ua/en/ubertext/) and save it under `datasets/ubertext_gec/ubertext.social.filter_rus_gcld+short.text_only.txt`
2. Run `preprocessing` by executing `preprocessing/format_ubertext_txt_to_csv.py`, which would yield csv output file under `datasets/ubertext_gec/raw_ubertext_gec.csv`
3. Run `synthetic_data_generation` to generate target by executing:

    a. `ubertext_batched_multi_gec.ipynb`, which would use `datasets/ubertext_gec/raw_ubertext_gec.csv` as input to generate multiple possible corrections, and save the output to `datasets/ubertext_gec/batched.nosync/*.jsonb` files.
    
    b. `ubertext_batched_gec_aggregation.ipynb`, which would use the `jsonb` files from previous step to aggregate multiple possible corrections into one, and save it under `datasets/ubertext_gec/pre_post_processing_ubertext_gec_slim.csv`
4. Run `postprocessing` by executing `postprocessing/remove_footers.csv`, which removes unnecessary footers promoting subscription to the social media channels. In its turn this step would yield `datasets/ubertext_gec/ubertext_gec.csv` which is final dataset for UberText-GEC we use in HuggingFace

### Inputs and Configs:

- `datasets/ubertext_gec/ubertext.social.filter_rus_gcld+short.text_only.txt` - "UberText 2.0 Social Media Corpora" from [lang.org.ua](https://lang.org.ua/en/ubertext/)
- `datasets/ubertext_gec/raw_ubertext_gec.csv` - CSV variant with token statistics of above
- `datasets/ubertext_gec/pre_post_processing_ubertext_gec_slim.csv` - UberText 2.0 Social Media dataset with generated GEC targets, without removing footers. (before post-processing) saved in parallel fashion to save space (only feature-target).

### Temporary Outputs:

- After step 3.a is run, we save results in `jsonb` format under `datasets/ubertext_gec/.nosync/*.jsonb`, the data will be used later in `ubertext_batched_gec_aggregation.ipynb`


### Outputs

- `datasets/ubertext_gec/ubertext_gec.csv` - UberText-GEC dataset we published in HuggingFace [lang-uk/UberText-GEC](https://huggingface.co/datasets/lang-uk/UberText-GEC), with footers removed, i.e. after post-processing.

### Postprocessing Notes

We remove unwanted footers like:

```text
Апостроф  |Підписатися
* Підписатися на Укрінформ
@babel
👉Підписатися на ZN.
Підписатися | Сайт | FB | YouTube | Підтримати нас.
Підписатися на Укрінформ
Підписуйтеся на Укрінформ.
👉  Підписатися на ZN.
UA
Підписатися на Укрінформ
Підписатися на Укрінформ.
Підпишіться на НВ
Підпишіться на НВ.
ідписатися на ZN.
UA
Апостроф  |Підписатися
Новостьна русском.
👉  Підписатися на ZN.
Новина російською. 👉 Підписатися на ZN.UA.
Підписатися на ZN. UA
Підписатися на ZN.
 Підписуйтеся на ZN.UA.
Підписатися на ZN.
Підписатися на Укрінформ
👉 Підписатися на ZN.
UA
Підписатися на ZN.
UA
```

using regex pattern matching.

#### Limitations

Some footers might be left unremoved in either feature or target data, as this step was done in post-processing mode, when it should have been removed before synthetic data generation. As the latter rephrases this unwanted data in hardly predictable way, making it even harder to remove this unwanted data.
