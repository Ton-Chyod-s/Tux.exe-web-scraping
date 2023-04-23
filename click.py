from pynput import mouse
import keyboard

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

# Imprimir todas as coordenadas do mouse após o loop while infinito
for c in coordenadas:
    print(f"Coordenadas do mouse: ({c[0]}, {c[1]})")