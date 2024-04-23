import os

import pyautogui
import math
from items_database import item_info
import threading


def search_items_chunk(items, found_items):
    for item in items:
        res = None
        try:
            res = pyautogui.locateOnScreen(item_info[item]["file_path"], confidence=0.9)
        except Exception as e:
            # Errors are expected if the item is not found
            pass
            # print("Could not find item", item, "\nerror:", e)
        if res:
            found_items.append(item)


def find_items():
    items = list(item_info.keys())
    chunk_size = math.ceil(len(items) / 7)  # Divide items into approximately equal chunks
    chunks = [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
    found_items = []
    threads = []

    for chunk in chunks:
        thread = threading.Thread(target=search_items_chunk, args=(chunk, found_items))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return found_items


def click_picture(picture):
    try:
        res = pyautogui.locateOnScreen(picture, confidence=0.9)
        print(res)
        pyautogui.click(res)
        print("clicking")
    except Exception as e:
        print("not found", e)


def get_description_from_name(name, items_database):
    for item in items_database.values():
        if item["name"] == name:
            return item["description"]
    return ""


def get_filepath(chosen_item):
    chosen_item_image = os.path.join("pictures", chosen_item) + ".png"
    return chosen_item_image
