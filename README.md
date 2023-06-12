# Extractron

Extractron is a Python script that performs Entity Extraction using the spaCy Natural Language Processing model(s).\
This has purely been created for CTF's.

![Screenshot 2023-06-12 160003](https://github.com/B0neShAd0w/Extractron/assets/117080369/88d4ee9b-7dde-4c64-8f58-189f33062725)

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

#### Load the test_dataset and perform an Entity Extraction using the 'small' spaCy model, against the 'PERSON' entity
```python
python3 Extractron.py --input test_dataset.txt --model small --person
```

#### Load the test_dataset and perform an Entity Extraction using the 'transformer' spaCy model, against the 'GEOPOLITICAL' entity
```python
python3 Extractron.py --input test_dataset.txt --model small --gpe
```

#### Load the test_dataset and perform an Entity Extraction using the 'medium' spaCy model, against the 'EVENT' entity, and output to 'results.txt'
```python
python3 Extractron.py --input test_dataset.txt --model medium --event --output results.txt
```

#### Available entities
| Parameter | Description |
|---------|-----------|
| --person | Extract PERSON entities, including fictional characters and groups of people. |
| --gpe | Extract GEOPOLITICAL entities, such as countries, cities, and states. |
| --loc | Extract NON-GPE locations, such as mountains, bodies of water, and parks. |
| --org | Extract ORGANIZATIONS entities, such as companies, institutions, and agencies. |
| --date | Extract DATE entities, absolute or relative dates or periods. |
| --time | Extract TIME entities, including specific times of day or durations. |
| --money | Extract MONEY entities, monetary values, including currency symbols. |
| --percent | Extract PERCENT entities, including percentage symbol. |
| --cardinal | Extract CARDINAL entities, such as numerals that do not fall under another type. |
| --ordinal | Extract ORDINAL entities, such as 'first', 'second', etc. |
| --quantity | Extract QUANTITY entities, such as measurements, as of weight or distance. |
| --product | Extract PRODUCT entities, such as objects, vehicles, foods, etc. (Not included in all models |
| --event | Extract EVENT entities, such as Named hurricanes, battles, wars, sports events, etc. (Not included in all models |

#### Available spaCy models
| Parameter | Value | spaCy Model name |
|---------|-----|----------------|
| --model | small | en_core_web_sm |
| --model | medium | en_core_web_md |
| --model | large | en_core_web_lg |
| --model | transformer | en_core_web_transformer |

## Planned features

- [X] None currently

## Contact
Feel free to contact me on <a href="https://twitter.com/B0neShad0w">Twitter</a>
