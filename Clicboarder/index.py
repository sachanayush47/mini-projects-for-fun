import keyboard
from constants import *
from triggers import copy_content, paste_content, exit_program


def register_copy_hotkeys():
    for copy_hot_key in COPY_HOT_KEYS:
        key_number = int(copy_hot_key.split('+')[-1])
        keyboard.add_hotkey(copy_hot_key, lambda key_number=key_number: copy_content(key_number))


def register_paste_hotkey():
    for paste_hot_key in PASTE_HOT_KEYS:
        key_number = int(paste_hot_key.split('+')[-1])
        keyboard.add_hotkey(paste_hot_key, lambda key_number=key_number: paste_content(key_number))


def register_program_hotkeys():
    keyboard.add_hotkey(STOP_HOT_KEY, exit_program)


register_copy_hotkeys()
register_paste_hotkey()
register_program_hotkeys()


# Block forever, waiting for the hotkey to be pressed
keyboard.wait()


