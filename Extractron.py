import spacy
import argparse
import os
import sys

from colorama import Fore

def check_spacy_model(model):
    try:
        spacy.load(model)
        return True
    except OSError:
        return False

def extract_entities(input_data, input_type, entity_types, model):
    nlp = spacy.load(model)
    if input_type == "file":
        with open(input_data, "r") as file:
            text = file.read()
            doc = nlp(text)
            entities = set(ent.text for ent in doc.ents if ent.label_ in entity_types)
            return entities
    else:
        raise ValueError("Invalid input type. Must be 'file'.")

if __name__ == "__main__":

    print(Fore.WHITE + """
    
    ███████╗██╗  ██╗████████╗██████╗  █████╗  ██████╗████████╗██████╗  ██████╗ ███╗   ██╗
    ██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║
    █████╗   ╚███╔╝    ██║   ██████╔╝███████║██║        ██║   ██████╔╝██║   ██║██╔██╗ ██║
    ██╔══╝   ██╔██╗    ██║   ██╔══██╗██╔══██║██║        ██║   ██╔══██╗██║   ██║██║╚██╗██║
    ███████╗██╔╝ ██╗   ██║   ██║  ██║██║  ██║╚██████╗   ██║   ██║  ██║╚██████╔╝██║ ╚████║
    ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                     
             Created by """ + Fore.WHITE + "BoΠeShΔdϴw³ | https://github.com/B0neShAd0w/Extractron\n")

    parser = argparse.ArgumentParser(description="Entity Extraction")
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--person", action="store_true", help="Extract PERSON entities, including fictional characters and groups of people.")
    parser.add_argument("--gpe", action="store_true", help="Extract GEOPOLITICAL entities, such as countries, cities, and states.")
    parser.add_argument("--loc", action="store_true", help="Extract NON-GPE locations, such as mountains, bodies of water, and parks.")
    parser.add_argument("--org", action="store_true", help="Extract ORGANIZATIONS entities, such as companies, institutions, and agencies.")
    parser.add_argument("--date", action="store_true", help="Extract DATE entities, absolute or relative dates or periods.")
    parser.add_argument("--time", action="store_true", help="Extract TIME entities, including specific times of day or durations.")
    parser.add_argument("--money", action="store_true", help="Extract MONEY entities, monetary values, including currency symbols.")
    parser.add_argument("--percent", action="store_true", help="Extract PERCENT entities, including percentage symbol.")
    parser.add_argument("--cardinal", action="store_true", help="Extract CARDINAL entities, such as numerals that do not fall under another type.")
    parser.add_argument("--ordinal", action="store_true", help="Extract ORDINAL entities, such as 'first', 'second', etc.")
    parser.add_argument("--quantity", action="store_true", help="Extract QUANTITY entities, such as measurements, as of weight or distance.")
    parser.add_argument("--product", action="store_true", help="Extract PRODUCT entities, such as objects, vehicles, foods, etc. (Not included in all models)")
    parser.add_argument("--event", action="store_true", help="Extract EVENT entities, such as Named hurricanes, battles, wars, sports events, etc. (Not included in all models)")
    parser.add_argument("--model", required=True, help="Spacy model to use")
    parser.add_argument("--output", help="Output file path")
    args = parser.parse_args()

    input_data = args.input
    input_type = "file"
    entity_types = []

    if args.person:
        entity_types.append("PERSON")
    if args.gpe:
        entity_types.append("GPE")
    if args.loc:
        entity_types.append("LOC")
    if args.org:
        entity_types.append("ORG")
    if args.date:
        entity_types.append("DATE")
    if args.time:
        entity_types.append("TIME")
    if args.money:
        entity_types.append("MONEY")
    if args.percent:
        entity_types.append("PERCENT")
    if args.cardinal:
        entity_types.append("CARDINAL")
    if args.ordinal:
        entity_types.append("ORDINAL")
    if args.quantity:
        entity_types.append("QUANTITY")
    if args.product:
        entity_types.append("PRODUCT")
    if args.event:
        entity_types.append("EVENT")

    model = args.model

    if not check_spacy_model(model):
        print(f"{Fore.RED}[-] Spacy model '{model}' is not installed. Please install it by running: python -m spacy download {model}\n")
        sys.exit(1)

    if not entity_types:
        print(f"{Fore.YELLOW}[-] At least one entity type must be specified.\n")
        sys.exit(1)

    print(f'Please be patient while entities are extracted...\n')

    entities = set()
    for entity_type in entity_types:
        entities.update(extract_entities(input_data, input_type, [entity_type], model))

    output_file = args.output if args.output else f"{entity_types[0].lower()}_{args.model.lower()}.txt"

    with open(output_file, "w") as file:
        for entity in entities:
            file.write(f"{entity}\n")

    num_entities = len(entities)
    print(f"{num_entities} unique entities extracted.")
    print(f"All entities saved to: {output_file}\n")
