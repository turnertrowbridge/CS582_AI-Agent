import os
os.environ["OPENCV_LOG_LEVEL"]="FATAL"  # Suppress OpenCV warnings before importing pyautogui

import pyautogui
import time
import config
import gpt_client
import items_database
import gag_selecting

GAME_ICON_X, GAME_ICON_Y = 100, 100

game_name = "corporateclash"

typing_speed_mean = 0.001  # Mean time between keystrokes in seconds
typing_speed_std_dev = 0.02  # Standard deviation of typing speed in seconds


def launch_game():
    pyautogui.click(GAME_ICON_X, GAME_ICON_Y)
    time.sleep(5)  # Adjust this time according to your game's launch time


def main():
    items_database.set_filepaths()  # loads the file paths for the items in the database based on os
    launch_game()  # Launch the game

    # Set up Client
    client = gpt_client.Client(config.API_KEY, items_database.item_info)

    while True:
        # see what gags are possible to be used
        found_items = gag_selecting.find_items()
        if not found_items:
            print("No items found")
            time.sleep(1)
            continue

        # forward items to the AI and get item back
        chosen_item = client.ask_gag_choice(found_items)

        # ask_chatgpt about the item and type joke or taunt
        chosen_item_description = gag_selecting.get_description_from_name(chosen_item, items_database.item_info)
        client.say_gag_commentary(chosen_item_description)

        # click on the gag
        chosen_item_image = gag_selecting.get_filepath(chosen_item)
        gag_selecting.click_picture(chosen_item_image)

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
