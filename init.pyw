import os, pyautogui
from view import *
os.system("start " + os.getcwd() + r"\Data\chedkDir.bat")
with open("Data\dir.txt", "r") as arq:
    if "AutoHotkey" in arq.read():
        pyautogui.alert("Já tá instalado")
    else:
        pyautogui.alert("Ainda não tá instalado")
        os.system("start " + os.getcwd() + r"\Data\installAutoHotkey.bat")
        os.system("start " + os.getcwd() + r"\Data\chedkDir.bat")
app = app()
