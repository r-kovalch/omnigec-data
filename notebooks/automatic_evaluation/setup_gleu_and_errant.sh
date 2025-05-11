git clone https://github.com/shotakoyama/gleu.git && \
cd gleu

pip install regex pandas syntok

git clone https://github.com/cainesap/errant
cd errant
pip install -e .
cd ../

git clone https://github.com/cainesap/spacy_conll
cd spacy_conll
pip install -e .
cd ../

pip install spacy-udpipe
mkdir spacy_udpipe_models
