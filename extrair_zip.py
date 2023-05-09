import zipfile
import PySimpleGUI as sg
import os
import winshell


def extract_zipfile(zip_file_path, extract_dir):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
 
selected_theme = 'Reddit'
sg.theme(selected_theme)  
layout = [
    [sg.Text(f'Click no botão\n-Não se esqueça de trocar a TR e E-mail\n-Arquivo/Nome de utilizador')],
    [sg.Button('Extrair Tux',size=(13,1))]
 ]

window = sg.Window('lol', icon='favicon.ico',layout=layout, keep_on_top=True, finalize = True)

while True:
    event,values = window.read()
    if event in (None, 'Sair'):
        break 
    if event in 'Extrair Tux':
        
        # Defina o caminho do arquivo ZIP
        zip_file_path = os.path.abspath('Tux-unofficial 3.03.zip')
        #definindo o nome do usuario do pc
        username = 'Public'
        pasta = 'Documents'
        # Defina o caminho da pasta de extração
        extract_dir = os.path.join('C:\\', 'Users', username, pasta, 'Tux-Unofficial')

        # Crie a pasta de extração se ela não existir
        if not os.path.exists(extract_dir):
            os.makedirs(extract_dir)

        # Extrair o arquivo ZIP para a pasta de extração
        extract_zipfile(zip_file_path, extract_dir)
    
        # Defina o caminho do arquivo dentro do diretório do programa
        file_path = os.path.join(extract_dir, 'Tux 3.03.exe')
        
        # Crie um atalho para o arquivo na área de trabalho
        shortcut_file = os.path.join(winshell.desktop(), "Tux 3.03.exe.lnk")

        with winshell.shortcut(shortcut_file) as shortcut:
            shortcut.path = file_path
            shortcut.working_directory = extract_dir
        
        # Caminho da pasta que você deseja criar o atalho
        folder_path = os.path.join('C:\\', 'Users', username, pasta, 'Tux-Unofficial','survey')
        folder_path1 = os.path.join('C:\\', 'Users', username, pasta, 'Tux-Unofficial','kmz')
        folder_path2 = os.path.join('C:\\', 'Users', username, pasta, 'Tux-Unofficial','Arquivos xlsx')
        folder_path3 = os.path.join('C:\\', 'Users', username, pasta, 'Tux-Unofficial','Exemplos.jpg Arquivos')
        
        # Nome do arquivo .lnk que será criado
        shortcut_name = 'Survey.lnk'
        shortcut_name1 = 'kmz.lnk'
        shortcut_name2 = 'Arquivos.lnk'
        shortcut_name3 = 'Exemplos.jpg Arquivos.lnk'
        
        # Caminho completo do arquivo .lnk que será criado
        shortcut_path = os.path.join(winshell.desktop(), shortcut_name)
        shortcut_path1 = os.path.join(winshell.desktop(), shortcut_name1)
        shortcut_path2 = os.path.join(winshell.desktop(), shortcut_name2)
        shortcut_path3 = os.path.join(winshell.desktop(), shortcut_name3)
        
        #criando atalho
        with winshell.shortcut(shortcut_path) as shortcut:
            shortcut.path = folder_path
            shortcut.description = 'Atalho para a pasta'
            shortcut.icon = None  # usa o ícone padrão do sistema
        
        with winshell.shortcut(shortcut_path1) as shortcut:
            shortcut.path = folder_path1
            shortcut.description = 'Atalho para a pasta'
            shortcut.icon = None  # usa o ícone padrão do sistema
        
        with winshell.shortcut(shortcut_path2) as shortcut:
            shortcut.path = folder_path2
            shortcut.description = 'Atalho para a pasta'
            shortcut.icon = None  # usa o ícone padrão do sistema
        
        with winshell.shortcut(shortcut_path3) as shortcut:
            shortcut.path = folder_path3
            shortcut.description = 'Atalho para a pasta'
            shortcut.icon = None  # usa o ícone padrão do sistema
            
        break    
        
window.close()