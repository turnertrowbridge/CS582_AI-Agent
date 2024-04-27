import pyautogui
from openai import OpenAI
import time
import prompts

TEXT_INPUT_X, TEXT_INPUT_Y = 500, 500


class Client:
    def __init__(self, api_key, item_info):
        self.client = OpenAI(
            api_key=api_key
        )
        # Replace these coordinates with the location of the text input field in your game
        self.text_input_x = TEXT_INPUT_X
        self.text_input_y = TEXT_INPUT_Y
        self.start_prompt = prompts.start_prompt
        self.item_info = item_info
        self.item_history = []

    def has_item_history(self):
        return len(self.item_history) > 0

    # Type message that is passed in by asking the AI
    def type_message(self, message):
        pyautogui.click(self.text_input_x, self.text_input_y)
        print("Typing message:", message)
        pyautogui.press("t")
        time.sleep(0.5)
        for char in message:
            pyautogui.write(char, interval=0.001)  # lower interval to type faster
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

    # Asks AI about gag and saves the choice
    def ask_chatgpt_about_gag(self, prompt):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
        response = chat_completion.choices[0].message.content

        self.item_history.append(response)
        print("Item history:", self.item_history)
        return response

    def ask_gag_choice(self, items):
        prompt = ""
        if self.item_history:
            prompt += prompts.past_items_prompt
            for item in self.item_history:
                try:
                    prompt += f'item: {self.item_info[item]["name"]} - type: {self.item_info[item]["type"]}\n '
                except KeyError:
                    print("Item not found in item_info")
                    continue

        prompt += f"You have {len(items)} {prompts.item_selection_prompt}"

        for item in items:
            prompt += f'item: {self.item_info[item]["name"]} - type: {self.item_info[item]["type"]} \n'

        print(prompt)

        return self.ask_chatgpt_about_gag(prompt)

    def say_gag_commentary(self, chosen_item_desc):
        prompt = "In 100 characters or less, make a joke or taunt your enemy relating to this action: " + chosen_item_desc
        item_taunt_or_joke = self.ask_chatgpt(prompt)
        self.type_message(item_taunt_or_joke)

    def reset_item_history(self):
        self.item_history = []





