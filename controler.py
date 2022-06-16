from model import *
import pyautogui

partys = arq("partys")

def hide_all_windows():
    pyautogui.hotkey("win", "m")

def add_party(party_name):
    partys.write(party_name + "\n", "a")
        
def del_party(party_name):
    print(partys.content.replace(party_name, ""))
    artys.write(partys.content.replace(party_name, ""))



