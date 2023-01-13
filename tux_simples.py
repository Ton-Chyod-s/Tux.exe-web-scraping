from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from selenium.webdriver import Ie
from selenium.webdriver import Edge
import PySimpleGUI as sg
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (frame_to_be_available_and_switch_to_it, element_to_be_clickable)
from selenium.webdriver.support.ui import Select
import json
from selenium.webdriver.common.by import By
import time
import PySimpleGUI as sg
from selenium.webdriver.support import expected_conditions as EC

sg.popup_notify(f'Carregando biblioteca...')

class Internet:
    def __init__(self):
        pass 
    def navegador_driver(self,web_1=True,web_2=True,web_3=True,home=True):
        if web_1:
            self.driver = Edge()
        elif web_2:
            self.driver = Chrome()  
        elif web_3:
            self.driver = Ie()
        else:
            self.driver = Firefox()
          
        self.driver.maximize_window()
        
        if home:
            self.driver.get("http://netwin-vtal.interno/")
            #self.driver.get("http://netwin-vtal.interno/")
        else:
            self.driver.get("http://netwin.intranet/")

        self.driver.implicitly_wait(20)
       
    def entrar_driver(self, login = True):
        wdw = WebDriverWait(self.driver, 60)

        with open("credenciais.json", encoding='utf-8') as meu_json:
            dado = json.load(meu_json)
            
        def entrar(elemento,txt):
            wdw.until(element_to_be_clickable(('id', elemento)))
            self.driver.find_element(By.ID, elemento).clear()
            self.driver.find_element(By.ID, elemento).send_keys(txt)
            return
            
        entrar('inputLogin',dado['login'])
        entrar('inputPassword',dado['senha'])
            
    def esperar_clicar_ID(self,elemento):
        wdw = WebDriverWait(self.driver, 60)
        wdw.until(EC.element_to_be_clickable(('id', elemento)))
        self.driver.find_element(By.ID,elemento).click()

    def esperar_clicar_xpath(self,elemento):
        wdw = WebDriverWait(self.driver, 60)
        wdw.until(EC.element_to_be_clickable((By.XPATH, elemento)))
        self.driver.find_element(By.XPATH,elemento).click()
        
    def esperar_txt_ID(self,elemento, txt):
        wdw = WebDriverWait(self.driver, 60)    
        wdw.until(element_to_be_clickable(('id', elemento)))
        self.driver.find_element(By.ID,elemento).clear()
        self.driver.find_element(By.ID,elemento).send_keys(txt)

    def esperar_link_txt(self,elemento):
        wdw = WebDriverWait(self.driver, 60)
        wdw.until(element_to_be_clickable(('link text', elemento))) 
        self.driver.find_element(By.LINK_TEXT,elemento).click()

    def esperar_selecionar_ID(self,elemento, value):
        wdw = WebDriverWait(self.driver, 60)
        wdw.until((element_to_be_clickable(('id', elemento))))
        selecionar = Select(self.driver.find_element(By.ID,elemento))
        time.sleep(1)
        selecionar.select_by_value(value)

    def esperar_selecionar_value(self,elemento, value):
        wdw = WebDriverWait(self.driver, 60)
        wdw.until((element_to_be_clickable(('id', elemento))))
        selecionar = Select(self.driver.find_element(By.ID,elemento))
        time.sleep(1)
        selecionar.select_by_value(value)

    def esperar_selecionar_value_xpath(self,elemento, value):
        wdw = WebDriverWait(self.driver, 60)
        wdw.until((element_to_be_clickable(('xpath', elemento))))
        selecionar = Select(self.driver.find_element(By.ID,elemento))
        time.sleep(1)
        selecionar.select_by_value(value)
    
    def esperar_selecionar_ID_txt(self,elemento,txt):
        wdw = WebDriverWait(self.driver, 60)
        wdw.until(element_to_be_clickable(('id', elemento)))
        self.driver.find_element(By.ID,elemento).clear()
        self.driver.find_element(By.ID,elemento).send_keys(txt)
        time.sleep(1.5)
        self.driver.find_element(By.ID,elemento).send_keys(Keys.ENTER)
        
    def iframe(self,elemento):
        try:
            wdw = WebDriverWait(self.driver, 60)
            wdw.until(frame_to_be_available_and_switch_to_it((
                'id',elemento)))
        except:
            sg.popup_error('i carai\nnem encontrou oque vc queria, tem que reiniciar o programa',keep_on_top=True)   
            exit()

    def esperar_xpath_txt(self,elemento,txt):
        wdw = WebDriverWait(self.driver, 60)
        wdw.until(element_to_be_clickable(('xpath', elemento)))    
        time.sleep(.15)
        self.driver.find_element(By.XPATH,elemento).send_keys(txt)
    
    def esperar_selecionar_index(self,elemento,num):
        wdw = WebDriverWait(self.driver, 60)
        wdw.until(element_to_be_clickable(('id', elemento)))
        selecionar = Select(self.driver.find_element(By.ID,elemento))
        selecionar.select_by_index(num)

    def esperar_xpath(self,elemento):
        wdw = WebDriverWait(self.driver, 60)
        wdw.until(element_to_be_clickable(('xpath', elemento)))    
        time.sleep(1)
        self.driver.find_element(By.XPATH,elemento).click()

    def poste (self,poste,cap,id_sicom,origem=True,proprietario=True,tr=True,padrao=True,origem_rs=True,tipo=True,id=True):
        try:
            # Esperando até seja visivel as Iframe da pagina
            self.iframe('iframe-content-wrapper')
            self.iframe('externalLocationIframe')
            
            if padrao:
                pass
            else:
                #Fora de padão 
                time.sleep(.05)
                self.esperar_clicar_ID('location_input_FORA_PADRAO')
                #Etiqueta
                time.sleep(.05)
                self.esperar_xpath('//*[@id="location_input_etiquetaEmCampo"]')
                time.sleep(.05)
                if cap == None:
                    self.esperar_xpath_txt('//*[@id="location_input_etiquetaEmCampo"]', poste )
                else:
                    fornecedor =  poste ,  '-'  , cap
                    self.esperar_xpath_txt('//*[@id="location_input_etiquetaEmCampo"]', fornecedor )

                #Capacidade (Altura/Esforço)
                self.esperar_xpath('//span[@id="select2-location_select_poleCapacity-container"]')
                self.esperar_xpath_txt('//input[@class="select2-search__field"]',poste)
                self.esperar_xpath('//li[@class="select2-results__option select2-results__option--highlighted"]')
                    
                if padrao:
                    #Identificação em campo
                    self.esperar_xpath('//span[@id="select2-location_select_fieldId-container"]')
                    self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Existente - Não Validado')
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                else:
                    #Identificação em campo
                    self.esperar_xpath('//span[@id="select2-location_select_fieldId-container"]')
                    self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Existente - Conforme')
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                if tipo:
                    #tipo
                    self.esperar_xpath('//*[@id="select2-location_select_poleType-container"]/span')
                    self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('CONCRETO/DUPLO T')
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                else:
                    #tipo
                    self.esperar_xpath('//*[@id="select2-location_select_poleType-container"]/span')
                    self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('CONCRETO/CIRCULAR')
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                    
                #transformador
                if tr:
                    self.esperar_xpath('//*[@id="select2-location_select_transformer-container"]/span')
                    self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Não')
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                else:
                    self.esperar_xpath('//*[@id="select2-location_select_transformer-container"]/span')
                    self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Sim')
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                    
                    self.esperar_xpath('//*[@id="select2-location_select_landed-container"]')
                    self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Sim')
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                        
                #historico
                self.esperar_xpath('//*[@id="location_tab_logs"]')   
                    
                #Origem
                if origem:
                    self.esperar_xpath('//*[@id="select2-location_select_source-container"]')        
                    self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Arquivo Eletrônico')
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                elif origem_rs:
                    self.esperar_xpath('//*[@id="select2-location_select_source-container"]')        
                    self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Geoplex')
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                    #não possui
                    time.sleep(1)
                    self.esperar_clicar_xpath('//*[@id="location_input_hasNoId"]')
                    time.sleep(2)
                    #disponibilização   
                    self.esperar_xpath('//*[@id="select2-location_select_provision-container"]')        
                    self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Duplicação Manual')
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                else:
                    self.esperar_xpath('//*[@id="select2-location_select_source-container"]')        
                    self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Netwin')
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                    
                #caracteristica
                self.esperar_xpath('//*[@id="location_tab_caracterizacao"]')
                    
                #proprietario
                if proprietario:
                    self.esperar_xpath('//*[@id="select2-location_select_owner-container"]')
                    self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Alugado de terceiros')
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                else:
                    self.esperar_xpath('//*[@id="select2-location_select_owner-container"]')
                    self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Oi')
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                #id-sicom
                if id:
                    pass
                else:
                    self.esperar_xpath('//*[@id="select2-location_select_ID_SICOM-container"]')
                    self.driver.find_element(By.XPATH,'/html/body/span/span/span[*]/input').send_keys(id_sicom)
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                    time.sleep(1.5)

                #localização
                self.esperar_xpath('//*[@id="location_tab_localization"]')
                sg.popup_no_buttons('Confere a localização antes de guardar dmr\nTMJ!',keep_on_top='True')
  
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content()
                
        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ou \nnão é o poste',keep_on_top=True)

    def traçado (self,id_Sicom,traçado=True, origem=True,projeto=True,id_projeto=True):
        wdw = WebDriverWait(self.driver, 30)
        try:
            self.iframe('iframe-content-wrapper')
            wdw.until(element_to_be_clickable(('xpath', '//*[@id="ui-dialog-title-entity-form-div"]')))
            objeto_aereo = self.driver.find_element(By.XPATH,'//*[@id="ui-dialog-title-entity-form-div"]').text
        
            if objeto_aereo == 'Traçado':
                #proprietario
                if traçado:
                    self.esperar_selecionar_ID('ownerId','2') #arquivo eletronico
                else:
                    self.esperar_selecionar_ID('ownerId','1') #oi
                if id_projeto:
                    #id sicon
                    self.esperar_txt_ID('idSicom',id_Sicom)
                    self.esperar_xpath('/html/body/div[*]/div[2]/form/div/div[2]/table[4]/tbody/tr[2]/td[1]/div[2]/div/ul/li')
                else:
                    #nome de projeto
                    self.esperar_txt_ID('project',id_Sicom)
                    self.esperar_xpath('//*[@id="project_div"]/ul/li[1]/a')

                if projeto:
                    self.esperar_selecionar_value('catProjectStateId','191') #implantação concluido
                else:
                    pass

                #origem
                if origem:
                    self.esperar_selecionar_index('sourceId',7) #levantamento de campo
                else:
                    self.esperar_selecionar_index('sourceId',1) #netwin
                
                #guardar
                self.esperar_clicar_xpath('/html/body/div[*]/div[3]/div/button[1]')   
                
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content() 
            
        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ou \nnão é o traçado',keep_on_top=True)

    def atribuir_endereco(self,iframe=True):
        self.driver.implicitly_wait(.05)
        wdw = WebDriverWait(self.driver, 10)
        
        if iframe:
            # Esperando até seja visivel as Iframe da pagina
            self.iframe('iframe-content-wrapper')
            self.iframe('elementSearchFrame')
        else:
            pass   
        
        def sair():
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()
            wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
            time.sleep(0.5)
            #fechar
            self.esperar_xpath('.//span[@class="ui-icon ui-icon-closethick"]')
            wdw.until(frame_to_be_available_and_switch_to_it(('id','elementSearchFrame'))) 
            
        for mancha in range(1,60):
            xpath_linha = f'.//*[@id="results"]/tbody/tr[{mancha}]'
            xpath_mancha = f'.//*[@id="results"]/tbody/tr[{mancha}]/td[12]/i'
            try:
                time.sleep(.1)
                #clicar no botão para atribuir endereço
                self.driver.find_element(By.XPATH,xpath_mancha).click()
                time.sleep(2)
            except:
                print('Não encontrei a linha para atribuir endereço :)')
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content()
                break
            time.sleep(1)
            #espera até o elemento esteja presente na DOM
            if self.driver.find_element(By.XPATH,xpath_linha):
                self.driver.switch_to.default_content()
                #Esperando até seja visivel as Iframe da pagina
                wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                time.sleep(1)
                conectividade = self.driver.find_element(By.XPATH,'//*[@id="ui-dialog-title-externalArea"]').text
                if 'Connectividade' in conectividade:
                    try:
                        wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
                        if 'Área de Influência' in self.driver.find_element(By.ID,'influenceAreaButton').text:
                            #Area de influencia
                            self.esperar_clicar_ID('influenceAreaButton')
                            time.sleep(2)
                            try:
                                xpath_endereco_1 = '//*[@id="notsupplied-sub"]/table/tbody/tr[1]'
                                xpath_endereco_2 = '/td[2]'
                                self.driver.find_element(By.XPATH,xpath_endereco_1+xpath_endereco_2).click()
                                time.sleep(1)
                                print('Foi Atribuido endereço')
                                sair()
                            except:
                                print('Não foi Atribuido endereço')
                                sair()  
                        else:
                            sair()
                    except:
                        sair()
    
