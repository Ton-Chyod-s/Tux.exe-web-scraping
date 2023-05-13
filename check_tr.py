from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import PySimpleGUI as sg

def check_tr():
    options = Options()
    options.add_argument('-headless')
    driver = Firefox(options=options)
    driver.implicitly_wait(.1)
    selected_theme = 'Reddit'
    sg.theme(selected_theme)
    layout = [
        [sg.Text('Credenciais:', size=(9,1)), sg.Input(size=(8,1), key='tr'), sg.Button('Ok')],
    ]
        
    window = sg.Window('num_prog', icon='favicon.ico', layout=layout, keep_on_top=True, finalize=True, no_titlebar=True, grab_anywhere=True)
    try:
        while True:
            
            event, values = window.read()
            if event in (None, 'Sair'):
                break
            
            if event == 'Ok':                
                url = "https://github.com/Ton-Chyod-s/Projetos/blob/main/verification%20tr's"

                driver.get(url)
                for i in range(1, 31):   
                    xpath = f'//*[@id="LC{i}"]'
                    try:
                        tr_link = driver.find_element(By.XPATH, xpath).text
                        if tr_link.lower() == values['tr'].lower():
                            sg.Popup(f'TR {values["tr"]} encontrada!', title='Resultado',keep_on_top=True)
                            window.close()
                            break
                    except Exception as e:
                        sg.Popup(f'TR {values["tr"]} não encontrada,\nTente novamente!', title='Resultado',keep_on_top=True, no_titlebar=True)
                        break
                else:
                    sg.Popup(f'TR {values["tr"]} não encontrada,\nTente novamente!', title='Resultado',keep_on_top=True, no_titlebar=True)
                    
    finally:
        print('Iniciado programa, Aguarde...')
        driver.quit()