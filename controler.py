from model import *
import pyautogui, pygame
from pynput.keyboard import *

keyboard = Controller()
partys = arq(r"Data\partys")
Program_Password = "12"

def dont_close_vote_screen():
    def see(key):
        print(key)
        if key == Key.alt_l:
            pyautogui.alert("Não é permitido sair sem votar")
        elif key == Key.cmd:
            keyboard.press(Key.esc)
            pyautogui.alert("Não é permitido sair sem votar")
        
        
    with Listener(on_press=see) as l:
        l.join()

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


