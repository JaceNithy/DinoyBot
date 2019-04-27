#Plugins utilizados: PyAutoGUI e Numpy
import pyautogui
import time
from PIL import ImageGrab, ImageOps
from numpy import array

x = 1366/2
y = 720/2

class pLocalDino_ptr:
    #Botão infeliz
    Restar_Game = (340,390)
    #Dino (Player)
    Dinoy_Player = (90,325)
    #BodiusRadius é a box do Dino, leitura de pixels
    BodiusRadius = (126,317,195,256)
    #Ao morreu ele vai resetar o respawn
    Reset_Box = (315,394,266,337)

    #Os dois mais importantes
    Abaixar_ptr = (243,412,253,422)
    Pular_ptr = (243,387,253,399)

def Resetar_Game():
    pyautogui.click(pLocalDino_ptr.Restar_Game)

def JumpDino():
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    print("Pula dino")

def BaixarDino():
    pyautogui.keyDown('down')
    time.sleep(0.05)
    pyautogui.keyUp('down')
    print("Abaixa dino")

def imageGrab(box):
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    sum = a.sum()
    return sum

def is_game_ver():
    image = ImageGrab.grab(pLocalDino_ptr.Reset_Box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    sum = a.sum()

    if sum == 2934:
        return False
    else:
        return True

def main():
    Resetar_Game()
    while True:
        if imageGrab(pLocalDino_ptr.Abaixar_ptr) != 347:
            JumpDino()
            continue
        if imageGrab(pLocalDino_ptr.Pular_ptr) != 367:
            BaixarDino()


main()




