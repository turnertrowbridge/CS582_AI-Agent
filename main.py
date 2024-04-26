import os
os.environ["OPENCV_LOG_LEVEL"] = "FATAL"


import time
import config
import gpt_client
import items_database
import auto_gui
import chat_reply

game_name = "corporateclash"

typing_speed_mean = 0.001  # Mean time between keystrokes in seconds
typing_speed_std_dev = 0.02  # Standard deviation of typing speed in seconds


def main():
    items_database.set_filepaths()  # loads the file paths for the items in the database based on os
    auto_gui.launch_game()  # Launch the game

    # Set up Client
    client = gpt_client.Client(config.API_KEY, items_database.item_info)

    while True:
        print("Checking if in battle...")
        print("In battle: ", auto_gui.in_battle())

        if auto_gui.free_to_run():
            print("Free to run, running...")
            auto_gui.run_to_next_floor()
            time.sleep(1)
            client.reset_item_history()

        elif auto_gui.in_battle():
            print("In battle")

            print("Looking for gags...")

            # see what gags are possible to be used
            found_items = auto_gui.find_items()
            if not found_items:
                print("No gags found")
                time.sleep(1)
                continue

            # forward items to the AI and get item back
            chosen_item = client.ask_gag_choice(found_items)
            print("Selected item: ", chosen_item)

            # ask_chatgpt about the item and type joke or taunt
            chosen_item_description = auto_gui.get_description_from_name(chosen_item, items_database.item_info)
            client.say_gag_commentary(chosen_item_description)
            time.sleep(1)
            auto_gui.close_chat()

            # click on the gag
            chosen_item_image = auto_gui.get_filepath(chosen_item)
            auto_gui.click_picture(chosen_item_image)
            time.sleep(1)

            # See if in multi-cog battle and select an arrow if so
            if auto_gui.arrow_on_screen_and_click():
                time.sleep(1)
                continue

        elif auto_gui.arrow_on_screen_and_click():
            time.sleep(1)

        # Check last chat
        else:
            time.sleep(2)
            chat_reply_instance = chat_reply.ChatReply(client)
            chat_reply_instance.click_npc_chat_tab()
            reply = chat_reply_instance.process_last_chat_and_reply()
            if reply:
                client.type_message(reply)

            auto_gui.close_chat()

        time.sleep(0)


if __name__ == "__main__":
    main()
