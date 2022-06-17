from model import *
import os, sys
os.system("python -m pip install pyautogui")
os.system("python -m pip install playsound")
import pyautogui, playsound

partys = arq("partys")
def sound():
    playsound.playsound("Urna Eletrônica.mp3")
    
def hide_all_windows():
    pyautogui.hotkey("win", "m")

def add_party(party_name):
    partys.write(party_name + "\n", "a")
        
def del_party(party_name):
    print(partys.content.replace(party_name, ""))
    partys.write(partys.content.replace(party_name, ""))



