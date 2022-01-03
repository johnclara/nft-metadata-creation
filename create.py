import pandas as pd
import json

csv_base_dir = "csvs"
csv_file_name = "Galactic Pixel Data - Galactic Warrior.csv"
input = pd.read_csv(f"{csv_base_dir}/{csv_file_name}")

def construct_galactic_warrior_metadata(row):
    return {
        "name": "TODO",
        "asset": row.at["File Name"],
        "properties": [
            {
                "prop_name": "Type",
                "prop_value": row.at["Type"]
            },
            {
                "prop_name": "Background",
                "prop_value": row.at["Background"]
            },
            {
                "prop_name": "Hands",
                "prop_value": row.at["Hands"]
            },
            {
                "prop_name": "Head",
                "prop_value": row.at["Head"]
            },
            {
                "prop_name": "Planet",
                "prop_value": row.at["Planet"]
            },
            {
                "prop_name": "Shield",
                "prop_value": row.at["Shield"]
            }
        ],
        "levels": [
            {
                "name": "Galactic Warrior Level",
                "value": row.at["Galactic Warrior Level"],
                "max_value": 10
            },
            {
                "name": "Galaxy Strike",
                "value": row.at["Galaxy Strike"],
                "max_value": 10
            },
            {
                "name": "Spell Power",
                "value": row.at["Spell Power"],
                "max_value": 10
            },
            {
                "name": "Spell Cast",
                "value": row.at["Spell Cast"],
                "max_value": 10
            }
        ],
        "stats": [
            {
                "name": "Battle Ready",
                "value": row.at["Battle Ready"],
                "max_value": 10,
            },
            {
                "name": "Power",
                "value": row.at["Power"],
                "max_value": 10,
            },
            {
                "name": "Speed",
                "value": row.at["Speed"],
                "max_value": 10,
            },
            {
                "name": "Spell Capability",
                "value": row.at["Spell Capability"],
                "max_value": 10,
            },
            {
                "name": "Spell Power",
                "value": row.at["Spell Power"],
                "max_value": 10,
            }
        ]
    }

def keep(file_name):
    return file_name.startswith("2C2A6A84") or file_name.startswith("4167B2C0")

data = [construct_galactic_warrior_metadata(row) for i, row in input.iterrows()]
data = [row for row in data if keep(str(row["asset"]))]

text_file = open("results/metadata.json", "w")
n = text_file.write(json.dumps(data, indent=4, sort_keys=True))
text_file.close()
