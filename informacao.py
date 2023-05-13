from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
import PySimpleGUI as sg
import socket
import requests
import json
import zipfile
import sys
import time

versao = '3.03'

if zipfile.is_zipfile(sys.executable):
    sg.popup('Não é possível executar o arquivo dentro do zip',keep_on_top=True)
    sys.exit()
else:
    ip_local = socket.gethostbyname(socket.gethostname())
    ip_publico = requests.get('https://api.ipify.org/').text
    
    url = f"https://ipapi.co/{ip_publico}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city = data.get("city")
        
    else:
        city = f'não foi possivel localizar cidade do ip:{ip_publico}'
        
    sg.popup_notify('Aguarde, validando informações ...')
    
    # tenta abrir o arquivo de credenciais e extrair as informações de login
    try:
        with open("credenciais.json", encoding='utf-8') as meu_json:
                    dado = json.load(meu_json)
        from selenium.webdriver.firefox.options import Options 
        info = dado['email']   
        tr = dado['login']
        senha = dado['senha']
    
    # se houver algum erro, exibe o formulário de login    
    except Exception as e:
        layout_login = [
            [sg.Text('Netwin - {versao}',size=(20,1),justification=('c'))],
            [sg.Text('TR:*\t'),sg.Input(size=(15,1),key='nome')], 
            [sg.Text('Senha:*\t'),sg.Input(size=(15,1),key='senha')],
            [sg.Text('Email Institucional',size=(20,1),justification=('c'))],
            [sg.Text('E-mail*:\t'),sg.Input(size=(15,1),key='email')],
            [sg.Text('Senha*:\t'),sg.Input(size=(15,1),key='senha_email')],
            [sg.Button('Ok',size=(6,1))]
            ]

        window = sg.Window(f'Netwin - {versao}', icon='favicon.ico',layout=layout_login, keep_on_top=True, finalize = True)

        while True:
            event,values = window.read()
            if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
                sys.exit()
            
            if event == 'Ok':
                if values['nome'] and values['email']:
                    dados = {
                        "login": values['nome'],
                        "senha": values['senha'],
                        "email": values['email'],
                        "senha_email": values['senha_email']
                    }
                    with open("credenciais.json", 'w') as file:
                        json.dump(dados, file, indent=4)
                        
                    tr = values['nome']
                    senha = values['senha']
                    info = values['email']
                    break
                else:
                    sg.popup_error('Preenche corretamente Tr e Email\nExemplo:\ntr125864\nblablabla@telemont.com.br', keep_on_top=True)
                    
            window.close()
            
    try:
        # abre o navegador firefox em segundo plano
        options = Options()
        options.add_argument('-headless')
        driver = Firefox(options=options)
        driver.implicitly_wait(.5)
        wdw = WebDriverWait(driver, 30)

        # entra na url
        url = "https://github.com/Ton-Chyod-s/Projetos/blob/main/tux%20mind"
        driver.get(url)
        time.sleep(1)

        # varre o site e atribui valores as variaveis  
        on = driver.find_element(By.XPATH, '//*[@id="LC1"]').text
        frase = driver.find_element(By.XPATH, '//*[@id="LC2"]').text

        # entra no site de formulario para preencher
        formulario = 'https://forms.gle/gQzJ6Th817BGSZyY9'
        driver.get(formulario)

        # preenche o formulário
        def preenche_formulario(driver, xpath, value):
            wdw.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            input_element = driver.find_element(By.XPATH, xpath)
            input_element.clear()
            input_element.send_keys(value)

        preenche_formulario(driver, '/html/body/div/div[2]/form/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/textarea', info)
        preenche_formulario(driver, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea', tr)
        preenche_formulario(driver, '/html/body/div/div[*]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea', ip_local)
        preenche_formulario(driver, '/html/body/div/div[*]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea', ip_publico)
        preenche_formulario(driver, '/html/body/div/div[*]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea', versao)
        preenche_formulario(driver, '/html/body/div/div[*]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input', city)

        # clica em enviar
        wdw.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
        input_element = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        input_element.click()
        

    except Exception as e:
        print(e)

    finally:
        driver.quit()