# OmniGEC‑Data

Light‑weight, **reproducible** pipelines and prompt libraries that back the [Introducing OmniGEC: A Silver Multilingual Dataset for Grammatical Error Correction](https://huggingface.co/collections/lang-uk/omnigec-68095391ebef195ed6c0a5f3).
All heavy data live on the HuggingFace Hub; this repo keeps only:

* parameter files (`/parameters`)
* runnable notebooks (`/notebooks`)
* prompt + utility source code (`/src`)
* empty folder stubs that mirror public dataset structure (`/datasets`).

For the full methodology and experimental results see our ACL 2025 paper
“**Introducing OmniGEC: A Silver Multilingual Dataset for Grammatical Error Correction**” – [PDF](TBD).



---

## Installation

```bash
git clone https://github.com/r‑kovalch/omnigec-data.git
cd omnigec-data
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

You will need an `OPENAI_API_KEY` in `.env` for synthetic‑data scripts.

---

## Repository layout

```text
omnigec-data/
├── datasets/                    # Empty placeholders that mirror public HF datasets
│   ├── automatic_evaluation/
│   ├── multigec/
│   ├── omnigec_model_training/
│   ├── reddit_multigec/
│   ├── ubertext_gec/
│   └── wikiedits_multigec/
├── notebooks/                   # Reproducible research notebooks
│   ├── omnigec/                 # OmniGEC aggregation / visualisations
│   ├── reddit_multigec/         # Reddit‑MultiGEC crawl & synthetic data
│   └── ubertext_gec/            # UberText‑GEC pipeline
├── parameters/                  # YAML configs for data collection/batching
├── src/
│   ├── prompts/                 # Prompt templates per corpus & language
│   └── utils/                   # Helper utilities (metrics, HTML diff, OpenAI batching)
└── README.md                    # ← you are here
```

### Selected notebooks & scripts

| Path                                 | Purpose                                                          |
| ------------------------------------ | ---------------------------------------------------------------- |
| `notebooks/omnigec/concat/*`         | Merge sub‑corpora into the **OmniGEC** super‑set                 |
| `notebooks/omnigec/visualizations/*` | Reproduce figures from the paper (token KDEs, Face‑2‑Face, etc.) |
| `notebooks/reddit_multigec/*`        | End‑to‑end Reddit crawler → content moderation → GEC synthesis   |
| `notebooks/ubertext_gec/*`           | UberText preprocessing and prompt‑based correction               |
| `src/prompts/*`                      | Typed prompt templates (Pydantic) per corpus / language          |
| `src/utils/openai_batch_utils.py`    | Helpers for OpenAI batch & file management                       |
| `src/utils/metrics.py`               | Plain‑Python edit‑distance & CER utilities                       |
| `parameters/*.yaml`                  | Ω‑Conf configs that parameterise batch generation                |

---

## Reddit → Reddit‑MultiGEC

To run, review `notebooks/reddit_multigec/README.md`

The module:

1. downloads fresh Reddit posts,
2. chunks them into JSONL micro‑batches,
3. submits them for correction with the **OpenAI Batch API**,
4. retrieves & collates the corrected texts.

## UberText 2.0 Social Media Corpora → Ubertext‑GEC

To run, review `notebooks/ubertext_gec/README.md`

The module:

1. preprocesses the "UberText 2.0 Social Media Corpora" dataset,
2. chunks them into JSONL micro-batches,
3. submits them for correction with the **OpenAI BatchAPI**,
4. retrieves & collates the corrected texts,
5. postprocesses the parallel dataset, by removing unwanted promotional footers present in original data.

## WikiEdits → WikiEdits‑MultiGEC

The code for WikiEdits-MultiGEC is maintained in another GitHub Repo – [WikiEdits-MultiGEC](https://github.com/PetroIvaniuk/wikiedits-multigec.git).\
However, it's linked to the OmniGEC-Data, as a submodule within `notebooks/wikiedits-multigec`

---

## Data Visualizations

![corpus_data.png](pictures%2Fcorpus_data.png)
![box_per_language_and_corpora.png](pictures%2Fbox_per_language_and_corpora.png)

---

## Citing
TBD
```bibtex
@inproceedings{omnigec2025,
  author    = {Roman Kovalchuk, Petro Ivaniuk, Mariana Romanyshyn},
  title     = {Introducing OmniGEC: A Silver Multilingual Dataset for Grammatical Error Correction},
  booktitle = {Proceedings of ACL 2025},
  year      = {2025}
}
```

---

© 2025 [Roman Kovalchuk](https://github.com/r-kovalch), [Petro Ivaniuk](https://github.com/PetroIvaniuk), [Mariana Romanyshyn](https://github.com/mariana-scorp). Licensed under the MIT License.

## Notes

- For details on trained models on this data, refer to the omnigec-models repository: https://github.com/r-kovalch/omnigec-models

