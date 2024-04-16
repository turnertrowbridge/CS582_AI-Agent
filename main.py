import pyautogui
import time
from openai import OpenAI
import config
import random
from items_database import item_info

start_prompt = "Act like you are a 50s cartoon villian. Respond to questions asked to you in 100 characters or less."

# Replace these coordinates with the location of your game icon on the screen
game_icon_x, game_icon_y = 100, 100

# Replace these coordinates with the location of the text input field in your game
text_input_x, text_input_y = 500, 500

conversation_history = []

# Replace 'game_name' with the name of your game
game_name = "corporateclash"

typing_speed_mean = 0.001  # Mean time between keystrokes in seconds
typing_speed_std_dev = 0.02  # Standard deviation of typing speed in seconds


def launch_game():
    pyautogui.click(game_icon_x, game_icon_y)
    time.sleep(5)  # Adjust this time according to your game's launch time


def type_message(message):
    pyautogui.click(text_input_x, text_input_y)
    print("Typing message:", message)
    pyautogui.press("t")
    time.sleep(0.5)
    for char in message:
        pyautogui.typewrite(char)
        # time.sleep(random.normalvariate(typing_speed_mean, typing_speed_std_dev))
    pyautogui.press("enter")


client = OpenAI(
    # This is the default and can be omitted
    api_key=config.API_KEY,
)


def ask_chatgpt(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": start_prompt
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content


def click_picture(response, picture):
    words = response.split(" ")
    try:
        # if "the" in words:
        res = pyautogui.locateOnScreen(picture, confidence=0.9)
        print(res)
        pyautogui.click(res)
        print("clicking")
    except Exception as e:
        print("not found", e)
        
def ask_gag_choice(items):
    prompt = f"You have {len(items)} and you need to pick exactly 1 of them. Say back to me only the name of the item, no added words or punctuation. Here are the items: "
    
    for item in items[:-1]:
        prompt += item_info[item]["name"] + ", "
    prompt += item_info[items[-1]]["name"]        
    
    print(prompt)  
    
    return ask_chatgpt(prompt)


def find_items():
    items = [".\pictures\op_slice.png", ".\pictures\slice.png"]
    found_items = []
    for item in items:
        res = None
        try:
            res = pyautogui.locateOnScreen(item, confidence=0.9)
        except Exception as e:
            print("Could not find item", item, "\nerror:", e)
        if res:
            found_items.append(item)
    return found_items


def ai_loop():
    while True:
        found_items = find_items()  # returns list of item.png
        if not found_items:
            print("No items found")
            time.sleep(1)
            continue
        # forward items to the AI and get item back
        chosen_item = ask_gag_choice(found_items)

        # ask_chatgpt about the item
        # type_message(response)
        type_message(f"I chose {chosen_item}")
        #pyautogui.click(chosen_item)
        input("Press enter to continue: ")

def old_test():
    while True:
        prompt = input("Ask a question: ")
        response = ask_chatgpt(prompt)
        type_message(response)
        click_picture("", "./pictures/op_slice.png")


if __name__ == "__main__":
    #old_test()
    ai_loop()
