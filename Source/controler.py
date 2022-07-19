from Source.model import *
import pyautogui, pygame, os, time
from pynput.keyboard import Key
import os

partys = arq(os.getcwd()  + ("\\Source" if "Source" not in os.getcwd() else "") + "\\Data\\partys")
progress = arq(os.getcwd()  + ("\\Source" if "Source" not in os.getcwd() else "") + "\\Data\\progress")
Program_Password = "12"

def remove_list_item(list, item_index):
    del(list[item_index])
    return list

def sound():
    pygame.mixer.init()
    pygame.mixer.music.load(os.getcwd()  + ("\\Source" if "Source" not in os.getcwd() else "") + "\\Data\\Urna Eletrônica.mp3")
    pygame.mixer.music.play()

def hide_all_windows():
    pyautogui.hotkey("win", "m")

def add_party(party_name):
    partys.write(party_name + "\n", "a")
        
def del_party(party_name):
    print(partys.content.replace(party_name, ""))
    partys.write(partys.content.replace(party_name, ""))

def check_election_progress():
    if "Running" in progress.content:
        return progress.content
    elif "Finished" in progress.content:
        return True
        
hotkeys = []

def check_exit_hotkeys(key):
    print(key)
    if key in [Key.cmd, Key.alt_l, Key.shift, Key.ctrl_l, Key.ctrl_r, Key.tab]:
        time.sleep(0.2)
        pyautogui.press("")
        
        
