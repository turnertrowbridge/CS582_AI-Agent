import pyautogui
import time
from openai import OpenAI
import config

start_prompt = "Act like you are a 50s cartoon villian. Respond to questions asked to you in 150 characters or less."

# Replace these coordinates with the location of your game icon on the screen
game_icon_x, game_icon_y = 100, 100

# Replace these coordinates with the location of the text input field in your game
text_input_x, text_input_y = 500, 500

# Replace 'game_name' with the name of your game
game_name = "corporateclash"


def launch_game():
    pyautogui.click(game_icon_x, game_icon_y)
    time.sleep(5)  # Adjust this time according to your game's launch time


def type_message(message):
    pyautogui.click(text_input_x, text_input_y)
    pyautogui.press("t")
    time.sleep(0.5)
    pyautogui.typewrite(message)
    pyautogui.press("enter")


client = OpenAI(
    # This is the default and can be omitted
    api_key=config.api_key
)


def ask_chatgpt(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model=""
    )
    return chat_completion.choices[0].message["content"]


if __name__ == "__main__":

    prompt = input("Ask a question: ")
    response = ask_chatgpt(prompt)
    print(response)
    type_message("hi")
