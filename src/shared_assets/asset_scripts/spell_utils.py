import re
import json
from lookups import icon_lookup, sound_lookup

# Load descriptions.json
with open('descriptions.json', 'r') as json_file:
    descriptions = json.load(json_file)

def generate_filename(caster_class, spell_id, spell_name):
    """
    Generates a filename based on the caster class, spell ID, and spell name.

    Parameters:
    - caster_class: The class of the caster (e.g., 'Sorcerer').
    - spell_id: The ID of the spell (e.g., '1101').
    - spell_name: The name of the spell (e.g., 'Discover Magic').

    Returns:
    A string representing the filename.
    """
    # Extract the first character of the caster class
    class_initial = caster_class[0].upper()
    # Extract the last three digits of the spell ID and format them as X-XX
    id_format = f"{spell_id[-3:-2]}-{spell_id[-2:]}"

    formatted_name = re.sub(r'[^a-zA-Z0-9 ]', '', spell_name)
    # Combine everything into the final filename

    filename = f"{class_initial}-{id_format}--{formatted_name}.gd"
    return filename


def get_icon_number(s):
    match = re.search(r'icon=(\d+)', s)
    if match:
        return int(match.group(1))
    else:
        return None

def get_proj_tex(s):
    icon_number = get_icon_number(s)
    icon = icon_lookup.get(icon_number)
    if icon_number != 0:
        return f"var proj_tex : String = '{icon}'"
    else:
        return ""

def get_proj_hit(s):
    icon_number = get_icon_number(s)
    icon = icon_lookup.get(icon_number)
    if icon_number != 0:
        return f"var proj_hit : String = '{icon}'"
    else:
        return ""
        

def get_sounds(cast_media, resolution_media):
    sounds = []
    cast_sound_match = re.search(r'sound=(\d+)', cast_media)
    if cast_sound_match:
        sounds.append(sound_lookup.get(int(cast_sound_match.group(1)), cast_sound_match.group(1)))
    resolution_sound_match = re.search(r'sound=(\d+)', resolution_media)
    if resolution_sound_match:
        sounds.append(sound_lookup.get(int(resolution_sound_match.group(1)), resolution_sound_match.group(1)))
    return sounds

def parse_damage(damage_field):
    """
    Parses the damage field to extract minimum and maximum damage values.

    Parameters:
    - damage_field: The damage field string from the CSV.

    Returns:
    A tuple containing (base_min, base_max, scaled_min, scaled_max).
    """
    # Regex to match the damage pattern
    damage_match = re.match(
        r'\[(\d+), (\d+)\] \+ \[(\d+), (\d+)\]/level', damage_field)
    if damage_match:
        base_min = int(damage_match.group(1))
        base_max = int(damage_match.group(2))
        scaled_min = int(damage_match.group(3))
        scaled_max = int(damage_match.group(4))
        return (base_min, base_max, scaled_min, scaled_max)
    else:
        # Return a default value if the pattern does not match
        return (0, 0, 0, 0)
    

def get_description(row):
  name = row['name']
  caste = row['caster_class']
  return descriptions[caste][name] if name in descriptions[caste] else name


def get_los(row):
    if (int(row['damage_type']) in [6, 1, 7, 8, 4] and
        int(row['target_type']) not in [10, 11] and
        int(row['effect']) in [0, 49] and
        int(row['size']) != 8 and
        not row['range'].startswith('-') and
        not row['resist_adjust'].startswith('-5%') and
        int(row['usable_in_camp']) != -1 and
        int(row['usable_in_combat']) == 1 and
        not int((row['damage_type']) == 4 and int(row['target_type']) == 4) and
        not int((row['damage_type']) == 7 and int(row['target_type']) == 4) and
        row['name'] != 'Acid Splash'):
        return 'true'
    return 'false'
  
def get_min_damage(damage):
    return f"{damage[0]} + ({damage[2]} * _power)"

def get_max_damage(damage):
     return f"{damage[1]} + ({damage[3]} * _power)"
 
def get_damage_roll(damage):
    return f"""var base_damage = 0
	var scaled_damage = 0

	var base_min = {damage[0]}
	var base_max = {damage[1]}

	base_damage = randi_range(base_min, base_max)
 
	var scaled_min = {damage[2]}
	var scaled_max = {damage[3]}
	for i in range(_power) :
		base_damage += randi_range(scaled_min, scaled_max)

	return scaled_damage + base_damage"""