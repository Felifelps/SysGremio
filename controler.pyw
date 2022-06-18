from model import *
import pyautogui, pygame

partys = arq("partys")
def sound():
    pygame.mixer.init()
    pygame.mixer.music.load('Urna Eletrônica.mp3')
    pygame.mixer.music.play()

def hide_all_windows():
    pyautogui.hotkey("win", "m")

def add_party(party_name):
    partys.write(party_name + "\n", "a")
        
def del_party(party_name):
    print(partys.content.replace(party_name, ""))
    partys.write(partys.content.replace(party_name, ""))


