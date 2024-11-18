import csv
import os
import re

from spell_template import gdscript_template
from spell_utils import generate_filename
from build_data import build_data

# Define the path to your CSV file
csv_file_path = 'spells.csv'
# Define the directory where the GDScript files will be saved
output_dir = 'gd_scripts'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Note: You'll need to adjust the code that fills in the template to include the new fields and logic.
# For example, `sp_cost_formula` should be set to `_power*2` for spells like "Enchanted Blade",
# and `special_effect_function` should include the logic for `add_traits_to_target` when applicable.

# Open the CSV file and read data
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:

        data = build_data(row)
        
        gdscript_content = gdscript_template.format(**data)

        # Define the file name for the GDScript file
        filename = generate_filename(
            row['caster_class'], row['code'], row['name'])
        # Save the GDScript file
        with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as gdscript_file:
            gdscript_file.write(gdscript_content)

        print(f"Generated GDScript file for spell: {row['name']}")
