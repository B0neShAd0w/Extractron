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

#### Import NMEA data from file and export to an KML file.
> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/B0neShAd0w/Markdown/main/Blockquotes/Light-Theme/note.svg">
>   <img alt="Info" src="https://raw.githubusercontent.com/B0neShAd0w/Markdown/main/Blockquotes/Dark-Theme/note.svg">
> </picture><br>
>
> The Output file will be saved to the same directory where Input file resides.
```python
# This will outfile a file using the name as the input file (auto appended with .kml)
python3 Extractron.py --input input_test_data.nmea
```
#### Load the outputted KML file into Google Earth Pro/Google Maps etc.


## Planned features

- [X] None currently

## Contact
Feel free to contact me on <a href="https://twitter.com/B0neShad0w">Twitter</a>
