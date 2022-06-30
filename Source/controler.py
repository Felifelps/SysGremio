from model import *
import pyautogui, pygame, os, time
from pynput.keyboard import Key

partys = arq(r"Data\partys")
Program_Password = "12"

def sound():
    pygame.mixer.init()
    pygame.mixer.music.load(r'Data\Urna Eletrônica.mp3')
    pygame.mixer.music.play()

def hide_all_windows():
    pyautogui.hotkey("win", "m")

def add_party(party_name):
    partys.write(party_name + "\n", "a")
        
def del_party(party_name):
    print(partys.content.replace(party_name, ""))
    partys.write(partys.content.replace(party_name, ""))

hotkeys = []

def check_exit_hotkeys(key):
    print(key)
    if key in [Key.cmd, Key.alt_l, Key.shift, Key.ctrl_l, Key.ctrl_r, Key.tab]:
        time.sleep(0.2)
        pyautogui.press("")
        
        
