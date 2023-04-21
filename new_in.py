import pyautogui as pt
from pynput import mouse
import PySimpleGUI as sg
#variavel qe define o tema
selected_theme = 'Reddit'
sg.theme(selected_theme)
quantidade = 2

def on_click(x, y,button,pressed):
    if button == mouse.Button.left and pressed:
        # Retornar False para a execução do listener de eventos
        return False
# Listener irá verificar quando o mouse clicará
with mouse.Listener(on_click=on_click) as listener:
    while True:
        # Assim que o mouse clicar, o listener irá encerrar e parar o loop
        if not listener.running:
            break
     
#definição da posição do mouse              
x , y = pt.position()
z = x - 65
x = y - 65

#inicio da criação do poste
for i in range(1,quantidade):
    sg.popup('Arguardando a confirmação:\nEndereço\nEstação abastecedora',keep_on_top=True, location=(1088, 593))
    
    
    
    
    
    #movimento do mouse para crição do poste
    pt.click(x , y)
    pt.rightClick(z, x)
    pt.move(530, 330)
    print('ta indo')
    