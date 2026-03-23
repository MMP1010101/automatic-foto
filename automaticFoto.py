from pynput import keyboard
import subprocess

def take_screenshot():
    subprocess.run(["gnome-screenshot", "-c"])

def on_press(key):
    try:
        if key.char == "/":
            take_screenshot()
    except:
        pass

print("Pulsa '/' para capturar y copiar 📸")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
