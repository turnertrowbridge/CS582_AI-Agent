import os

item_info = {
    "op_feather": {
        "name": "op_feather",
        "file_path": "",
        "type": "toonup",
        "description": "Healing an ally by tickling them with a feather",
        "damage": 12
    },

    "feather": {
        "name": "feather",
        "file_path": "",
        "type": "toonup",
        "description": "Healing an ally by tickling them with a feather",
        "damage": 12
    },
    
    "op_megaphone": {
        "name": "op_megaphone",
        "file_path": "",
        "type": "toonup",
        "description": "Healing an ally by saying a funny joke",
        "damage": 24
    },

    "megaphone": {
        "name": "megaphone",
        "file_path": "",
        "type": "toonup",
        "description": "Healing an ally by saying a funny joke",
        "damage": 24
    },
    
    "op_lipstick": {
        "name": "op_lipstick",
        "file_path": "",
        "type": "toonup",
        "description": "Healing an ally by giving them a kiss",
        "damage": 30
    },

    "lipstick": {
        "name": "lipstick",
        "file_path": "",
        "type": "toonup",
        "description": "Healing an ally by giving them a kiss",
        "damage": 30
    },
    
    "op_bamboo_cane": {
        "name": "op_bamboo_cane",
        "file_path": "",
        "type": "toonup",
        "description": "Healing an ally by doing a funny dance",
        "damage": 45
    },

    "bamboo_cane": {
        "name": "bamboo_cane",
        "file_path": "",
        "type": "toonup",
        "description": "Healing an ally by doing a funny dance",
        "damage": 45
    },
    
    "op_banana_peel": {
        "name": "op_banana_peel",
        "file_path": "",
        "type": "trap",
        "description": "Throwing a banana peel for the enemy robot to slip on",
        "damage": 14
    },

    "banana_peel": {
        "name": "banana_peel",
        "file_path": "",
        "type": "trap",
        "description": "Throwing a banana peel for the enemy robot to slip on",
        "damage": 14
    },
    
    "op_rake": {
        "name": "op_rake",
        "file_path": "",
        "type": "trap",
        "description": "Throwing a rake for the enemy robot to step on",
        "damage": 28
    },

    "rake": {
        "name": "rake",
        "file_path": "",
        "type": "trap",
        "description": "Throwing a rake for the enemy robot to step on",
        "damage": 28
    },
    
    "op_springboard": {
        "name": "op_springboard",
        "file_path": "",
        "type": "trap",
        "description": "Setting a springboard up for the enemy robot to step on",
        "damage": 45
    },

    "springboard": {
        "name": "springboard",
        "file_path": "",
        "type": "trap",
        "description": "Setting a springboard up for the enemy robot to step on",
        "damage": 45
    },
    
    "op_marbles": {
        "name": "op_marbles",
        "file_path": "",
        "type": "trap",
        "description": "Throwing marbles for the enemy robot to slip on",
        "damage": 75
    },

    "marbles": {
        "name": "marbles",
        "file_path": "",
        "type": "trap",
        "description": "Throwing marbles for the enemy robot to slip on",
        "damage": 75
    },
    
    "op_one_dollar": {
        "name": "op_one_dollar",
        "file_path": "",
        "type": "lure",
        "description": "Baiting or luring the enemy robot into stepping toward you with a one dollar bill",
        "damage": 0
    },

    "one_dollar": {
        "name": "one_dollar",
        "file_path": "",
        "type": "lure",
        "description": "Baiting or luring the enemy robot into stepping toward you with a one dollar bill",
        "damage": 0
    },
    
    "op_small_magnet": {
        "name": "op_small_magnet",
        "file_path": "",
        "type": "lure",
        "description": "Using a small magnet to bait or lure the enemy robot closer to you",
        "damage": 0
    },

    "small_magnet": {
        "name": "small_magnet",
        "file_path": "",
        "type": "lure",
        "description": "Using a small magnet to bait or lure the enemy robot closer to you",
        "damage": 0
    },
    
    "op_five_dollar": {
        "name": "op_five_dollar",
        "file_path": "",
        "type": "lure",
        "description": "Baiting or luring the enemy robot into stepping toward you with a five dollar bill",
        "damage": 0
    },

    "five_dollar": {
        "name": "five_dollar",
        "file_path": "",
        "type": "lure",
        "description": "Baiting or luring the enemy robot into stepping toward you with a five dollar bill",
        "damage": 0
    },
    
    "op_big_magnet": {
        "name": "op_big_magnet",
        "file_path": "",
        "type": "lure",
        "description": "Using a big magnet to bait or lure the enemy robot closer to you",
        "damage": 0
    },

    "big_magnet": {
        "name": "big_magnet",
        "file_path": "",
        "type": "lure",
        "description": "Using a big magnet to bait or lure the enemy robot closer to you",
        "damage": 0
    },
    
    "op_cupcake": {
        "name": "op_cupcake",
        "file_path": "",
        "type": "throw",
        "description": "Throwing a cupcake at the enemy robot",
        "damage": 8
    },

    "cupcake": {
        "name": "cupcake",
        "file_path": "",
        "type": "throw",
        "description": "Throwing a cupcake at the enemy robot",
        "damage": 8
    },
    
    "op_slice_fruit": {
        "name": "op_slice_fruit",
        "file_path": "",
        "type": "throw",
        "description": "Throwing a slice of fruit pie at the enemy robot",
        "damage": 13
    },

    "slice_fruit": {
        "name": "slice_fruit",
        "file_path": "",
        "type": "throw",
        "description": "Throwing a slice of fruit pie at the enemy robot",
        "damage": 13
    },
    
    "op_slice_cream": {
        "name": "op_slice_cream",
        "file_path": "",
        "type": "throw",
        "description": "Throwing a slice of cream pie at the enemy robot",
        "damage": 20
    },

    "slice_cream": {
        "name": "slice_cream",
        "file_path": "",
        "type": "throw",
        "description": "Throwing a slice of cream pie at the enemy robot",
        "damage": 20
    },
    
    "op_slice_birthday": {
        "name": "op_slice_birthday",
        "file_path": "",
        "type": "throw",
        "description": "Throwing a slice of birthday cake at the enemy robot",
        "damage": 35
    },

    "slice_birthday": {
        "name": "slice_birthday",
        "file_path": "",
        "type": "throw",
        "description": "Throwing a slice of birthday cake at the enemy robot",
        "damage": 35
    },
    
    "op_squirt_flower": {
        "name": "op_squirt_flower",
        "file_path": "",
        "type": "squirt",
        "description": "Using a prank flower to squirt water on the enemy robot",
        "damage": 4
    },

    "squirt_flower": {
        "name": "squirt_flower",
        "file_path": "",
        "type": "squirt",
        "description": "Using a prank flower to squirt water on the enemy robot",
        "damage": 4
    },
    
    "op_glass_water": {
        "name": "op_glass_water",
        "file_path": "",
        "type": "squirt",
        "description": "Spitting water on the enemy robot",
        "damage": 8
    },

    "glass_water": {
        "name": "glass_water",
        "file_path": "",
        "type": "squirt",
        "description": "Spitting water on the enemy robot",
        "damage": 8
    },
    
    "op_squirtgun": {
        "name": "op_squirtgun",
        "file_path": "",
        "type": "squirt",
        "description": "Shooting the enemy robot with a squirtgun",
        "damage": 12
    },

    "squirtgun": {
        "name": "squirtgun",
        "file_path": "",
        "type": "squirt",
        "description": "Shooting the enemy robot with a squirtgun",
        "damage": 12
    },
    
    "op_water_balloon": {
        "name": "op_water_balloon",
        "file_path": "",
        "type": "squirt",
        "description": "Throwing a water balloon at the enemy robot",
        "damage": 21
    },

    "water_balloon": {
        "name": "water_balloon",
        "file_path": "",
        "type": "squirt",
        "description": "Throwing a water balloon at the enemy robot",
        "damage": 21
    },
    
    "op_joybuzzer": {
        "name": "op_joybuzzer",
        "file_path": "",
        "type": "zap",
        "description": "Zapping the enemy robot with a buzzer",
        "damage": 12
    },

    "joybuzzer": {
        "name": "joybuzzer",
        "file_path": "",
        "type": "zap",
        "description": "Zapping the enemy robot with a buzzer",
        "damage": 12
    },
    
    "op_lightbulb": {
        "name": "op_lightbulb",
        "file_path": "",
        "type": "zap",
        "description": "Zapping the enemy robot by throwing a lightbulb at them",
        "damage": 20
    },

    "lightbulb": {
        "name": "lightbulb",
        "file_path": "",
        "type": "zap",
        "description": "Zapping the enemy robot by throwing a lightbulb at them",
        "damage": 20
    },
    
    "op_radio": {
        "name": "op_radio",
        "file_path": "",
        "type": "zap",
        "description": "Zapping the enemy robot with a broken radio",
        "damage": 36
    },

    "radio": {
        "name": "radio",
        "file_path": "",
        "type": "zap",
        "description": "Zapping the enemy robot with a broken radio",
        "damage": 36
    },
    
    "op_kart_battery": {
        "name": "op_kart_battery",
        "file_path": "",
        "type": "zap",
        "description": "Zapping the enemy robot with a car battery",
        "damage": 60
    },

    "kart_battery": {
        "name": "kart_battery",
        "file_path": "",
        "type": "zap",
        "description": "Zapping the enemy robot with a car battery",
        "damage": 60
    },
    
    "op_kazoo": {
        "name": "op_kazoo",
        "file_path": "",
        "type": "sound",
        "description": "Hurting the enemy robot's ears by playing the kazoo",
        "damage": 5
    },

    "kazoo": {
        "name": "kazoo",
        "file_path": "",
        "type": "sound",
        "description": "Hurting the enemy robot's ears by playing the kazoo",
        "damage": 5
    },
    
    "op_bike_horn": {
        "name": "op_bike_horn",
        "file_path": "",
        "type": "sound",
        "description": "Hurting the enemy robot's ears by squeaking a bike horn",
        "damage": 10
    },

    "bike_horn": {
        "name": "bike_horn",
        "file_path": "",
        "type": "sound",
        "description": "Hurting the enemy robot's ears by squeaking a bike horn",
        "damage": 10
    },
    
    "op_whistle": {
        "name": "op_whistle",
        "file_path": "",
        "type": "sound",
        "description": "Hurting the enemy robot's ears by using a whistle",
        "damage": 16
    },

    "whistle": {
        "name": "whistle",
        "file_path": "",
        "type": "sound",
        "description": "Hurting the enemy robot's ears by using a whistle",
        "damage": 16
    },
    
    "op_bugle": {
        "name": "op_bugle",
        "file_path": "",
        "type": "sound",
        "description": "Hurting the enemy robot's ears by playing a bugle",
        "damage": 23
    },

    "bugle": {
        "name": "bugle",
        "file_path": "",
        "type": "sound",
        "description": "Hurting the enemy robot's ears by playing a bugle",
        "damage": 23
    },
    
    "op_flowerpot": {
        "name": "op_flowerpot",
        "file_path": "",
        "type": "drop",
        "description": "Dropping a flowerpot on the enemy robot's head",
        "damage": 12
    },

    "flowerpot": {
        "name": "flowerpot",
        "file_path": "",
        "type": "drop",
        "description": "Dropping a flowerpot on the enemy robot's head",
        "damage": 12
    },
    
    "op_sandbag": {
        "name": "op_sandbag",
        "file_path": "",
        "type": "drop",
        "description": "Dropping a sandbag on the enemy robot's head",
        "damage": 20
    },

    "sandbag": {
        "name": "sandbag",
        "file_path": "",
        "type": "drop",
        "description": "Dropping a sandbag on the enemy robot's head",
        "damage": 20
    },
    
    "op_bowling_ball": {
        "name": "op_bowling_ball",
        "file_path": "",
        "type": "drop",
        "description": "Dropping a bowling ball on the enemy robot's head",
        "damage": 35
    },

    "bowling_ball": {
        "name": "bowling_ball",
        "file_path": "",
        "type": "drop",
        "description": "Dropping a bowling ball on the enemy robot's head",
        "damage": 35
    },
    
    "op_anvil": {
        "name": "op_anvil",
        "file_path": "",
        "type": "drop",
        "description": "Dropping an anvil on the enemy robot's head",
        "damage": 56
    },

    "anvil": {
        "name": "anvil",
        "file_path": "",
        "type": "drop",
        "description": "Dropping an anvil on the enemy robot's head",
        "damage": 56
    }
    
}


def set_filepaths():
    for item in item_info:
        item_info[item]["file_path"] = os.path.join("pictures", item) + ".png"