versao = '1.0.1 - Unofficial'
navegador = Internet()

class app:
    def __init__(self):
        selected_theme = 'Reddit'
        sg.theme(selected_theme)

        menu_def = ['&Arquivo', ['&Nome de utilizador']],['&Utilitario',['&Poste', '&Atribuir endereço']]
        self.layout_login = [
            [sg.Menu(menu_def,pad=(10,10))],
            [sg.Button('Web',size=(5,1)), sg.Text('INFRA',justification='c',size=(9,1)),sg.Button('Login',size=(6,1))],
            [sg.Combo(['Firefox','Chrome','Internet Explorer','Edge']),sg.Checkbox('V-tal',key='home')],
            ]

        window = sg.Window('Tux-Netwin', icon='compacto.ico',layout=self.layout_login, keep_on_top=True, finalize = True,size=(250,75))

        def poste():
            poste_layout = [
                            [sg.Button('Voltar',size=(5,1)),sg.Text('Poste',justification='c',size=(7,1)),sg.Stretch(),sg.Button('Traçado',size=(11,1))],
                            [sg.Text('ID Sicom',size=(11,1)),sg.Input(size=(11,1),key='id-sicom'),sg.Checkbox('Proj',key='projeto')],
                            [sg.Text('Capa/Forn',size=(11,1)),sg.Input(size=(8,1),key='capacidade'),sg.Input(size=(11,1),key='fornecedor')],
                            [sg.Button('Poste',size=(8,1)),sg.Checkbox('CC',key='cc'),sg.Checkbox('CdT',key='cdt'),sg.Checkbox('CPoste',key='CPoste')]  
            ]
            
            poste = sg.Window('Tux-Netwin', icon='compacto.ico', layout=poste_layout, keep_on_top=True, finalize = True)
            
            while True:
                event,values = poste.read()
                if event in (None, 'Sair'):
                    break 
                    
                if event == 'Voltar':
                    poste.close()
                    programa = app()
                    programa
                        
                if event == 'Poste':
                    if values['CPoste']:
                        if values['cdt']:
                            navegador.poste_inicio()
                            time.sleep(2)
                            navegador.poste(values['capacidade'],values['fornecedor'],values['id-sicom'],False,True,True,False)

                        elif values['cc']:
                            navegador.poste_inicio()
                            time.sleep(2)
                            navegador.poste(values['capacidade'],values['fornecedor'],values['id-sicom'],False,True,True,False,True,False)
                        else:
                            sg.popup('Marque o flag \nCC para Concreto Circular ou \nCdT para Concreto duplo T', keep_on_top=True)
                    else:
                        if values['cdt']:
                            navegador.poste(values['capacidade'],values['fornecedor'],values['id-sicom'],False,True,True,False)

                        elif values['cc']:
                            navegador.poste(values['capacidade'],values['fornecedor'],values['id-sicom'],False,True,True,False,True,False)
                        else:
                            sg.popup('Marque o flag \nCC para Concreto Circular ou \nCdT para Concreto duplo T', keep_on_top=True)

                if event == 'Tipo 2':
                    if values['cdt']:
                        navegador.poste_inicio()
                        time.sleep(1)
                        navegador.poste(values['capacidade'],values['fornecedor'],values['id-sicom'],False,True,True,False,False,False)

                    elif values['cc']:
                        navegador.poste_inicio()
                        time.sleep(1)
                        navegador.poste(values['capacidade'],values['fornecedor'],values['id-sicom'],False,True,True,False,False,False,False)

                    else:
                        sg.popup('Marque o flag \nCC para Concreto Circular ou \nCdT para Concreto duplo T', keep_on_top=True)
                
                if event == 'Traçado':
                    if values['projeto']:
                        navegador.traçado(values['id-sicom'],False,False,True,False)
                    else:
                        navegador.traçado(values['id-sicom'],False,False)

            poste.close()

        def nome_utilizador():
            self.layout_login = [
                [sg.Text('Tux-Netwin',size=(20,1),justification=('c'))],
                [sg.Text('TR:\t'),sg.Input(size=(15,1),key='nome')], 
                [sg.Text('Senha:\t'),sg.Input(size=(15,1),key='senha')],
                [sg.Button('Voltar',size=(6,1)),sg.Button('Ok',size=(6,1))]
                ]

            window = sg.Window('Nome do Utilizador', icon='compacto.ico',layout=self.layout_login, keep_on_top=True, finalize = True)

            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
                    break
                
                if event == 'Voltar':
                    window.close()
                    programa = app()
                    programa 
                
        
                if event == 'Ok':
                    if values['nome'] or values['senha'] == None:
                        dados = {
                            "login": values['nome'],
                            "senha": values['senha'],
                        }
                        with open("credenciais.json", 'w') as file:
                            json.dump(dados, file, indent=4)
                    else:
                        window.close()
                        return app()

                    window.close()
                    programa = app()
                    programa 

                window.close()

        while True:
            event,values = window.read()
            if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
                break
              
            if event == 'Web':
                try:
                    if values['home']:
                        if values[1] == 'Firefox':
                            navegador.navegador_driver(False,False,False)
                        elif values[1] == 'Chrome':
                            navegador.navegador_driver(False,True,False) 
                        elif values[1] == 'Internet Explorer':
                            navegador.navegador_driver(False,False,True)
                        elif values[1] == 'Edge':
                            navegador.navegador_driver(True,False,False)
                        else:
                            sg.popup_error('Selecione um navegador', keep_on_top=True) 
                    else:
                        if values[1] == 'Firefox':
                            navegador.navegador_driver(False,False,False,False)
                        elif values[1] == 'Chrome':
                            navegador.navegador_driver(False,True,False,False) 
                        elif values[1] == 'Internet Explorer':
                            navegador.navegador_driver(False,False,True,False)
                        elif values[1] == 'Edge':
                            navegador.navegador_driver(True,False,False,False)  
                        else:
                            sg.popup_error('Selecione um navegador', keep_on_top=True) 
                except:
                    sg.popup('Tente Novamente', keep_on_top=True)

            if event == 'Poste':
                window.close()
                poste()

            if event == 'Nome de utilizador':
                window.close()
                nome_utilizador()
            
            if event == 'Login':
                navegador.entrar_driver()

            if event == 'Atribuir endereço':
                try:
                    navegador.atribuir_endereco()
                except:
                    sg.popup('Nem ta na pagina certa', keep_on_top=True)

        window.close()

if __name__ == '__main__':
    app()