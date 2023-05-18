import time
import datetime
import subprocess
import pyautogui
from PIL import ImageGrab

def open_browser(url, program):
    subprocess.Popen(program)
    pyautogui.sleep(1)

    window = pyautogui.getWindowsWithTitle('New Tab')[0]
    window.maximize()

    pyautogui.write(url)
    pyautogui.press('enter')
    pyautogui.sleep(1)

    return pyautogui.getWindowsWithTitle('Search Cross Domain AD Users')[0]

def search_term(term, location, search_locations):
    search_box_location = search_locations[location]['search_box']
    submit_button_location = search_locations[location]['submit_button']
    hyperlink_location = search_locations[location]['hyperlink']

    pyautogui.click(search_box_location)
    pyautogui.typewrite(term)
    pyautogui.click(submit_button_location)
    time.sleep(3)
    pyautogui.click(hyperlink_location)
    time.sleep(3)


def take_screenshot(term, timestamp):
    screenshot = ImageGrab.grab()
    screenshot_filename = f"{term}_{timestamp}.png"
    screenshot.save(screenshot_filename)
    time.sleep(1)

'''
def take_screenshot(term, timestamp):
    screenshot_filename = f"{term}_{timestamp}.png"
    pyautogui.screenshot(screenshot_filename)
    time.sleep(1)
'''    

if __name__ == "__main__":
    url = 'https://adsearch.internal.t-mobile.com/'
    search_terms = ['RHolton1', 'BRawson', 'ASali6']
    program = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    search_locations = {
        'location1': {
            'search_box': (1315, 435),
            'submit_button': (1525, 435),
            'hyperlink': (336, 575)
        },
        'location2': {
            'search_box': (1475, 220),
            'submit_button': (1690, 220),
            'hyperlink': (336, 575)
        }
    }

    now = datetime.datetime.now()
    timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')

    main_window = open_browser(url, program)
    main_window.activate()

    for i, term in enumerate(search_terms):
        location = 'location1' if i == 0 else 'location2'
        time.sleep(3)
        search_term(term, location, search_locations)
        print(term)
        time.sleep(3)
        take_screenshot(term, timestamp)
        print(term)
        time.sleep(3)
        i += 1


