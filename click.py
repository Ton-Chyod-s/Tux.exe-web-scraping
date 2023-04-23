from pynput import mouse
import keyboard
import pyautogui as pt
from time import sleep

# Inicializar uma lista vazia para salvar as coordenadas do mouse
coordenadas = []

def on_click(cx, cy, button, pressed):
    if button == mouse.Button.left and pressed:
        coordenadas.append((cx, cy))
    
# Listener irá verificar quando o mouse clicará
with mouse.Listener(on_click=on_click) as listener:
    while True:
        # Verificar se a tecla Esc foi pressionada para encerrar o programa
        if keyboard.is_pressed('Esc'):
            break
        
while True:
    if len(coordenadas) >= 2:
        # acessar as duas primeiras coordenadas
        c1, c2 = coordenadas[:2]
        
        # pré definindo as duas primeiras coordenadas
        x1, y1 = c1
        x2, y2 = c2
        
        #print(f"Coordenadas 1: ({x1}, {y1})")
        #print(f"Coordenadas 2: ({x2}, {y2})")
        
        #clicar com mouse nas coordenadas pré definidas   
        pt.click(x1,y1)
        sleep(.5)
        pt.click(x2,y2)
        sleep(.3)
        pt.rightClick((x2-25) , (y2-25))
        
        
        
        
        
        # remover as primeiras 4 coordenadas da lista
        coordenadas = coordenadas[1:]
        
    if keyboard.is_pressed('Esc') or not coordenadas:
        break