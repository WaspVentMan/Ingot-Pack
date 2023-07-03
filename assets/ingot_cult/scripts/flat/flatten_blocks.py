# Generates item models and placeholder textures for blocks that have not been done yet.

import os
from shutil import copyfile

placeholder_item_texture = "/home/brine/projects/ingot-pack/assets/minecraft/textures/item/missing_texture.png"
item_models_directory = "/home/brine/projects/ingot-pack/assets/minecraft/models/item"
textures_directory = "/home/brine/projects/ingot-pack/assets/minecraft/textures/item"
vanilla_block_models_directory = "/home/brine/.mc/versions/1.20something/assets/minecraft/models/block"

template_item_model = "{\"parent\": \"minecraft:item/generated\",\"textures\":{\"layer0\":\"minecraft:item/#TEXTURE\"}}"

remove_exceptions = [
    "cracked_turtle_egg",
    "big_dripleaf_stem",
    "_fence_gate_wall",
    "dead_sea_pickle",
    "_occupied_slot",
    "fire_side_alt0",
    "fire_side_alt1",
    "fire_up_alt0",
    "fire_up_alt1",
    "_empty_slot",
    "sniffer_egg_",
    "piston_head",
    "sea_pickles",
    "turtle_eggs",
    "candle_cake",
    "_fence_side",
    "thin_block",
    "fire_floor",
    "fire_side",
    "soul_fire",
    "orientable",
    "_contents",
    "flowerbed",
    "_mirrored",
    "_cauldron",
    "attached_",
    "repeater",
    "_candles",
    "_frustum",
    "tripwire",
    "template",
    "subtract",
    "fire_up",
    "flowing",
    "_filled",
    "_height",
    "_portal",
    "_middle",
    "custom_",
    "moving_",
    "_merge",
    "potted",
    "_stage",
    "_dust",
    "light",
    "_base",
    "_full",
    "cross",
    "level",
    "stem_",
    "crop",
    "_tip",
    "cube",
    "_alt"
]
replace_exceptions = [
    "_bottom_right_open",
    "_bottom_left_open",
    "_top_right_open",
    "_one_candle_lit",
    "_between_walls",
    "_top_left_open",
    "_on_raised_ne",
    "_on_raised_sw",
    "_bottom_right",
    "_partial_tilt",
    "_bottom_left",
    "_one_candle",
    "_noside_alt",
    "_wall_open",
    "_side_tall",
    "_plant_lit",
    "_hanging_0",
    "_hanging_1",
    "_hanging_2",
    "_top_right",
    "_hanging_3",
    "_hanging_4",
    "_raised_ne",
    "_raised_sw",
    "_full_tilt",
    "_side_alt",
    "_top_left",
    "_dust_dot",
    "_noside1",
    "_noside2",
    "_noside3",
    "_bottle0",
    "_bottle1",
    "_bottle2",
    "_slice2",
    "_slice3",
    "_slice4",
    "_slice5",
    "_slice6",
    "_empty0",
    "_empty1",
    "_empty2",
    "_slice1",
    "1_age0",
    "1_age1",
    "2_age0",
    "2_age1",
    "3_age0",
    "3_age1",
    "4_age0",
    "4_age1",
    "_conditional",
    "_horizontal",
    "_inventory",
    "_unstable",
    "_extended",
    "_vertical",
    "_inverted",
    "_inactive",
    "_hanging",
    "_pressed",
    "_ceiling",
    "_corner",
    "_curved",
    "_bottom",
    "_stable",
    "_active",
    "_noside",
    "_double",
    "_floor",
    "_outer",
    "_honey",
    "_inner",
    "_plant",
    "_dead",
    "_down",
    "_side",
    "_open",
    "wall_",
    "_post",
    "_save",
    "_load",
    "_data",
    "_ends",
    "_flat",
    "_lit",
    "_off",
    "_cap",
    "_top",
    "_map",
    "_on",
    "_ns",
    "_ew",
    "_0",
    "_1",
    "_2",
    "_3",
    "_4",
    "_x",
    "_y",
    "_z"
]
exact_exceptions = [
    "block",
    "stairs",
    "slab",
    "door",
    "wall",
    "fence",
    "fence_gate"
    "button",
    "pressure_plate",
    "banner",
    "lava",
    "water",
    "bell_wall",
    "pitcher",
    "inner_stairs",
    "outer_stairs",
    "frosted_ice",
    "crop",
    "pressure_plate_up"
]

def determine_blocks_to_flatten():
    blocks_to_flatten = ["repeater"]
    model_names = []
    for root, dirs, models in os.walk(vanilla_block_models_directory):
        for filename in models:
            model_name = os.path.splitext(filename)[0]

            for exception in replace_exceptions:
                model_name = model_name.replace(exception, "")

            for exception in remove_exceptions:
                if exception in model_name: model_name = ""

            for exception in exact_exceptions:
                if model_name == exception: model_name = ""

            if model_name in blocks_to_flatten: model_name = ""

            if model_name != "":
                blocks_to_flatten.append(model_name)
    return blocks_to_flatten

def flatten_blocks(blocks):
    existing_textures = []
    for root, dirs, textures in os.walk(textures_directory):
        for filename in textures:
            name = os.path.splitext(filename)[0]
            existing_textures.append(name)
    
    existing_models = []
    for root, dirs, models in os.walk(item_models_directory):
        for filename in models:
            name = os.path.splitext(filename)[0]
            existing_models.append(name)

    for blockname in blocks:
        if not blockname in existing_textures:
            destination_path = textures_directory + "/" + blockname + ".png"
            copyfile(placeholder_item_texture, destination_path)
            print("Missing texture added for " + blockname + "!")

        if not blockname in existing_models:
            model_string = template_item_model.replace("#TEXTURE", blockname)
            destination_path = item_models_directory + "/" + blockname + ".json"
            with open(destination_path, "w") as file:
                file.write(model_string)
                print("Missing model added for " + blockname + "!")
            

flatten_blocks(determine_blocks_to_flatten())