import pyautogui
import time
from openai import OpenAI
import config
import random

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


if __name__ == "__main__":
    while True:
        prompt = input("Ask a question: ")
        response = ask_chatgpt(prompt)
        type_message(response)
        click_picture("", "./pictures/op_slice.png")
