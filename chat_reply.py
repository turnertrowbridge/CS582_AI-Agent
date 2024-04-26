import pyautogui
import pytesseract
from PIL import Image
import time


class ChatReply:
    def __init__(self, client):
        self.client = client
        self.text_box_x = 20
        self.text_box_y = 110
        self.text_box_width = 620
        self.text_box_height = 250
        self.last_chat = None
        self.default_screenshot_path = 'text_box_screenshot.png'

    # Function to recognize text from an image
    def _recognize_text(self, image_path):
        try:
            image = Image.open(image_path)
        except Exception:
            return None
        try:
            text = pytesseract.image_to_string(image)
        except Exception:
            return None
        return text

    # Function to capture a screenshot of the text box region
    def _capture_text_box_region(self):
        screenshot = pyautogui.screenshot(region=(self.text_box_x, self.text_box_y,
                                                  self.text_box_width, self.text_box_height))
        screenshot.save(self.default_screenshot_path)
        return self.default_screenshot_path

    # Function to extract the last chat message from the recognized text
    def _get_last_chat(self, messages):
        messages = messages.split(':')
        return messages[-1]

    def click_npc_chat_tab(self):
        pyautogui.press('t')
        pyautogui.click(440, 75)

    def process_last_chat_and_reply(self):
        time.sleep(2)
        screenshot_path = self._capture_text_box_region()
        text = self._recognize_text(screenshot_path)
        last_chat = self._get_last_chat(text)
        print("Last chat:", last_chat)

        if last_chat != self.last_chat:
            print("New last chat detected")
            self.last_chat = last_chat
            reply = self.client.ask_chatgpt(last_chat)
            print("Reply:", reply)
            return reply
        return None
