from model import *
import pyautogui, pygame, os

partys = arq(r"Data\partys")
Program_Password = "12"

def check_exit_hotkeys(key):
    print(key)

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


    

