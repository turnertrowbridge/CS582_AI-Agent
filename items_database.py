import os

item_info = {
    "op_slice": {
        "name": "op_slice",
        "file_path": "",
        "type": "throw",
        "description": "Slice of cream pie",
        "damage": 10
    },

    "slice": {
        "name": "slice",
        "file_path": "",
        "type": "throw",
        "description": "Slice of cream pie",
        "damage": 10
    }
}


def set_filepaths():
    for item in item_info:
        item_info[item]["file_path"] = os.path.join("pictures", item) + ".png"

