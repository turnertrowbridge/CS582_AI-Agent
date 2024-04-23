import pyautogui
from openai import OpenAI
import time

TEXT_INPUT_X, TEXT_INPUT_Y = 500, 500


class Client:
    def __init__(self, api_key, item_info):
        self.client = OpenAI(
            api_key=api_key
        )
        # Replace these coordinates with the location of the text input field in your game
        self.text_input_x = TEXT_INPUT_X
        self.text_input_y = TEXT_INPUT_Y
        self.start_prompt = "Act like you are a 50s cartoon villian. Respond to questions asked to you in 100 characters or less."
        self.item_info = item_info

    # Type message that is passed in by asking the AI
    def type_message(self, message):
        pyautogui.click(self.text_input_x, self.text_input_y)
        print("Typing message:", message)
        pyautogui.press("t")
        time.sleep(0.5)
        for char in message:
            pyautogui.typewrite(char)
            # time.sleep(random.normalvariate(typing_speed_mean, typing_speed_std_dev))
        pyautogui.press("enter")

    def ask_chatgpt(self, prompt):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": self.start_prompt
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message.content

    def ask_gag_choice(self, items):
        prompt = (f"You have {len(items)} and you need to pick exactly 1 of them. Say back to me only the name of the "
                  f"item, no added words or punctuation. Here are the items:")

        for item in items[:-1]:
            prompt += self.item_info[item]["name"] + ", "
        prompt += self.item_info[items[-1]]["name"]

        print(prompt)

        return self.ask_chatgpt(prompt)


def get_description_from_name(name, items_database):
    for item in items_database.values():
        if item["name"] == name:
            return item["description"]
    return ""
