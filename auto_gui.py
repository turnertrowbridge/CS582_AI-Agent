import os
import pyautogui
import math
from items_database import item_info
import threading
import time

GAME_ICON_X, GAME_ICON_Y = 100, 150


def search_items_chunk(items, found_items):
    for item in items:
        res = None
        try:
            res = pyautogui.locateOnScreen(
                item_info[item]["file_path"], confidence=0.99)
        except Exception:
            # Errors are expected if the item is not found
            pass
            # print("Could not find item", item, "\nerror:", e)
        if res:
            found_items.append(item)


def find_items():
    items = list(item_info.keys())
    # Divide items into approximately equal chunks
    chunk_size = math.ceil(len(items) / 8)
    chunks = [items[i:i + chunk_size]
              for i in range(0, len(items), chunk_size)]
    found_items = []
    threads = []

    for chunk in chunks:
        thread = threading.Thread(
            target=search_items_chunk, args=(chunk, found_items))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return found_items


def find_item_on_screen(picture):
    try:
        res = pyautogui.locateOnScreen(picture, confidence=0.8)
        return res
    except Exception:
        return None


def click_picture(picture):
    try:
        res = pyautogui.locateOnScreen(picture, confidence=0.9)
        print(res)
        pyautogui.click(res)
        print("clicking")
        pyautogui.click(GAME_ICON_X, GAME_ICON_Y)
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


def free_to_run():
    return find_item_on_screen(get_filepath("book")) is not None


def in_battle():
    return find_item_on_screen(get_filepath("gag_question")) is not None


def run_to_next_floor():
    pyautogui.keyDown("w")
    time.sleep(5)


def arrow_on_screen_and_click():
    arrow = get_filepath("arrow")

    if find_item_on_screen(arrow):
        print("Arrow found and clicked")
        click_picture(arrow)
        return True
    else:
        return False


def launch_game():
    pyautogui.click(GAME_ICON_X, GAME_ICON_Y)
    time.sleep(5)  # Adjust this time according to your game's launch time


def close_chat():
    pyautogui.click(673, 79)
    time.sleep(1)
