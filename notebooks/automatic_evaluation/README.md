### Automatic Evaluation

Steps to reproduce:
0. Run `setup_gleu_and_errant.sh` in this folder.
1. Download annotation dataset from [Huggingface](https://huggingface.co/datasets/peterua/OmniGEC-ModelTraining/tree/main) and save under `datasets/annotations/anot_1500.csv`
2. Run `create_multiref_corrections.ipynb` notebook, to create three possible corrections from: LanguageTool, Spivavtor, and Pravopysnyk, which saves the results to `datasets/automatic_evaluation/multiref.csv`
3. Run `gleu_and_errant.ipynb` to compute multiref GLEU and ERRANT scores for annotation dataset, which is in Ukrainian, and saves the results per corpora (need to change the variable for wanted one) to `datasets/automatic_evaluation/{corpora}_errant_multi_ref.csv` where `corpora` could be: `uber`, `reddit`, and `wikiedits`. GLEU is saved to `datasets/automatic_evaluation/{corpora}_gleu_multi_ref.csv`
4. Run `edit_distance.ipynb` with target `corpora` set as in step 3, outputs are outputted to `datasets/automatic_evaluation/{corpora}_edit_distance.csv`

Inputs:

- `datasets/annotations/anot_1500.csv` - annotation dataset for Ukrainian, downloaded from [Huggingface](https://huggingface.co/datasets/peterua/OmniGEC-ModelTraining/tree/main)

Outputs:

- `datasets/automatic_evaluation/multiref.csv` - for each 1500 samples in `annot_1500` dataset we create three possible corrections from other relevant GEC tools for Ukrainian
- `datasets/automatic_evaluation/{corpora}_errant_multi_ref.csv` - ERRANT scores per corpora in multi-ref comparison
- `datasets/automatic_evaluation/{corpora}_gleu_multi_ref.csv` - GLEU scores per corpora in multi-ref comparison
- `datasets/automatic_evaluation/{corpora}_edit_distance.csv` - edit-distance, CER scores

For details in theoretical part and evaluation results, refer to the source Paper.
