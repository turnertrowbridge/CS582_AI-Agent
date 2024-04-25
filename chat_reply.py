import pyautogui
import pytesseract
from PIL import Image

# Function to recognize text from an image


def recognize_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Function to capture a screenshot of the text box region


def capture_text_box_region(x, y, width, height):
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save('text_box_screenshot.png')

def get_last_chat(messages):
    messages = messages.split(':')
    return messages[-1]

# Example coordinates of the text box region (adjust as per your screen)
text_box_x = 20
text_box_y = 110
text_box_width = 620
text_box_height = 250

# Capture screenshot of the text box region
capture_text_box_region(text_box_x, text_box_y,
                        text_box_width, text_box_height)

# Recognize text from the captured screenshot
recognized_text = recognize_text('text_box_screenshot.png')

# Process the recognized text
print("Recognized Text:", recognized_text)

print("Last Chat:", get_last_chat(recognized_text))
