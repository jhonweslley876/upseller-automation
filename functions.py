import pyautogui
import random
import time
import keyboard
import pyperclip

def pageCounter(counter):
    mouseMovFunction(757, 100)
    time.sleep(0.1)


    keyboard.write(str(counter))
    time.sleep(0.1)


    keyboard.press_and_release('enter')
    time.sleep(0.1)

#Função que pega o nome do cliente na nota fiscal
def nameSelect():
    global name

    width = 1366
    height_base = 768

    width, height = pyautogui.size()

    new_x = int(337 * width / width)
    new_y = int(175 * height / height_base)

    pyautogui.doubleClick(new_x, new_y)
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.1)
    name = pyperclip.paste()
    time.sleep(0.1)

#Função que move e clica o mouse para as posições desejadas.
def mouseMovFunction(x, y):
    width_base = 1366
    height_base = 768

    width, height = pyautogui.size()

    new_x = int(x * width / width_base)
    new_y = int(y * height / height_base)

    pyautogui.click(new_x, new_y)
    time.sleep(0.1)

#Função que chama a função de movimento, colocando todos os movimentos necessários da máquina.
def mouseMovement(counter):

    first_page = counter == 2

    if first_page:
        nameSelect()
        mouseMovFunction(232, 100)
        mouseMovFunction(742, 415)
        mesage()
        mouseMovFunction(232, 100)
        mouseMovFunction(700, 415)
        pageCounter(counter)
    else:
        nameSelect()
        mouseMovFunction(272, 100)
        mouseMovFunction(742, 415)
        mesage()
        mouseMovFunction(272, 100)
        mouseMovFunction(700, 415)
        print(counter)
        pageCounter(counter)

#criador e gerador de mensagens
def mesages(value):
    global mesageType
    match value:
        case 1:
            mesageType = (f"Agradecemos pela compra, {name}. ❤")
        case 2:
            mesageType = (f'Seu pedido já está à caminho. Agradecemos pelo pedido, {name}.')
    keyboard.write(mesageType)

    print(mesageType)

#gerador de mensagens
def mesage():
    value = random.randint(1, 2)
    mesages(value)
    time.sleep(0.1)