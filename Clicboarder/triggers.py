import keyboard
import pyperclip
import time

DATA = {}


def exit_program():
    keyboard.unhook_all_hotkeys()
    exit(0)


def copy_content(key):
    if keyboard.is_pressed('ctrl+c'):
        save_content(key)

        
def save_content(key):
    time.sleep(0.1)
    clipboard_content = pyperclip.paste()
    DATA[key] = clipboard_content
    print(DATA)
    

def get_content(key):
    content = DATA.get(key)
    return '' if content == None else content


def paste_content(key):
    current_content = pyperclip.paste()
    content = get_content(key)
    pyperclip.copy(content)
    keyboard.press_and_release('ctrl+v')
    pyperclip.copy(current_content)
    