# Extractron

Extractron is a Python script that performs Entity Extraction using the spaCy Natural Language Processing model(s).\
This has purely been created for CTF's.



## Setup

#### Clone the repository
```shell
git clone https://github.com/B0neShad0w/Extractron
cd Extractron
```

#### Install requirements
```shell
pip3 install -r requirements.txt
```

#### Install the spaCy model(s)
```bash
python3 -m spacy download en_core_web_sm
python3 -m spacy download en_core_web_md
python3 -m spacy download en_core_web_lg
python3 -m spacy download en_core_web_trf
```

## Usage

#### Load a dataset and perform an Entity Extraction
```python
# This will outfile a file using the name as the input file (auto appended with .kml)
python3 Extractron.py --input test_dataset.txt
```
#### Load the outputted KML file into Google Earth Pro/Google Maps etc.


## Planned features

- [X] None currently

## Contact
Feel free to contact me on <a href="https://twitter.com/B0neShad0w">Twitter</a>
