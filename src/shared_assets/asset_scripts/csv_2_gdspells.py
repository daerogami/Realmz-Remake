import csv
import os

from spell_template import gdscript_template
from spell_utils import generate_filename
from build_data import build_data

# Define the path to your CSV file
csv_file_path = 'spells.csv'
# Define the directory where the GDScript files will be saved
output_dir = 'gd_scripts'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Dictionary to hold rows by caster class
caster_class_rows = {}

# Open the CSV file and read data
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        caster_class = row['caster_class']
        if caster_class not in caster_class_rows:
            caster_class_rows[caster_class] = []
        caster_class_rows[caster_class].append(row)

# List to hold the merged rows
csv_rows = []

# Merge the rows by taking one spell from each caster class each cycle
while any(caster_class_rows.values()):
    for caster_class in list(caster_class_rows.keys()):
        if caster_class_rows[caster_class]:
            csv_rows.append(caster_class_rows[caster_class].pop(0))

# Dictionary to hold all the data by spell name
all_spells = {}

# Process the rows to build the data
for row in csv_rows:
    spell_name = row['name']
    if spell_name in all_spells:
        # Add the caster_class to the school array if the spell already exists
        print(
            f"Spell {spell_name} already exists. Adding {row['caster_class']} to schools array."
        )
        all_spells[spell_name][1]['schools'].append(row['caster_class'])
    else:
        data = build_data(row)
        all_spells[spell_name] = (row, data)

# Write the GDScript files
for spell_name, (row, data) in all_spells.items():
    gdscript_content = gdscript_template.format(**data)
    filename = generate_filename(row['caster_class'], row['code'], spell_name)
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as gdscript_file:
        gdscript_file.write(gdscript_content)
    print(f"Generated GDScript file for spell: {spell_name}")
