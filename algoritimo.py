from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from selenium.webdriver import Ie
from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (frame_to_be_available_and_switch_to_it, element_to_be_clickable)
from selenium.webdriver.support.ui import Select
import json
from selenium.webdriver.common.by import By
import pyautogui as pt
import time
import PySimpleGUI as sg
from pynput import mouse
from random import randint
import os
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC

sg.popup_notify(f'Carregando biblioteca...')

#sg.popup_timed(f'C:\Users\klayton.dias\Desktop\Tux.exe\photo_2022-12-08_15-49-17')

esperar = time.sleep(.05)
esperar1 = time.sleep(1)
esperar2 = time.sleep(2)
esperar3 = time.sleep(.01)
esperar4 = time.sleep(3)
esperar5 = time.sleep(3.5)


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
        esperar
        selecionar.select_by_value(value)

    def esperar_selecionar_value(self,elemento, value):
        wdw = WebDriverWait(self.driver, 60)
        wdw.until((element_to_be_clickable(('id', elemento))))
        selecionar = Select(self.driver.find_element(By.ID,elemento))
        esperar
        selecionar.select_by_value(value)

    def esperar_selecionar_value_xpath(self,elemento, value):
        wdw = WebDriverWait(self.driver, 60)
        wdw.until((element_to_be_clickable(('xpath', elemento))))
        selecionar = Select(self.driver.find_element(By.ID,elemento))
        esperar
        selecionar.select_by_value(value)
    
    def esperar_selecionar_ID_txt(self,elemento,txt):
        wdw = WebDriverWait(self.driver, 60)
        wdw.until(element_to_be_clickable(('id', elemento)))
        self.driver.find_element(By.ID,elemento).clear()
        self.driver.find_element(By.ID,elemento).send_keys(txt)
        esperar2
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
        esperar
        self.driver.find_element(By.XPATH,elemento).click()

    def procurar_estação(self,elemento,procurar=True):
        if procurar:
            self.esperar_xpath('//a[@data-module="Outside Plant"]')
            self.iframe('iframe-content-wrapper')
            self.iframe('ifrarvore')
            self.iframe('ifArvore')
            self.esperar_clicar_ID('sigrede_1_0_2_2_txt')
            self.driver.switch_to.default_content()

            self.iframe('iframe-content-wrapper')
            self.iframe('ifrarvore')
            self.iframe('ifPesquisa')
            
            self.esperar_selecionar_ID_txt('searchName',elemento)
            esperar
            self.driver.switch_to.default_content()
        else:    
            self.iframe('iframe-content-wrapper')
            self.iframe('ifrarvore')
            self.iframe('ifPesquisa')
            esperar
            self.esperar_selecionar_ID_txt('searchName',elemento)
            esperar
            self.driver.switch_to.default_content()


        esperar

        #menu_op_ico

        self.driver.find_element(By.CSS_SELECTOR, ".odd > #tdresultado").click()
        self.driver.switch_to.frame(1)
        element = self.driver.find_element(By.CSS_SELECTOR, "#sigrede_1_0_2_4 > .menu_op_txt")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, "#sigrede_1_0_2_13_3_1845911_4_1853370_191_793569_ico > img").click()
        self.driver.find_element(By.ID, "nodefault_1").click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".olControlCellButtonItemInactive").click()
        self.driver.find_element(By.ID, "olControlGPONCell").click()
        self.driver.find_element(By.ID, "olControlViewCell").click()
        self.driver.find_element(By.ID, "searchLocation").click()
        dropdown = self.driver.find_element(By.ID, "searchLocation")
        dropdown.find_element(By.XPATH, "//option[. = 'CPBA - BANDEIRANTES']").click()
        self.driver.find_element(By.ID, "searchCellD").click()
        dropdown = self.driver.find_element(By.ID, "searchCellD")
        dropdown.find_element(By.XPATH, "//option[. = '480']").click()
        
        self.driver.switch_to.default_content()

    def cdoe_precon(self,id_sicon,estação,est=True,confirmar=True,frame=True,sap=True,sap_1=True,campo=True,tbd=True,projeto=True):
        
        #Esperando até seja visivel as Iframe da pagina
        if frame:
            self.iframe('iframe-content-wrapper')
        else:
            pass
        try:
            self.iframe('externalIspIframe')
            self.iframe('dados')
            wdw = WebDriverWait(self.driver, 60)
            wdw.until(element_to_be_clickable(('xpath', '//*[@id="idTipoElemento"]')))
            objeto_aereo = self.driver.find_element(By.XPATH,'//*[@id="idTipoElemento"]').text

            if objeto_aereo == 'CDOE':
                self.esperar_clicar_ID('id_sicom_name')
                #Tipo
                if confirmar:
                    self.esperar_selecionar_ID('elem_tipo.outroNomeEquip','CAIXA DIST OPT SEL 9 SC EXT SLIM 1:8')
                elif sap:
                    self.esperar_selecionar_ID('elem_num_sap','331995') #1:8 final
                elif sap_1:
                    self.esperar_selecionar_ID('elem_num_sap','331688') #1:8 intermediaria
                else:
                    self.esperar_selecionar_ID('elem_tipo.outroNomeEquip','CAIXA DIST OPT SEL 10 SC EXT SLIM 30/70')

                #Rede
                self.esperar_selecionar_ID('network','Óptica GPON')
                if projeto:
                    #Id-sicon
                    self.esperar_txt_ID('id_sicom_name',id_sicon)
                    self.esperar_xpath('//li[@class="ac_even ac_over"]')
                else:
                    #Nome projeto
                    self.esperar_txt_ID('projecto_name',id_sicon)
                    self.esperar_xpath('/html/body/div[*]/ul/li/strong')
                if campo:
                    #Identif. campo
                    self.esperar_selecionar_ID('nameCampId','Existente - Não Validado')
                else:
                    #Identif. campo
                    self.esperar_selecionar_ID('nameCampId','Existente - Conforme')
                #Estação abastecedora 1
                if est:
                    #identiicar local para escrita/escrever , confirmar
                    self.esperar_selecionar_ID_txt('supplierStationName',estação)
                    self.esperar_xpath('//li[@class="ac_even ac_over"]')
                else:
                    pass 
                #Topologia
                self.esperar_selecionar_ID('topology','A/B')
                time.sleep(.05)
                
                #Estações Abastecedoras 2
                self.driver.find_element(By.LINK_TEXT,'Estações abastecedoras').click()
                self.esperar_txt_ID('autocompleteSLocation',estação)
                self.esperar_xpath('//li[@class="ac_even ac_over"]')
                self.esperar_clicar_ID('adicionar')
                #Rastreabilidade
                self.driver.find_element(By.LINK_TEXT,'Rastreabilidade').click()
                self.esperar_selecionar_ID('sourceId','Netwin')
                #caracteristica
                self.esperar_clicar_xpath('/html/body/table/tbody/tr/td/div/div/div/form/div/table/tbody/tr[*]/td/div/ul/li[1]/a/span')

                if tbd:
                    pass
                else:
                    #tbd
                    self.esperar_clicar_xpath('//*[@id="outOfPattern_check"]') #fora de padrão
                    time.sleep(1)
                    self.esperar_xpath('//*[@id="onPatternTag"]')
                    '''
                    time.sleep(1)
                    etiqueta_padrao = self.driver.find_element(By.XPATH,'//*[@id="onPatternTag"]').text()
                    '''
                    time.sleep(1)
                    self.esperar_xpath_txt('//*[@id="tagOnField"]','CDOE-'+'000'+'-TBD')

                #Confimar
                self.esperar_clicar_ID('confAssoc')
                #Sair
                self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content()

        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ou \nnão é a CDOE',keep_on_top=True)

    def cdoe_precon_2022(self,id_sicon,estação,est=True,confirmar=True,frame=True,precom_rs=True,tbd=True,projeto=True):
        #Esperando até seja visivel as Iframe da pagina
        if frame:
            self.iframe('iframe-content-wrapper')
        else:
            pass
        try:
            self.iframe('externalIspIframe')
            self.iframe('dados')
            wdw = WebDriverWait(self.driver, 60)
            wdw.until(element_to_be_clickable(('xpath', '//*[@id="idTipoElemento"]')))
            objeto_aereo = self.driver.find_element(By.XPATH,'//*[@id="idTipoElemento"]').text
            
            if objeto_aereo == 'CDOE':
                self.esperar_clicar_ID('id_sicom_name')
                #Tipo
                if confirmar:
                    self.esperar_selecionar_ID('elem_tipo.outroNomeEquip','CAIXA DISTR OPT SEL 18 SC EXT TAP 30/70') 
                else:
                    self.esperar_selecionar_ID('elem_tipo.outroNomeEquip','CAIXA DISTR OPT SEL 17 SC EXT TAP 1:16')
                #Rede
                self.esperar_selecionar_ID('network','Óptica GPON')
                if projeto:
                    #Id-sicon
                    self.esperar_txt_ID('id_sicom_name',id_sicon)
                    self.esperar_xpath('//li[@class="ac_even ac_over"]')
                else:
                    #Nome projeto
                    self.esperar_txt_ID('projecto_name',id_sicon)
                    self.esperar_xpath('/html/body/div[*]/ul/li/strong')
                if precom_rs:
                    #Identif. campo
                    self.esperar_selecionar_ID('nameCampId','Desconhecido')
                else:
                    #Identif. campo
                    self.esperar_selecionar_ID('nameCampId','Existente - Conforme')
                #Estação abastecedora 1
                if est:
                    #identiicar local para escrita/escrever , confirmar
                    self.esperar_selecionar_ID_txt('supplierStationName',estação)
                    esperar
                    self.esperar_xpath('//li[@class="ac_even ac_over"]')
                else:
                    #identiicar local para escrita/escrever , confirmar
                    self.esperar_selecionar_ID_txt('supplierStationName',estação)
                    esperar
                    self.esperar_xpath('//li[@class="ac_odd"]') 
                #Topologia
                self.esperar_selecionar_ID('topology','A/B')
                #Estações Abastecedoras 2
                if est:
                    self.esperar_link_txt('Estações abastecedoras')
                    self.esperar_txt_ID('autocompleteSLocation',estação)
                    self.esperar_xpath('//li[@class="ac_even ac_over"]')
                    self.esperar_clicar_ID('adicionar')
                else:
                    self.esperar_link_txt('Estações abastecedoras')
                    self.esperar_txt_ID('autocompleteSLocation',estação)
                    esperar1
                    self.esperar_xpath('//li[@class="ac_odd ac_over"]')
                    self.esperar_clicar_ID('adicionar')
                #Rastreabilidade
                self.esperar_link_txt('Rastreabilidade')
                self.esperar_selecionar_ID('sourceId','Netwin')
                #caracteristica
                self.esperar_clicar_xpath('/html/body/table/tbody/tr/td/div/div/div/form/div/table/tbody/tr[*]/td/div/ul/li[1]/a/span')
                
                if tbd:
                    pass
                else:
                    #tbd
                    self.esperar_clicar_xpath('//*[@id="outOfPattern_check"]') #fora de padrão
                    time.sleep(1)
                    self.esperar_xpath('//*[@id="onPatternTag"]')
                    '''
                    time.sleep(1)
                    etiqueta_padrao = self.driver.find_element(By.XPATH,'//*[@id="onPatternTag"]').text()
                    '''
                    time.sleep(1)
                    self.esperar_xpath_txt('//*[@id="tagOnField"]','CDOE-'+'000'+'-TBD')

                #Confimar
                self.esperar_clicar_ID('confAssoc')
                #Sair
                self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content()
        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ou \nnão é a CDOE',keep_on_top=True)

    def cdoe_comun(self, id_sicon, estação, numero=randint, confimar = False, confirmar_quebra = True):
        wdw = WebDriverWait(self.driver, 30)
        if confirmar_quebra:
                self.iframe('iframe-content-wrapper')
                #adicionar
                self.esperar_xpath('//div[@class="olControlIndoorMapAddButtonItemInactive"]')
                #equipamento
                self.esperar_clicar_ID('olControlAddEquipment')
                #fibra optica
                self.esperar_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div/div/fieldset/ul/li[1]/a/div[2]')
                #CDO
                self.esperar_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div/div/fieldset/ul/li[1]/ul/li[1]/a/div[2]')
                #CDOE
                self.esperar_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div/div/fieldset/ul/li[1]/ul/li[1]/ul/li[1]/a/div[2]')
                #clicar para criação do equipamento
                pt.click(x=1662, y=758) #esquerdo
                pt.rightClick(x=1725, y=736) #direito
                time.sleep(1)
                
        else:
            if confirmar_quebra:
                pass
            else:
                self.iframe('iframe-content-wrapper')
            time.sleep(1)
            self.iframe('externalIspIframe')
            self.iframe('dados')
            #esperar um tempo para carregar iframe
            self.esperar_clicar_ID('id_sicom_name')
                
            #Tipo
            if confimar:
                self.esperar_selecionar_ID('elem_tipo.outroNomeEquip','CDOE 8-48FS C/ SPL 1:8 OPTITAP COR/TOP/FACH') 
            else:
                self.esperar_selecionar_ID('elem_tipo.outroNomeEquip','CDOE 16-48FS C/ SPL 2 x 1:8 OPTITAP COR/TOP/FACH')     
            #Rede
            self.esperar_selecionar_ID('network','Óptica GPON')
            #Fabricante
            self.esperar_selecionar_ID('idFabricante','CORNING')
            #Id-sicon
            self.esperar_txt_ID('id_sicom_name',id_sicon)
            self.esperar_xpath('//li[@class="ac_even ac_over"]')
                
                
            #Estação abastecedora/predial
            #navegador.esperar_clicar('suppStationFilterButton')
            #navegador.esperar_selecionar_txt('estacao', estação)
            #navegador.esperar_clicar('imgListaRelEquipamento')
                
            self.esperar_txt_ID('supplierStationName', estação)
            self.esperar_xpath('//li[@class="ac_even ac_over"]')
                
            #Topologia
            self.esperar_selecionar_ID('topology','A/B')
            #Identif. campo
            self.esperar_selecionar_ID('nameCampId','Existente - Não Validado')
            #numero
            self.esperar_txt_ID('nomecNumber',numero)
            time.sleep(.15)
            #Estações Abastecedoras
            self.esperar_link_txt('Estações abastecedoras')
            self.esperar_txt_ID('autocompleteSLocation', estação)
            self.esperar_xpath('//li[@class="ac_even ac_over"]')
            self.esperar_clicar_ID('adicionar')
            #Rastreabilidade
            self.esperar_link_txt('Rastreabilidade')
            self.esperar_selecionar_ID('sourceId','Netwin')
            #Confimar
            self.esperar_clicar_ID('confAssoc')
            #Sair
            self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
            time.sleep(1)
                
            #Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()

#revisar
    def criar_equipamento(self,lado=True):

        self.iframe('iframe-content-wrapper')
        #adicionar
        self.esperar_xpath('//div[@class="olControlIndoorMapAddButtonItemInactive"]') 
        #equipamento
        self.esperar_clicar_ID('olControlAddEquipment')
        #fibra optica
        self.esperar_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div/div/fieldset/ul/li[1]/a/div[2]') # //a[@catsubtypeid="undefined"]
        #CDO
        self.esperar_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div/div/fieldset/ul/li[1]/ul/li[1]/a/div[2]') # //a[@catsubtypeid="515"]
        #CDOE
        self.esperar_xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div/div/fieldset/ul/li[1]/ul/li[1]/ul/li[1]/a/div[2]') # //a[@catsubtypeid="518"]
    
        #dentro do poste
        self.esperar_xpath('//*[@id="OpenLayers.Layer.Vector_204_svgRoot"]')
        
        
        
        
        '''    
        if lado:
            #clicar para criação do equipamento
            pt.click(x=1662, y=758) #esquerdo
            pt.rightClick(x=1725, y=736) #direito
            time.sleep(1)
            self.driver.switch_to.default_content()
        else:
            #clicar para criação do equipamento
            pt.click(x=1780, y=767) #esquerdo
            pt.rightClick(x=1725, y=736) #direito
            time.sleep(1)
            self.driver.switch_to.default_content()
        '''
                      
    def componentes(self,modelo=True):
            self.iframe('iframe-content-wrapper')
            self.iframe('externalFrame')
            self.iframe('dados')
            #componetes
            self.esperar_xpath('/html/body/table/tbody/tr/td/div/div/div/form/div/table/tbody/tr[*]/td/div/ul/li[4]/a/span')
            #+
            self.esperar_clicar_ID('addNoPosComp')
            time.sleep(1)
            self.iframe('targetIframe')

            if modelo:
                #modelo
                self.esperar_selecionar_value('idTipoElemento','20748') #1:8
                time.sleep(.1)
                #legado
                self.esperar_selecionar_value('LEGADO','NÃO')
                time.sleep(.1)
                #confirmar
                esperar1
                self.esperar_clicar_ID('confAssoc')
                esperar1
                #fechar
                self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
                self.driver.switch_to.default_content()
            else:
                #modelo
                self.esperar_selecionar_value('idTipoElemento','20726') #1:8
                time.sleep(.1)
                #legado
                self.esperar_selecionar_value('LEGADO','NÃO')
                time.sleep(.1)
                #confirmar
                esperar1
                self.esperar_clicar_ID('confAssoc')
                esperar1
                #fechar
                self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
                time.sleep(1)
                
                self.driver.switch_to.default_content()
                self.iframe('iframe-content-wrapper')
                self.iframe('externalFrame')
                self.iframe('dados')
                
                #+
                self.esperar_clicar_ID('addNoPosComp')
                self.iframe('targetIframe')
                #modelo
                self.esperar_selecionar_value('idTipoElemento','20725') #1:2
                time.sleep(.1)
                #legado
                self.esperar_selecionar_value('LEGADO','NÃO')
                time.sleep(.1)
                #confirmar
                esperar1
                self.esperar_clicar_ID('confAssoc')
                esperar1
                #fechar
                self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
                self.driver.switch_to.default_content()
            
            self.iframe('iframe-content-wrapper')
            self.esperar_xpath('/html/body/div[*]/div[*]/a[1]/span')
            self.driver.switch_to.default_content()

    def componentes_2022(self,modelo=True):
            self.iframe('iframe-content-wrapper')
            self.iframe('externalFrame')
            self.iframe('dados')
            #componetes
            self.esperar_xpath('/html/body/table/tbody/tr/td/div/div/div/form/div/table/tbody/tr[*]/td/div/ul/li[4]/a/span')
            #+
            self.esperar_clicar_ID('addNoPosComp')
            time.sleep(1)
            self.iframe('targetIframe')

            if modelo:
                #modelo
                self.esperar_selecionar_value('idTipoElemento','20723') #1:16
                time.sleep(1.5)
                #legado
                self.esperar_selecionar_value('LEGADO','NÃO')
                time.sleep(1.5)
                #confirmar
                time.sleep(1.5)
                self.esperar_clicar_ID('confAssoc')
                esperar1
                #fechar
                self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
                self.driver.switch_to.default_content()
            else:
                #modelo
                self.esperar_selecionar_value('idTipoElemento','20752') #1:16
                time.sleep(1.5)
                #legado
                self.esperar_selecionar_value('LEGADO','NÃO')
                time.sleep(1.5)
                #confirmar
                esperar1
                self.esperar_clicar_ID('confAssoc')
                esperar1
                #fechar
                self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
                time.sleep(1)
                
                self.driver.switch_to.default_content()
                self.iframe('iframe-content-wrapper')
                self.iframe('externalFrame')
                self.iframe('dados')
                
                #+
                self.esperar_clicar_ID('addNoPosComp')
                self.iframe('targetIframe')
                #modelo
                self.esperar_selecionar_value('idTipoElemento','20727') #1:2
                time.sleep(1.5)
                #legado
                self.esperar_selecionar_value('LEGADO','NÃO')
                time.sleep(1.5)
                #confirmar
                esperar1
                self.esperar_clicar_ID('confAssoc')
                esperar1
                #fechar
                self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
                self.driver.switch_to.default_content()
            
            self.iframe('iframe-content-wrapper')
            self.esperar_xpath('/html/body/div[*]/div[*]/a[1]/span')
            self.driver.switch_to.default_content()

    def conectividade(self,spliter=True,mod=True):
        wdw = WebDriverWait(self.driver, 60)
        self.iframe('iframe-content-wrapper')
        self.iframe('externalFrame')
        try:
            if spliter:
                #cenario
                self.esperar_selecionar_value('cbScenario','difusion') #Fibra óptica 1:1 Splitter n:n Fibra óptica
                wdw.until(element_to_be_clickable(('id', 'splitter_ratio_inout_2main')))
                self.esperar_clicar_ID('splitter_ratio_inout_2main')
                #cabo
                self.esperar_selecionar_index('cable_inout_1main',1)
                #fibra
                self.esperar_selecionar_value('fiber_inout_1main','1')

                if mod:
                    #spliter
                    self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1/2
                else:
                    self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1/2

                #porta de entrada
                self.esperar_selecionar_index('splitter_port_in_2main',1)
                #porta saida inicial
                self.esperar_selecionar_index('splitter_port_out_2main',1)
                #cabo
                self. esperar_selecionar_index('cable_inout_3main',1)
                #Fibra Inicial
                self.esperar_selecionar_index('fiber_inout_3main',1)
                #ligar
                self.esperar_clicar_ID('connectButton')
                #confirmar
                self.esperar_clicar_ID('attributesConfirmButton')
                time.sleep(1)
                #OK
                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content()
                
            else:
                self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                time.sleep(2)
                
                #cabo
                self.esperar_selecionar_index('cable_inout_1main',1)
                #fibra
                self.esperar_selecionar_value('fiber_inout_1main','1')
                if mod:
                    #spliter
                    self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1/2
                else:
                    self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1/2
                #porta de entrada
                self.esperar_selecionar_index('splitter_port_in_2main',1)
                #porta saida 
                self.esperar_selecionar_index('splitter_port_out_2main',2)
                if mod:
                    #spliter
                    self.esperar_selecionar_index('splitter_ratio_inout_3main',2)  #1:8
                else:
                    self.esperar_selecionar_index('splitter_ratio_inout_3main',1)  #1:8
                #porta entrada
                self.esperar_selecionar_index('splitter_port_in_3main',1)
                #porta saida inicial
                self.esperar_selecionar_index('splitter_port_out_3main',1)
                #porta saida final
                self.esperar_selecionar_index('splitter_port_out_3main_final',8)
                #porta inicial
                self.esperar_selecionar_index('pdoport_inout_4main',1)
                #porta final
                self.esperar_selecionar_index('pdoport_inout_4main_final',8)
                #ligar
                self.esperar_clicar_ID('connectButton')
                #tipo ligador
                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                #tipo ligador
                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                time.sleep(1)
                #confirmar
                self.esperar_clicar_ID('attributesConfirmButton')
                #x
                #self.esperar_xpath('//*[@id="closeButton"]')
                
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content() 
            
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()
        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ou \nnão é a CONECTIVIDADE 1:8',keep_on_top=True)

    def conectividade_2022(self,spliter=True,ratio=True,iframe=True):
        if iframe:
            wdw = WebDriverWait(self.driver, 60)
            self.iframe('iframe-content-wrapper')
            self.iframe('externalFrame')
        else:
            pass
        try:
            if spliter:
                #cenario
                self.esperar_selecionar_value('cbScenario','difusion') #Fibra óptica 1:1 Splitter n:n Fibra óptica
                wdw.until(element_to_be_clickable(('id', 'splitter_ratio_inout_2main')))
                self.esperar_clicar_ID('splitter_ratio_inout_2main')
                #cabo
                self.esperar_selecionar_index('cable_inout_1main',1)
                #fibra
                self.esperar_selecionar_value('fiber_inout_1main','1')
                if ratio:
                    #spliter
                    self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:16
                else:
                    #spliter
                    self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1:16
                #porta de entrada
                self.esperar_selecionar_index('splitter_port_in_2main',1)
                #porta saida inicial
                self.esperar_selecionar_index('splitter_port_out_2main',1)
                #cabo
                self. esperar_selecionar_index('cable_inout_3main',1)
                #Fibra Inicial
                self.esperar_selecionar_index('fiber_inout_3main',1)
                #ligar
                self.esperar_clicar_ID('connectButton')
                #confirmar
                self.esperar_clicar_ID('attributesConfirmButton')
                #OK
                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content()
                
            else:
                self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                time.sleep(2)
                
                #cabo
                self.esperar_selecionar_index('cable_inout_1main',1)
                #fibra
                self.esperar_selecionar_value('fiber_inout_1main','1')
                if ratio:
                    #spliter
                    self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:2
                else:
                    #spliter
                    self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1:2
                #porta de entrada
                self.esperar_selecionar_index('splitter_port_in_2main',1)
                #porta saida 
                self.esperar_selecionar_index('splitter_port_out_2main',2)
                if ratio:
                    #spliter
                    self.esperar_selecionar_index('splitter_ratio_inout_3main',1)  #1:16
                else:
                    #spliter
                    self.esperar_selecionar_index('splitter_ratio_inout_3main',2)  #1:16
                #porta entrada
                self.esperar_selecionar_index('splitter_port_in_3main',1)
                #porta saida inicial
                self.esperar_selecionar_index('splitter_port_out_3main',1)
                #porta saida final
                self.esperar_selecionar_index('splitter_port_out_3main_final',16)
                #porta inicial
                self.esperar_selecionar_index('pdoport_inout_4main',1)
                #porta final
                self.esperar_selecionar_index('pdoport_inout_4main_final',16)
                #ligar
                self.esperar_clicar_ID('connectButton')
                #tipo ligador
                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                #tipo ligador
                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                #confirmar
                self.esperar_clicar_ID('attributesConfirmButton')
                #x
                #self.esperar_xpath('//*[@class="ui-icon ui-icon-closethick"]')
                
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content() 
            
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()

        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ou \nnão é a CONECTIVIDADE 1:16',keep_on_top=True)

    def mudar_status_cabo_completo(self):
        wdw = WebDriverWait(self.driver, 60)
        self.iframe('iframe-content-wrapper')
        #modificar
        self.esperar_xpath('/html/body/div[*]/div[2]/div[2]/div[15]')
        #script para controlar a ação do mouse em seguida de repetição da ação *clique/local
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
        x, y = pt.position()

        time.sleep(2.2)

        #implantação concluida
        self.esperar_selecionar_ID('catProjectStateId','191')
        time.sleep(.5)
        #guardar    
        self.esperar_xpath('/html/body/div[*]/div[3]/div/button[1]')

        # Retorna para a janela principal (fora do iframe)
        self.driver.switch_to.default_content()

        time.sleep(1.7)

        print(pt.click(x, y))
        #entrar no iframe
        self.iframe('iframe-content-wrapper')
        time.sleep(1.5)
        #as-built
        self.esperar_clicar_ID('lot')
        esperar1
        self.esperar_clicar_ID('asBuilt')
        #estado de projeto
        self.esperar_selecionar_value('catProjectStateId','194')
        esperar1
        #guardar    
        self.esperar_xpath('/html/body/div[*]/div[3]/div/button[1]')

        # Retorna para a janela principal (fora do iframe)
        self.driver.switch_to.default_content()
        
    def sob_demanda(self):
        self.iframe('iframe-content-wrapper')
        
        #sob demanda
        self.esperar_selecionar_value('catProjectStateId','190')
        #instalação futura
        self.esperar_clicar_ID('futureInstall')
        time.sleep(.5)
        #guardar
        self.esperar_xpath('/html/body/div[*]/div[3]/div/button[1]')
            
        # Retorna para a janela principal (fora do iframe)
        self.driver.switch_to.default_content()
      
    def encontrar(self,elemento):
        wdw = WebDriverWait(self.driver, 60)
        self.iframe('iframe-content-wrapper')
        #entidade
        self.esperar_selecionar_value('rede','EQUIPMENT')
        #tipo
        self.esperar_selecionar_value('tipo','515')
        #Nome
        self.esperar_txt_ID('codigo',elemento)
        #resultado
        time.sleep(5)
        wdw.until(element_to_be_clickable(('xpath', '//*[@aria-describedby="pesquisaGrid_code"]')))
        time.sleep(1)
        pt.click(x=233, y=476)
    
       
        # Retorna para a janela principal (fora do iframe)
        self.driver.switch_to.default_content()

    def endereco(procurar = True):
        if procurar:
            sg.theme('Reddit')
            local = sg.popup_get_folder(r'Selecione o caminho dos Arquivos')
            caminho = os.chdir(local)
        else:
            pass
        
        return caminho

    def poste (self,poste,cap,id_sicom,origem=True,proprietario=True,tr=True,padrao=True,origem_rs=True,tipo=True,id=True):
        wdw = WebDriverWait(self.driver, 60)
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
                '''
                #Número
                self.esperar_xpath('//*[@class="select2-selection__placeholder"]')
                self.driver.find_element(By.XPATH,'//*[@id="location_input_numero"]').clear()
                self.driver.find_element(By.XPATH,'//*[@id="location_input_numero"]').send_keys(randint(1,999999))
                time.sleep(.05)
                '''
                #id-sicom
                if id:
                    pass
                else:
                    self.esperar_xpath('//*[@id="select2-location_select_ID_SICOM-container"]')
                    self.driver.find_element(By.XPATH,'/html/body/span/span/span[*]/input').send_keys(id_sicom)
                    self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                    time.sleep(1.5)

                #guardar
                #esperar_xpath('//*[@id="forms_button_save"]')
                    
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content()
                
        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ou \nnão é o poste',keep_on_top=True)

    def cabo_precon(self,id_sicon,num_pri,num_ori,num_sec,cabo,sob_demanda=False,cabo_rs=False,projeto=True):
        wdw = WebDriverWait(self.driver, 30)
        self.iframe('iframe-content-wrapper')
        try:    
            #Tipo
            self.esperar_selecionar_ID('cableModelType','1902372') #CFOAC-BLI-AS
            #Fibras
            self.esperar_selecionar_ID('cableCapacity','1')
            if cabo_rs:
                #Fabricante
                self.esperar_selecionar_ID('idManufacturer','885995') #Corning
            else:
                #Fabricante
                self.esperar_selecionar_ID('idManufacturer','885997') #FURUKAWA
            #Modelo
            '''
            modelo = self.driver.find_elements(By.ID,'catModelId')
            for i in modelo:
                print(i)
            '''
            #Lote
            self.esperar_txt_ID('lot','BT')
            if projeto:
                #ID SICOM
                self.esperar_txt_ID('idSicom',id_sicon)
                self.esperar_xpath('/html/body/div[*]/div[*]/form/div/div[2]/table[2]/tbody/tr[1]/td[3]/div[2]/div/ul/li/a')
            else:
                #Nome de projeto 
                self.esperar_txt_ID('project',id_sicon)
                self.esperar_xpath('//*[@id="project_div"]/ul/li/a')
            #Destinção
            self.esperar_selecionar_value('destinationId','1000385')
            #pop up
            if 'Tem certeza que deseja continuar?' in self.driver.find_element(By.ID,'ModalDialog').text:
                self.driver.switch_to.active_element
                self.esperar_clicar_xpath('/html/body/div[*]/div[11]/div/button[1]/span')
            else:
                pass
            time.sleep(1)
            #estação abastecedora
            self.esperar_xpath('/html/body/div[*]/div[2]/form/div/ul/li[2]/a/label')    
            self.esperar_xpath('/html/body/div[*]/div[2]/form/div/div[7]/table/tbody/tr[6]/td/div[2]/select/option')
            self.esperar_clicar_ID('addStationButton2')     
            #rastreabilidade
            self.esperar_xpath('/html/body/div[*]/div[2]/form/div/ul/li[7]/a/label')
            self.esperar_selecionar_ID('sourceCableId','1000139') #netwim
            #caracteristica
            self.esperar_xpath('/html/body/div[*]/div[2]/form/div/ul/li[1]/a/label')
            if sob_demanda:
                #instalação futura
                self.esperar_clicar_ID('futureInstall')
                self.esperar_selecionar_ID('catProjectStateId','190')
            else:
                pass
            #Tipo
            self.esperar_selecionar_ID('nomencTypeId','1000365') #secundario
            # Número do cabo primário
            self.esperar_txt_ID('cableNr',num_pri)
            #Nó de origem significativa
            time.sleep(1)
            self.esperar_txt_ID('significativeOriginNodeId',num_ori)
            self.esperar_xpath('/html/body/div[*]/div[*]/form/div/div[2]/table[2]/tbody/tr[25]/td/div[2]/div/ul/li/a')
            time.sleep(2)
            # Número do cabo secundário
            self.esperar_txt_ID('cableSecNumber',num_sec)
            if cabo_rs:
                #identificação de campo
                self.esperar_selecionar_ID('labelCampId','1000448') #existente conforme
            else:
                #identificação de campo
                self.esperar_selecionar_ID('labelCampId','1000450') #existente não validado
            #rota
            self.esperar_clicar_ID('unknownRouteFalse')   
            
            res = int(cabo)
            
            #CL e folgas
            self.esperar_xpath('/html/body/div[*]/div[2]/form/div/ul/li[4]/a/label')
            time.sleep(.5)
            #caracteristica
            self.esperar_xpath('/html/body/div[*]/div[2]/form/div/ul/li[1]/a/label')
            time.sleep(.5)
            #CL e folgas
            self.esperar_xpath('/html/body/div[*]/div[2]/form/div/ul/li[4]/a/label')
            self.driver.find_element(By.XPATH,'/html/body/div[*]/div[2]/form/div/ul/li[4]/a/label').click()
            time.sleep(.5)

            #total
            wdw.until(element_to_be_clickable(('xpath', '/html/body/div[*]/div[2]/form/div/div[5]/div/div[3]/div[4]/div/table/tbody/tr/td[3]')))
            tot_cl = self.driver.find_element(By.XPATH,'/html/body/div[*]/div[2]/form/div/div[5]/div/div[3]/div[4]/div/table/tbody/tr/td[3]')
            cl_folgas = tot_cl.get_attribute('title')
            resultado = str(res - float(cl_folgas))
            
            #final
            self.esperar_xpath('/html/body/div[*]/div[2]/form/div/div[5]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[5]') #inicial
            wdw.until(element_to_be_clickable(('id', '1_clearance'))) #folga(m)
            lote = self.driver.find_element(By.ID,'1_clearance')
            lote.clear()
            
            #resultado
            self.esperar_txt_ID('1_clearance', resultado)  
            self.esperar_xpath('.//label[@for="edit-button"]')   
            
            #caracteristica
            self.esperar_xpath('/html/body/div[*]/div[2]/form/div/ul/li[1]/a/label')  
            
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()

        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ou \nnão é o CABO',keep_on_top=True)

    def traçado (self,id_Sicom,traçado=True, origem=True,projeto=True):
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
                #id sicon
                self.esperar_txt_ID('idSicom',id_Sicom)
                self.esperar_xpath('/html/body/div[*]/div[2]/form/div/div[2]/table[4]/tbody/tr[2]/td[1]/div[2]/div/ul/li')
                
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
                 
    def ler_pdf(self):
        dataframe = pd.read_excel('Loc_Est_RMS.xlsx', index_col=0,usecols="D,E") 
        for i in dataframe:
            pass

    def abastecimento(self,hp):
        try:
            self.driver.implicitly_wait(0)
            wdw = WebDriverWait(self.driver, .1)
            # Esperando até seja visivel as Iframe da pagina
            wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
            wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
            #ir para aba de abastecimento
            self.esperar_clicar_ID('influenceAreaButton')
            
            def procurar_hp(survey):
                lista  = survey.split(',')
                for hp in lista:
                    for i in range(1,167):
                        tr = str(i)
                        xpath_primareira_linha = ".//table[@class='connectionsTable']/tbody/tr["
                        #xpath_segunda_linha = "]/td"
                        #xpath para encontrar linhas na tabela
                        #xpath_linha = xpath_primareira_linha + str(i) + xpath_segunda_linha
                        primeira_parte_survey = "]/td[text()='"
                        segunda_parte_survey = "']"
                        #xpath para encontrar linhas na tabela e hp na tabela
                        xpath_hp = (xpath_primareira_linha + tr + primeira_parte_survey + hp + segunda_parte_survey)
                        try:
                            #espera até o elemento esteja presente na DOM
                            if self.driver.find_element(By.XPATH,xpath_hp):
                                survey = self.driver.find_element(By.XPATH,xpath_hp).text
                                if survey == hp:
                                    primeira_parte_abastecimento = xpath_primareira_linha
                                    segunda_parte_abastecimento = ']/td[1]/a'
                                    xpath_abastecimento = (primeira_parte_abastecimento + tr + segunda_parte_abastecimento)
                                    self.driver.find_element(By.XPATH,xpath_abastecimento).click()
                                    if "Alerta" in self.driver.find_element(By.XPATH,"//*[@id='ui-id-3']").Text:
                                        self.driver.find_element(By.XPATH,"//*[@id='captionCancel']/span").Click
                                        break
                                    else:
                                        break
                                else:
                                    break
                            else:
                                    break
                        except:
                            pass 
                                    
            procurar_hp(hp)
                    
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()
            
        except:
             sg.po
         
    def encontrar_projetado(self):
        self.iframe('iframe-content-wrapper')
        self.iframe('elementSearchFrame')
        tabela = self.driver.find_elements(By.ID,'results')
        for i in tabela:
            if 'Projetado' in i.text:
                self.driver.find_element(By.ID,'results').get_property
            else:
                print('nem encontrei')

    def hub_box_p(self,id_sicon,estacao,numero, hub_box=True):
        self.iframe('iframe-content-wrapper')
        self.iframe('externalIspIframe')
        self.iframe('dados')
        try:
            if hub_box:
                #tipo
                self.esperar_selecionar_value('elem_num_sap','332032') #CAIXA DIST OPT E 8 TAP A HUB 
            else:
                self.esperar_selecionar_value('elem_num_sap','321408') #ceos p

            #rede
            self.esperar_selecionar_value('network','Óptica GPON')
            if hub_box:
                pass
            else:
                self.esperar_selecionar_value('idFabricante','GENÉRICO')
            #destinação 
            self.esperar_selecionar_value('destinationId','1000385') #acesso gpon
            #Id-sicon
            self.esperar_txt_ID('id_sicom_name',id_sicon)
            self.esperar_xpath('//li[@class="ac_even ac_over"]')
            if hub_box:
                pass
            else:
                self.esperar_clicar_ID('outOfPattern_check')
                time.sleep(.5)
                self.esperar_txt_ID('tagOnField','CEOS-P-01')
            time.sleep(.5)
            #identiicar local para escrita/escrever , confirmar
            self.esperar_selecionar_ID_txt('supplierStationName',estacao)
            self.esperar_xpath('//li[@class="ac_even ac_over"]')
            if hub_box:
                #numero da ceos
                self.esperar_selecionar_ID_txt('nomecNumber',numero)
            else:
                self.esperar_txt_ID('nomecNumber','N/D')

            #identificação de campo
            self.esperar_selecionar_value('nameCampId','Existente - Conforme')
            #estação abastecedora 
            self.esperar_link_txt('Estações abastecedoras')
            self.esperar_txt_ID('autocompleteSLocation',estacao)
            self.esperar_xpath('//li[@class="ac_even ac_over"]')
            self.esperar_clicar_ID('adicionar')
            #Rastreabilidade
            self.esperar_link_txt('Rastreabilidade')
            self.esperar_selecionar_ID('sourceId','Netwin')
            #Identificação
            self.esperar_link_txt('Identificação')

            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()

        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ou \nnão é a Hub/Ceos p',keep_on_top=True)

    def cdoi(self,id_sicon,estacao,topologia=True):
        self.iframe('iframe-content-wrapper')
        self.iframe('externalIspIframe')
        self.iframe('dados')
        try:
            #tipo
            self.esperar_selecionar_value('elem_tipo.outroNomeEquip','CDOI MODULAR até 64 ADP')
            #rede
            self.esperar_selecionar_value('network','Óptica GPON')
            #fabricante
            self.esperar_selecionar_value('idFabricante','FURUKAWA')
            #Id-sicon
            self.esperar_txt_ID('id_sicom_name',id_sicon)
            self.esperar_xpath('//li[@class="ac_even ac_over"]')

            if topologia:
                self.esperar_selecionar_value('topology','A/B')
            else:
                self.esperar_selecionar_value('topology','C')
            #identiicar local para escrita/escrever , confirmar
            self.esperar_selecionar_ID_txt('supplierStationName',estacao)
            self.esperar_xpath('//li[@class="ac_even ac_over"]')
            #identificação de campo
            self.esperar_selecionar_value('nameCampId','Existente - Conforme')
            #estação abastecedora 
            self.esperar_link_txt('Estações abastecedoras')
            self.esperar_txt_ID('autocompleteSLocation',estacao)
            self.esperar_xpath('//li[@class="ac_even ac_over"]')
            self.esperar_clicar_ID('adicionar')
            #Rastreabilidade
            self.esperar_link_txt('Rastreabilidade')
            self.esperar_selecionar_ID('sourceId','Netwin')
            #Identificação
            self.esperar_link_txt('Identificação')

            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()

        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ou \nnão é a CDOI',keep_on_top=True)

    def spliter_hub(self,topologia=True):
        self.iframe('iframe-content-wrapper')
        self.iframe('externalFrame')
        self.iframe('dados')
        try:
            #componentes
            self.esperar_link_txt('Componentes')
            #+
            self.esperar_clicar_ID('addNoPosComp')
            time.sleep(1)
            self.iframe('targetIframe')

            if topologia:
                #modelo
                self.esperar_selecionar_value('idTipoElemento','20751') #1:2
                time.sleep(.1)
                #legado
                self.esperar_selecionar_value('LEGADO','NÃO')
                time.sleep(.1)
                #confirmar
                esperar1
                self.esperar_clicar_ID('confAssoc')
                esperar1
                #fechar
                self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
                self.driver.switch_to.default_content()

        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ou \nnão é a o spliter da HUB',keep_on_top=True)

    def conectividade_1_8(self,spliter=True,iframe=True):
        if iframe:
            wdw = WebDriverWait(self.driver, 60)
            self.iframe('iframe-content-wrapper')
            self.iframe('externalFrame')
        else:
            pass
        try:
            #cenario
            self.esperar_selecionar_value('cbScenario','pdo_splitter') #Fibra óptica 1:1 Splitter n:n Porta CDO
            time.sleep(1.5)
            #cabo
            self.esperar_selecionar_index('cable_inout_1main',1)
            #fibra
            self.esperar_selecionar_value('fiber_inout_1main','1')
            if spliter:
                #spliter
                self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1/8
            else:
                #spliter
                self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1/16
            #porta de entrada
            self.esperar_selecionar_index('splitter_port_in_2main',1)
            #porta saida inicial
            self.esperar_selecionar_index('splitter_port_out_2main',1)
            if spliter:
                #porta final
                self.esperar_selecionar_index('splitter_port_out_2main_final','8')
            else:
                #porta final
                self.esperar_selecionar_index('splitter_port_out_2main_final','16')
            #Fibra Inicial
            self.esperar_selecionar_index('pdoport_inout_3main',1)
            if spliter:
                #porta final
                self.esperar_selecionar_index('pdoport_inout_3main_final','8')
            else:
                #porta final
                self.esperar_selecionar_index('pdoport_inout_3main_final','16')
            #ligar
            self.esperar_clicar_ID('connectButton')
            time.sleep(.05)
            #tipo ligador
            self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
            #confimar
            self.esperar_clicar_ID('attributesConfirmButton')
            self.driver.switch_to.default_content()
            self.iframe('iframe-content-wrapper')
            #x
            self.esperar_xpath('//*[@class="ui-icon ui-icon-closethick"]')

            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()
        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ',keep_on_top=True)
    
    def spliter_cdoi(self,spliter=True):
        self.iframe('iframe-content-wrapper')
        self.iframe('externalFrame')
        self.iframe('dados')
        try:
            #componentes
            self.esperar_link_txt('Componentes')
            #+
            self.esperar_clicar_ID('addNoPosComp')
            time.sleep(1)
            self.iframe('targetIframe')

            if spliter:
                #modelo
                self.esperar_selecionar_value('idTipoElemento','13928') #1:64
                time.sleep(.1)
                #legado
                self.esperar_selecionar_value('LEGADO','NÃO')
                time.sleep(.1)
            else:
                #modelo
                self.esperar_selecionar_value('idTipoElemento','13910') #1:8
                time.sleep(.1)
                #legado
                self.esperar_selecionar_value('LEGADO','Não')
                time.sleep(.1)
            #confirmar
            esperar1
            self.esperar_clicar_ID('confAssoc')
            esperar1
            #fechar
            self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
            self.driver.switch_to.default_content()
        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ou \nnão é o Spliter da CDOI',keep_on_top=True)

    def cabo_primario(self,id_sicon,primario,value_12=False,value_24=False,value_36=False,value_48=False,value_72=False,value_144=False,value_288=False,id_sicom=True):
        wdw = WebDriverWait(self.driver, 30)
        self.iframe('iframe-content-wrapper')
        try:
            #tipo
            self.esperar_selecionar_value('cableModelType','1902376') #CFOA-SM-DD
            if value_12:
                #fibra
                self.esperar_selecionar_value('cableCapacity','12')
            elif value_24:
                #fibra
                self.esperar_selecionar_value('cableCapacity','24')
            elif value_36:
                #fibra
                self.esperar_selecionar_value('cableCapacity','36')
            elif value_48:
                #fibra
                self.esperar_selecionar_value('cableCapacity','48')
            elif value_72:
                #fibra
                self.esperar_selecionar_value('cableCapacity','72')
            elif value_144:
                #fibra
                self.esperar_selecionar_value('cableCapacity','144')
            elif value_288:
                #fibra
                self.esperar_selecionar_value('cableCapacity','288')
            else:
                pass
            #fabricante
            self.esperar_selecionar_index('idManufacturer',2) #furakwa
            #modelo
            self.esperar_selecionar_index('catModelId',1)
            #lote
            self.esperar_txt_ID('lot','BT')
            if id_sicom:
                #ID SICOM
                self.esperar_txt_ID('idSicom',id_sicon)
                self.esperar_xpath('/html/body/div[*]/div[*]/form/div/div[2]/table[2]/tbody/tr[1]/td[3]/div[2]/div/ul/li/a')
            else:
                #ID SICOM
                self.esperar_txt_ID('project',id_sicon)
                self.esperar_xpath('/html/body/div[*]/div[*]/form/div/div[2]/table[2]/tbody/tr[1]/td[2]/div[2]/div/ul/li/a')

            #Destinção
            self.esperar_selecionar_value('destinationId','1000385')
            if 'Tem certeza que deseja continuar?' in self.driver.find_element(By.ID,'ModalDialog').text:
                    self.driver.switch_to.active_element
                    self.esperar_clicar_xpath('/html/body/div[*]/div[11]/div/button[1]/span')
            else:
                pass

            #Tipo
            self.esperar_selecionar_index('nomencTypeId',2) #primario 
            #numero cabo primario
            self.esperar_txt_ID('cableNr',primario)
            #identificação de campo
            self.esperar_selecionar_value('labelCampId','1000448')
            #conhecida
            self.esperar_clicar_ID('unknownRouteFalse')
            #estação abastecedora
            self.esperar_xpath('/html/body/div[*]/div[2]/form/div/ul/li[2]/a/label')    
            self.esperar_xpath('/html/body/div[*]/div[2]/form/div/div[7]/table/tbody/tr[6]/td/div[2]/select/option')
            self.esperar_clicar_ID('addStationButton2')  
            #rastreabilidade
            self.esperar_link_txt('Rastreabilidade')
            #origem
            self.esperar_selecionar_value('sourceCableId','1000139')
            time.sleep(1.5)
            #guardar
            self.esperar_clicar_xpath('/html/body/div[*]/div[3]/div/button[1]/span')

            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()
          
        except:
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            sg.popup_error(f'Ixi deu um erro ae O_O \nse pa você ta no caminho errado ou \nnão é o Cabo',keep_on_top=True)

    def conectividade_cdoi(self,cdoi_64=True):
        wdw = WebDriverWait(self.driver, 60)
        self.iframe('iframe-content-wrapper')
        self.iframe('externalFrame')    
        if cdoi_64:
            #cenario
            self.esperar_selecionar_value('cbScenario','pdo_splitter') #Fibra óptica 1:1 Splitter n:n Porta CDO
            #cabo
            time.sleep(1)
            self.esperar_selecionar_index('cable_inout_1main',1)
            #fibra
            self.esperar_selecionar_value('fiber_inout_1main','1')
            #Spliter
            self.esperar_selecionar_index('splitter_ratio_inout_2main',1)
            #Porta de entrada
            self.esperar_selecionar_index('splitter_port_in_2main',1)
            #Porta saida inicial
            self.esperar_selecionar_value('splitter_port_out_2main','2483041789')
            #Porta saida final
            self.esperar_selecionar_value('splitter_port_out_2main_final','2483041920')
            #Porta inicial
            self.esperar_selecionar_value('pdoport_inout_3main','2483038371')
            #Porta final
            self.esperar_selecionar_value('pdoport_inout_3main_final','2483038587')   
            #clicar ligar
            self.esperar_clicar_ID('connectButton')
            #tipo ligador
            self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
            #confirmar
            self.esperar_clicar_ID('attributesConfirmButton')

    def Spliter_completa(self):
        self.driver.implicitly_wait(.1)
        wdw = WebDriverWait(self.driver, 60)
        wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
        wdw.until(frame_to_be_available_and_switch_to_it(('id','elementSearchFrame')))
        
        def sair():
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()
            wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
            time.sleep(0.5)
            #fechar
            self.esperar_xpath('.//span[@class="ui-icon ui-icon-closethick"]')
            wdw.until(frame_to_be_available_and_switch_to_it(('id','elementSearchFrame')))
            
        for olho in range(1,60):
            time.sleep(.5)
            xpath_linha = f'.//*[@id="results"]/tbody/tr[{olho}]'
            time.sleep(.5)
            xpath_olho = f'.//*[@id="results"]/tbody/tr[{olho}]/td[10]/i'
            try:
                time.sleep(1.5)
                self.driver.find_element(By.XPATH,xpath_olho).click()
            except:
                print('Não encontrei a linha para colocar spliter:)')
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content()
                break
            time.sleep(1)
            #espera até o elemento esteja presente na DOM
            if self.driver.find_element(By.XPATH,xpath_linha):
                self.driver.switch_to.default_content()
                #Esperando até seja visivel as Iframe da pagina
                wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
                wdw.until(frame_to_be_available_and_switch_to_it(('id','dados')))
                time.sleep(2)
                cdoe = self.driver.find_element(By.XPATH,'//*[@id="idTipoElemento"]').get_attribute('value')
                #self.nome_CDOE = self.driver.find_element(By.XPATH,'//*[@id="elem_tipo.outroNomeEquip"]').get_attribute('text')
                if cdoe == '271':
                    #Esperando elemento sap ser visivel
                    time.sleep(.1)
                    cdoe_sap = self.driver.find_element(By.ID,'elem_num_sap').get_attribute('value')
                    #escolhendo equipamento para colocar spliter
                    if cdoe_sap == '332013': #17 tap final de cabo
                        self.driver.switch_to.default_content()
                        self.iframe('iframe-content-wrapper')
                        self.iframe('externalFrame')
                        self.iframe('dados')
                        #componetes
                        self.esperar_xpath('/html/body/table/tbody/tr/td/div/div/div/form/div/table/tbody/tr[*]/td/div/ul/li[4]/a/span')
                        #+
                        self.esperar_clicar_ID('addNoPosComp')
                        time.sleep(1)
                        self.iframe('targetIframe')
                        #modelo
                        self.esperar_selecionar_value('idTipoElemento','20723') #1:16
                        #legado
                        self.esperar_selecionar_value('LEGADO','NÃO')
                        time.sleep(1)
                        #confirmar
                        self.esperar_clicar_ID('confAssoc')
                        esperar1
                        #fechar
                        self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
                        sair()
                                    
                    elif cdoe_sap == '332014': #18 tap intermediaria corning
                        self.driver.switch_to.default_content()
                        self.iframe('iframe-content-wrapper')
                        self.iframe('externalFrame')
                        self.iframe('dados')
                        #componetes
                        self.esperar_xpath('/html/body/table/tbody/tr/td/div/div/div/form/div/table/tbody/tr[*]/td/div/ul/li[4]/a/span')
                        #+
                        self.esperar_clicar_ID('addNoPosComp')
                        time.sleep(1)
                        self.iframe('targetIframe')
                        #modelo
                        self.esperar_selecionar_value('idTipoElemento','20752') #1:16
                        time.sleep(1.5)
                        #legado
                        self.esperar_selecionar_value('LEGADO','NÃO')
                        time.sleep(1.5)
                        #confirmar
                        esperar1
                        self.esperar_clicar_ID('confAssoc')
                        esperar1
                        #fechar
                        self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
                        time.sleep(1)
                        
                        self.driver.switch_to.default_content()
                        self.iframe('iframe-content-wrapper')
                        self.iframe('externalFrame')
                        self.iframe('dados')
                        
                        #+
                        self.esperar_clicar_ID('addNoPosComp')
                        self.iframe('targetIframe')
                        #modelo
                        self.esperar_selecionar_value('idTipoElemento','20727') #1:2
                        #legado
                        self.esperar_selecionar_value('LEGADO','NÃO')
                        time.sleep(1)
                        #confirmar
                        esperar1
                        self.esperar_clicar_ID('confAssoc')
                        esperar1
                        #fechar
                        self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
                        sair()
                                    
                    elif cdoe_sap == '331995': #9 tap final de cabo corning
                        self.driver.switch_to.default_content()
                        self.componentes()
                        sair()
                                    
                    elif cdoe_sap == '331688': #10 tap intermediaria corning
                        self.driver.switch_to.default_content()
                        self.componentes(False)
                        sair()
                                
                    else:
                        sair()        
                else:
                    sair()
            else:
                sair()        

    def Conectividade_completa(self,iframe=True):
        self.driver.implicitly_wait(.05)
        wdw = WebDriverWait(self.driver, 30)
        
        if iframe:
            # Esperando até seja visivel as Iframe da pagina
            wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
            wdw.until(frame_to_be_available_and_switch_to_it(('id','elementSearchFrame')))
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
            time.sleep(.05)
            xpath_linha = f'.//*[@id="results"]/tbody/tr[{mancha}]'
            xpath_capacidade = '/td[4]'
            time.sleep(1)
            xpath_mancha = f'.//*[@id="results"]/tbody/tr[{mancha}]/td[12]/i'
            try:
                capacidade = self.driver.find_element(By.XPATH,xpath_linha + xpath_capacidade ).text
                time.sleep(1)
                self.driver.find_element(By.XPATH,xpath_mancha).click()
            except:
                print('Não encontrei a linha para fazer a conectividade :)')
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content()
                break
            time.sleep(1)
            #espera até o elemento esteja presente na DOM
            if self.driver.find_element(By.XPATH,xpath_linha):
                self.driver.switch_to.default_content()
                #Esperando até seja visivel as Iframe da pagina
                wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                if '16' in capacidade:
                    try:
                        if self.driver.find_element(By.XPATH,'//*[@id="externalArea"]'):
                            #Esperando até seja visivel as Iframe da pagina
                            wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
                    except:
                        break
                    try:
                        #Cenario
                        time.sleep(.1)
                        wdw.until(element_to_be_clickable((By.ID,'cbScenario')))
                    except:
                        break
                    selecionar = Select(self.driver.find_element(By.ID,'cbScenario'))
                    selecionar.select_by_value('difusion')
                    #spliter
                    time.sleep(.1)
                    wdw.until(element_to_be_clickable((By.ID,'splitter_ratio_inout_2main')))
                    selecionar_1 = self.driver.find_element(By.ID,'splitter_ratio_inout_2main')
                    time.sleep(.05)
                    try:
                        spliter = selecionar_1.find_element(By.XPATH,'//*[@id="splitter_ratio_inout_2main"]/option[2]').get_attribute('text')
                        cabo_inicial = self.driver.find_element(By.XPATH,'//*[@id="cable_inout_1main"]')
                        cabo_1 = cabo_inicial.find_element(By.XPATH,'//*[@id="cable_inout_1main"]/option[2]').get_attribute('text')
                        cabo_final = self.driver.find_element(By.XPATH,'//*[@id="cable_inout_3main"]')
                        cabo_2 = cabo_final.find_element(By.XPATH,'//*[@id="cable_inout_3main"]/option[2]').get_attribute('text')
                    except:
                        sair()
                        continue
                    time.sleep(.05)
                    if cabo_1 == cabo_2:
                        sair()
                        xpath_olho = f'.//*[@id="results"]/tbody/tr[{mancha}]/td[10]/i'
                        time.sleep(2)
                        self.driver.find_element(By.XPATH,xpath_olho).click()
                        time.sleep(0.5)
                        self.driver.switch_to.default_content()
                        #Esperando até seja visivel as Iframe da pagina
                        wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                        wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
                        wdw.until(frame_to_be_available_and_switch_to_it(('id','dados')))
                        time.sleep(2)
                        cdoe_sap = self.driver.find_element(By.ID,'elem_num_sap').get_attribute('value')
                        sair()
                        if cdoe_sap == '332014': #18 tap intermediaria corning
                            try:
                                try:
                                    try:
                                        self.driver.find_element(By.XPATH,xpath_mancha).click()
                                    except:
                                        print('não consegui clicar')  
                                    self.driver.switch_to.default_content() 
                                    # Esperando até seja visivel as Iframe da pagina
                                    wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                                    wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
                                    time.sleep(0.5)   
                                    #cenario
                                    self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                                    time.sleep(1.5)
                                    #cabo
                                    self.esperar_selecionar_index('cable_inout_1main',1)
                                    #fibra
                                    self.esperar_selecionar_value('fiber_inout_1main','1')
                                    #spliter
                                    self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:2
                                    #porta de entrada
                                    self.esperar_selecionar_index('splitter_port_in_2main',1)
                                    #porta saida 
                                    self.esperar_selecionar_index('splitter_port_out_2main',2)
                                    #spliter
                                    self.esperar_selecionar_index('splitter_ratio_inout_3main',1)  #1:16
                                    #porta entrada
                                    self.esperar_selecionar_index('splitter_port_in_3main',1)
                                    #porta saida inicial
                                    self.esperar_selecionar_index('splitter_port_out_3main',1)
                                    #porta saida final
                                    self.esperar_selecionar_index('splitter_port_out_3main_final',16)
                                    #porta inicial
                                    self.esperar_selecionar_index('pdoport_inout_4main',1)
                                    #porta final
                                    self.esperar_selecionar_index('pdoport_inout_4main_final',16)
                                    #ligar
                                    self.esperar_clicar_ID('connectButton')
                                    #tipo ligador
                                    self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                                    #tipo ligador
                                    self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                                    #confirmar
                                    self.esperar_clicar_ID('attributesConfirmButton')
                                    print(f'{xpath_mancha}\n,fim de cabo')
                                    sair()
                                except:
                                    try:
                                        time.sleep(0.5)
                                        self.driver.find_element(By.XPATH,xpath_mancha).click()
                                    except:
                                        print('não consegui clicar')  
                                    self.driver.switch_to.default_content() 
                                    # Esperando até seja visivel as Iframe da pagina
                                    wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                                    wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
                                    time.sleep(0.5)    
                                    #cenario
                                    self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                                    time.sleep(1.5)
                                    #cabo
                                    self.esperar_selecionar_index('cable_inout_1main',1)
                                    #fibra
                                    self.esperar_selecionar_value('fiber_inout_1main','1')
                                    #spliter
                                    self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1:2
                                    #porta de entrada
                                    self.esperar_selecionar_index('splitter_port_in_2main',1)
                                    #porta saida 
                                    self.esperar_selecionar_index('splitter_port_out_2main',2)
                                    #spliter
                                    self.esperar_selecionar_index('splitter_ratio_inout_3main',2)  #1:16
                                    #porta entrada
                                    self.esperar_selecionar_index('splitter_port_in_3main',1)
                                    #porta saida inicial
                                    self.esperar_selecionar_index('splitter_port_out_3main',1)
                                    #porta saida final
                                    self.esperar_selecionar_index('splitter_port_out_3main_final',16)
                                    #porta inicial
                                    self.esperar_selecionar_index('pdoport_inout_4main',1)
                                    #porta final
                                    self.esperar_selecionar_index('pdoport_inout_4main_final',16)
                                    #ligar
                                    self.esperar_clicar_ID('connectButton')
                                    #tipo ligador
                                    self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                                    #tipo ligador
                                    self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                                    #confirmar
                                    self.esperar_clicar_ID('attributesConfirmButton')
                                    print(f'{xpath_mancha}\n,fim de cabo')
                                    sair()
                            except Exception as e:
                                print(e)
                                sg.popup_error('Tem que prestar atenção no cadastro pow\n','Evite conversar\n','Mexer no celular\n', 'Desviar atenção na hora de acionar o programa\n','Reinicie o programa',keep_on_top=True)
                                sair()
                        else:
                            try:
                                try:
                                    time.sleep(0.5)
                                    self.driver.find_element(By.XPATH,xpath_mancha).click()
                                except:
                                    print('não consegui clicar') 
                                # Retorna para a janela principal (fora do iframe)
                                self.driver.switch_to.default_content()
                                self.iframe('iframe-content-wrapper')
                                self.iframe('externalFrame')
                                
                                try:
                                    #cenario
                                    time.sleep(0.5)
                                    self.esperar_selecionar_value('cbScenario','pdo_splitter') #Fibra óptica 1:1 Splitter n:n Porta CDO
                                    time.sleep(2)
                                    #cabo
                                    self.esperar_selecionar_index('cable_inout_1main',1)
                                    #fibra
                                    self.esperar_selecionar_value('fiber_inout_1main','1')
                                    time.sleep(.5)
                                    #spliter
                                    self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1/16
                                    #porta de entrada
                                    self.esperar_selecionar_index('splitter_port_in_2main',1)
                                    #porta saida inicial
                                    self.esperar_selecionar_index('splitter_port_out_2main',1)
                                
                                    #porta final
                                    self.esperar_selecionar_index('splitter_port_out_2main_final','16')
                                    #Fibra Inicial
                                    self.esperar_selecionar_index('pdoport_inout_3main',1)
                                
                                    #porta final
                                    self.esperar_selecionar_index('pdoport_inout_3main_final','16')
                                    #ligar
                                    self.esperar_clicar_ID('connectButton')
                                    time.sleep(.05)
                                    #tipo ligador
                                    self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                                    #confimar
                                    self.esperar_clicar_ID('attributesConfirmButton')
                                    sair()
                                except:
                                    print('não consegui clicar')
                                    sair()

                                print(f'{xpath_mancha}\n,fim de cabo')
                            except Exception as e:
                                print(e)
                                sg.popup_error('Tem que prestar atenção no cadastro pow\n','Evite conversar\n','Mexer no celular\n', 'Desviar atenção na hora de acionar o programa\n','Reinicie o programa',keep_on_top=True)
                                sair()
                        
                    elif spliter == 'S16_1':
                        try:
                            try:
                                #cenario
                                time.sleep(0.5)
                                self.esperar_selecionar_value('cbScenario','difusion') #Fibra óptica 1:1 Splitter n:n Fibra óptica
                                wdw.until(element_to_be_clickable(('id', 'splitter_ratio_inout_2main')))
                                self.esperar_clicar_ID('splitter_ratio_inout_2main')
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','1')
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_2main',1)
                                #cabo
                                self. esperar_selecionar_index('cable_inout_3main',1)
                                #Fibra Inicial
                                self.esperar_selecionar_index('fiber_inout_3main',1)
                                #ligar
                                self.esperar_clicar_ID('connectButton')
                                #confirmar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                #OK
                                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                                time.sleep(1.5)
                                #cenario
                                self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                                time.sleep(2)
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','1')
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida 
                                self.esperar_selecionar_index('splitter_port_out_2main',2)
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_3main',1)  #1:16
                                #porta entrada
                                self.esperar_selecionar_index('splitter_port_in_3main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_3main',1)
                                #porta saida final
                                self.esperar_selecionar_index('splitter_port_out_3main_final',16)
                                #porta inicial
                                self.esperar_selecionar_index('pdoport_inout_4main',1)
                                #porta final
                                self.esperar_selecionar_index('pdoport_inout_4main_final',16)
                                #ligar
                                self.esperar_clicar_ID('connectButton')
                                #tipo ligador
                                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                                #tipo ligador
                                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                                #confirmar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                print(f'{xpath_mancha}\n,Conectividade feita')
                                sair()
                            except:
                                #cenario
                                time.sleep(0.5)
                                self.esperar_selecionar_value('cbScenario','difusion') #Fibra óptica 1:1 Splitter n:n Fibra óptica
                                wdw.until(element_to_be_clickable(('id', 'splitter_ratio_inout_2main')))
                                self.esperar_clicar_ID('splitter_ratio_inout_2main')
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','1')
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1:2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_2main',1)
                                #cabo
                                self. esperar_selecionar_index('cable_inout_3main',1)
                                #Fibra Inicial
                                self.esperar_selecionar_index('fiber_inout_3main',1)
                                #ligar
                                self.esperar_clicar_ID('connectButton')
                                #confirmar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                #OK
                                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                                time.sleep(1.5)
                                #cenario
                                self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                                time.sleep(2)
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','1')
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1:2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida 
                                self.esperar_selecionar_index('splitter_port_out_2main',2)
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_3main',2)  #1:16
                                #porta entrada
                                self.esperar_selecionar_index('splitter_port_in_3main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_3main',1)
                                #porta saida final
                                self.esperar_selecionar_index('splitter_port_out_3main_final',16)
                                #porta inicial
                                self.esperar_selecionar_index('pdoport_inout_4main',1)
                                #porta final
                                self.esperar_selecionar_index('pdoport_inout_4main_final',16)
                                #ligar
                                self.esperar_clicar_ID('connectButton')
                                #tipo ligador
                                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                                #tipo ligador
                                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                                #confirmar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                print(f'{xpath_mancha}\n,Conectividade feita')
                                sair()
                        except Exception as e:
                            print(e)
                            sg.popup_error('Tem que prestar atenção no cadastro pow\n','Evite conversar\n','Mexer no celular\n', 'Desviar atenção na hora de acionar o programa\n','Reinicie o programa',keep_on_top=True)
                            sair()
                            
                    elif spliter == 'S2_1':
                        try:
                            try:
                                #cenario
                                time.sleep(0.5)
                                self.esperar_selecionar_value('cbScenario','difusion') #Fibra óptica 1:1 Splitter n:n Fibra óptica
                                wdw.until(element_to_be_clickable(('id', 'splitter_ratio_inout_2main')))
                                self.esperar_clicar_ID('splitter_ratio_inout_2main')
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','1')
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1:2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_2main',1)
                                #cabo
                                self. esperar_selecionar_index('cable_inout_3main',1)
                                #Fibra Inicial
                                self.esperar_selecionar_index('fiber_inout_3main',1)
                                #ligar
                                self.esperar_clicar_ID('connectButton')
                                #confirmar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                #OK
                                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                                time.sleep(1.5)
                                #cenario
                                self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                                time.sleep(2)
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','1')
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1:2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida 
                                self.esperar_selecionar_index('splitter_port_out_2main',2)
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_3main',2)  #1:16
                                #porta entrada
                                self.esperar_selecionar_index('splitter_port_in_3main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_3main',1)
                                #porta saida final
                                self.esperar_selecionar_index('splitter_port_out_3main_final',16)
                                #porta inicial
                                self.esperar_selecionar_index('pdoport_inout_4main',1)
                                #porta final
                                self.esperar_selecionar_index('pdoport_inout_4main_final',16)
                                #ligar
                                self.esperar_clicar_ID('connectButton')
                                #tipo ligador
                                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                                #tipo ligador
                                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                                #confirmar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                print(f'{xpath_mancha}\n,Conectividade feita')
                                sair()
                            except:
                                #cenario
                                time.sleep(0.5)
                                self.esperar_selecionar_value('cbScenario','difusion') #Fibra óptica 1:1 Splitter n:n Fibra óptica
                                wdw.until(element_to_be_clickable(('id', 'splitter_ratio_inout_2main')))
                                self.esperar_clicar_ID('splitter_ratio_inout_2main')
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','1')
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_2main',1)
                                #cabo
                                self. esperar_selecionar_index('cable_inout_3main',1)
                                #Fibra Inicial
                                self.esperar_selecionar_index('fiber_inout_3main',1)
                                #ligar
                                self.esperar_clicar_ID('connectButton')
                                #confirmar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                #OK
                                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                                time.sleep(1.5)
                                #cenario
                                self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                                time.sleep(2)
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','1')
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida 
                                self.esperar_selecionar_index('splitter_port_out_2main',2)
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_3main',1)  #1:16
                                #porta entrada
                                self.esperar_selecionar_index('splitter_port_in_3main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_3main',1)
                                #porta saida final
                                self.esperar_selecionar_index('splitter_port_out_3main_final',16)
                                #porta inicial
                                self.esperar_selecionar_index('pdoport_inout_4main',1)
                                #porta final
                                self.esperar_selecionar_index('pdoport_inout_4main_final',16)
                                #ligar
                                self.esperar_clicar_ID('connectButton')
                                #tipo ligador
                                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                                #tipo ligador
                                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                                #confirmar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                print(f'{xpath_mancha}\n,Conectividade feita')
                                sair()
                        except Exception as e:
                            print(e)
                            sg.popup_error('Tem que prestar atenção no cadastro pow\n','Evite conversar\n','Mexer no celular\n', 'Desviar atenção na hora de acionar o programa\n','Reinicie o programa',keep_on_top=True)
                            sair()

                    else:
                        sair()

                elif '8' in capacidade:
                    try:
                        if self.driver.find_element(By.XPATH,'//*[@id="externalArea"]'):
                            #Esperando até seja visivel as Iframe da pagina
                            wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
                    except:
                        break
                    try:
                        #Cenario
                        time.sleep(0.5)
                        wdw.until(element_to_be_clickable((By.ID,'cbScenario')))
                    except:
                        break
                    selecionar = Select(self.driver.find_element(By.ID,'cbScenario'))
                    selecionar.select_by_value('difusion')
                    #spliter
                    time.sleep(.1)
                    wdw.until(element_to_be_clickable((By.ID,'splitter_ratio_inout_2main')))
                    selecionar_1 = self.driver.find_element(By.ID,'splitter_ratio_inout_2main')
                    time.sleep(.05)
                    try:
                        spliter = selecionar_1.find_element(By.XPATH,'//*[@id="splitter_ratio_inout_2main"]/option[2]').get_attribute('text')
                        cabo_inicial = self.driver.find_element(By.XPATH,'//*[@id="cable_inout_1main"]')
                        cabo_1 = cabo_inicial.find_element(By.XPATH,'//*[@id="cable_inout_1main"]/option[2]').get_attribute('text')
                        cabo_final = self.driver.find_element(By.XPATH,'//*[@id="cable_inout_3main"]')
                        cabo_2 = cabo_final.find_element(By.XPATH,'//*[@id="cable_inout_3main"]/option[2]').get_attribute('text')
                    except:
                        sair()
                        continue
                    time.sleep(.05)
                    if cabo_1 == cabo_2:
                        sair()
                        xpath_olho = f'.//*[@id="results"]/tbody/tr[{mancha}]/td[10]/i'
                        time.sleep(2)
                        self.driver.find_element(By.XPATH,xpath_olho).click()
                        time.sleep(0.5)
                        self.driver.switch_to.default_content()
                        #Esperando até seja visivel as Iframe da pagina
                        wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                        wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
                        wdw.until(frame_to_be_available_and_switch_to_it(('id','dados')))
                        time.sleep(2)
                        cdoe_sap = self.driver.find_element(By.ID,'elem_num_sap').get_attribute('value')
                        sair()
                        if cdoe_sap == '331688': #10 tap intermediaria corning
                            try:
                                try:  
                                    try:
                                        self.driver.find_element(By.XPATH,xpath_mancha).click()
                                    except:
                                        print('não consegui clicar')  
                                    self.driver.switch_to.default_content() 
                                    # Esperando até seja visivel as Iframe da pagina
                                    wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                                    wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))    
                                    #cenario
                                    time.sleep(0.5)
                                    self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                                    time.sleep(1.5)
                                    #cabo
                                    self.esperar_selecionar_index('cable_inout_1main',1)
                                    #fibra
                                    self.esperar_selecionar_value('fiber_inout_1main','1')
                                    #spliter
                                    self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1:2
                                    #porta de entrada
                                    self.esperar_selecionar_index('splitter_port_in_2main',1)
                                    #porta saida 
                                    self.esperar_selecionar_index('splitter_port_out_2main',2)
                                    #spliter
                                    self.esperar_selecionar_index('splitter_ratio_inout_3main',2)  #1:8
                                    #porta entrada
                                    self.esperar_selecionar_index('splitter_port_in_3main',1)
                                    #porta saida inicial
                                    self.esperar_selecionar_index('splitter_port_out_3main',1)
                                    #porta saida final
                                    self.esperar_selecionar_index('splitter_port_out_3main_final',8)
                                    #porta inicial
                                    self.esperar_selecionar_index('pdoport_inout_4main',1)
                                    #porta final
                                    self.esperar_selecionar_index('pdoport_inout_4main_final',8)
                                    #ligar
                                    self.esperar_clicar_ID('connectButton')
                                    #tipo ligador
                                    self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                                    #tipo ligador
                                    self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                                    #confirmar
                                    self.esperar_clicar_ID('attributesConfirmButton')
                                    print(f'{xpath_mancha}\n,fim de cabo')
                                    sair()
                                except:
                                    #cenario
                                    time.sleep(0.5)
                                    self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                                    time.sleep(1.5)
                                    #cabo
                                    self.esperar_selecionar_index('cable_inout_1main',1)
                                    #fibra
                                    self.esperar_selecionar_value('fiber_inout_1main','1')
                                    #spliter
                                    self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:2
                                    #porta de entrada
                                    self.esperar_selecionar_index('splitter_port_in_2main',1)
                                    #porta saida 
                                    self.esperar_selecionar_index('splitter_port_out_2main',2)
                                    #spliter
                                    self.esperar_selecionar_index('splitter_ratio_inout_3main',1)  #1:8
                                    #porta entrada
                                    self.esperar_selecionar_index('splitter_port_in_3main',1)
                                    #porta saida inicial
                                    self.esperar_selecionar_index('splitter_port_out_3main',1)
                                    #porta saida final
                                    self.esperar_selecionar_index('splitter_port_out_3main_final',8)
                                    #porta inicial
                                    self.esperar_selecionar_index('pdoport_inout_4main',1)
                                    #porta final
                                    self.esperar_selecionar_index('pdoport_inout_4main_final',8)
                                    #ligar
                                    self.esperar_clicar_ID('connectButton')
                                    #tipo ligador
                                    self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                                    #tipo ligador
                                    self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                                    #confirmar
                                    self.esperar_clicar_ID('attributesConfirmButton')
                                    print(f'{xpath_mancha}\n,fim de cabo')
                                    sair()
                            except:
                                sg.popup_error('Tem que prestar atenção no cadastro pow\n','Evite conversar\n','Mexer no celular\n', 'Desviar atenção na hora de acionar o programa\n','Reinicie o programa',keep_on_top=True)
                            
                        else:
                            try:
                                try:
                                    self.driver.find_element(By.XPATH,xpath_mancha).click()
                                except:
                                    print('não consegui clicar') 
                                # Retorna para a janela principal (fora do iframe)
                                self.driver.switch_to.default_content()
                                self.iframe('iframe-content-wrapper')
                                self.iframe('externalFrame')
                                try:
                                    #cenario
                                    time.sleep(0.5)
                                    self.esperar_selecionar_value('cbScenario','pdo_splitter') #Fibra óptica 1:1 Splitter n:n Porta CDO
                                    time.sleep(2)
                                    #cabo
                                    self.esperar_selecionar_index('cable_inout_1main',1)
                                    #fibra
                                    self.esperar_selecionar_value('fiber_inout_1main','1')
                                    time.sleep(.5)
                                    #spliter
                                    self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1/8
                                    #porta de entrada
                                    self.esperar_selecionar_index('splitter_port_in_2main',1)
                                    #porta saida inicial
                                    self.esperar_selecionar_index('splitter_port_out_2main',1)
                                
                                    #porta final
                                    self.esperar_selecionar_index('splitter_port_out_2main_final','8')
                                    #Fibra Inicial
                                    self.esperar_selecionar_index('pdoport_inout_3main',1)
                                
                                    #porta final
                                    self.esperar_selecionar_index('pdoport_inout_3main_final','8')
                                    #ligar
                                    self.esperar_clicar_ID('connectButton')
                                    time.sleep(.05)
                                    #tipo ligador
                                    self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                                    #confimar
                                    self.esperar_clicar_ID('attributesConfirmButton')
                                    sair()
                                except:
                                    print('não consegui clicar')
                                    sair()
                                print(f'{xpath_mancha}\n,fim de cabo')

                            except:
                                sg.popup_error('Tem que prestar atenção no cadastro pow\n','Evite conversar\n','Mexer no celular\n', 'Desviar atenção na hora de acionar o programa\n','Reinicie o programa',keep_on_top=True)

                    elif spliter == 'S2_1':
                        try:
                            try:
                                #cenario
                                time.sleep(0.5)
                                self.esperar_selecionar_value('cbScenario','difusion') #Fibra óptica 1:1 Splitter n:n Fibra óptica
                                wdw.until(element_to_be_clickable(('id', 'splitter_ratio_inout_2main')))
                                self.esperar_clicar_ID('splitter_ratio_inout_2main')
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','1')
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1:2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_2main',1)
                                #cabo
                                self. esperar_selecionar_index('cable_inout_3main',1)
                                #Fibra Inicial
                                self.esperar_selecionar_index('fiber_inout_3main',1)
                                #ligar
                                self.esperar_clicar_ID('connectButton')
                                #confirmar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                #OK
                                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                                time.sleep(1.5)
                                #cenario
                                self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                                time.sleep(2)
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','1')
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1:2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida 
                                self.esperar_selecionar_index('splitter_port_out_2main',2)
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_3main',2)  #1:8
                                #porta entrada
                                self.esperar_selecionar_index('splitter_port_in_3main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_3main',1)
                                #porta saida final
                                self.esperar_selecionar_index('splitter_port_out_3main_final',8)
                                #porta inicial
                                self.esperar_selecionar_index('pdoport_inout_4main',1)
                                #porta final
                                self.esperar_selecionar_index('pdoport_inout_4main_final',8)
                                #ligar
                                self.esperar_clicar_ID('connectButton')
                                #tipo ligador
                                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                                #tipo ligador
                                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                                #confirmar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                print(f'{xpath_mancha}\n,Conectividade feita')
                                sair()
                            except:
                                #cenario
                                time.sleep(0.5)
                                self.esperar_selecionar_value('cbScenario','difusion') #Fibra óptica 1:1 Splitter n:n Fibra óptica
                                wdw.until(element_to_be_clickable(('id', 'splitter_ratio_inout_2main')))
                                self.esperar_clicar_ID('splitter_ratio_inout_2main')
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','1')
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_2main',1)
                                #cabo
                                self. esperar_selecionar_index('cable_inout_3main',1)
                                #Fibra Inicial
                                self.esperar_selecionar_index('fiber_inout_3main',1)
                                #ligar
                                self.esperar_clicar_ID('connectButton')
                                #confirmar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                #OK
                                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                                time.sleep(1.5)
                                #cenario
                                self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                                time.sleep(2)
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','1')
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida 
                                self.esperar_selecionar_index('splitter_port_out_2main',2)
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_3main',1)  #1:8
                                #porta entrada
                                self.esperar_selecionar_index('splitter_port_in_3main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_3main',1)
                                #porta saida final
                                self.esperar_selecionar_index('splitter_port_out_3main_final',8)
                                #porta inicial
                                self.esperar_selecionar_index('pdoport_inout_4main',1)
                                #porta final
                                self.esperar_selecionar_index('pdoport_inout_4main_final',8)
                                #ligar
                                self.esperar_clicar_ID('connectButton')
                                #tipo ligador
                                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                                #tipo ligador
                                self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                                #confirmar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                print(f'{xpath_mancha}\n,Conectividade feita')
                                sair()
                        except Exception as e:
                            print(e)
                            sg.popup_error('Tem que prestar atenção no cadastro pow\n','Evite conversar\n','Mexer no celular\n', 'Desviar atenção na hora de acionar o programa\n','Reinicie o programa',keep_on_top=True)
                            sair()

                    elif spliter == 'S8_1':
                        try:
                            #cenario
                            time.sleep(0.5)
                            self.esperar_selecionar_value('cbScenario','difusion') #Fibra óptica 1:1 Splitter n:n Fibra óptica
                            wdw.until(element_to_be_clickable(('id', 'splitter_ratio_inout_2main')))
                            self.esperar_clicar_ID('splitter_ratio_inout_2main')
                            #cabo
                            self.esperar_selecionar_index('cable_inout_1main',1)
                            #fibra
                            self.esperar_selecionar_value('fiber_inout_1main','1')
                            #spliter
                            self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:2
                            #porta de entrada
                            self.esperar_selecionar_index('splitter_port_in_2main',1)
                            #porta saida inicial
                            self.esperar_selecionar_index('splitter_port_out_2main',1)
                            #cabo
                            self. esperar_selecionar_index('cable_inout_3main',1)
                            #Fibra Inicial
                            self.esperar_selecionar_index('fiber_inout_3main',1)
                            #ligar
                            self.esperar_clicar_ID('connectButton')
                            #confirmar
                            self.esperar_clicar_ID('attributesConfirmButton')
                            #OK
                            self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                            time.sleep(1.5)
                            #cenario
                            self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                            time.sleep(2)
                            #cabo
                            self.esperar_selecionar_index('cable_inout_1main',1)
                            #fibra
                            self.esperar_selecionar_value('fiber_inout_1main','1')
                            #spliter
                            self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:2
                            #porta de entrada
                            self.esperar_selecionar_index('splitter_port_in_2main',1)
                            #porta saida 
                            self.esperar_selecionar_index('splitter_port_out_2main',2)
                            #spliter
                            self.esperar_selecionar_index('splitter_ratio_inout_3main',1)  #1:8
                            #porta entrada
                            self.esperar_selecionar_index('splitter_port_in_3main',1)
                            #porta saida inicial
                            self.esperar_selecionar_index('splitter_port_out_3main',1)
                            #porta saida final
                            self.esperar_selecionar_index('splitter_port_out_3main_final',8)
                            #porta inicial
                            self.esperar_selecionar_index('pdoport_inout_4main',1)
                            #porta final
                            self.esperar_selecionar_index('pdoport_inout_4main_final',8)
                            #ligar
                            self.esperar_clicar_ID('connectButton')
                            #tipo ligador
                            self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                            #tipo ligador
                            self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                            #confirmar
                            self.esperar_clicar_ID('attributesConfirmButton')
                            print(f'{xpath_mancha}\n,Conectividade feita')
                            sair()  
                        except:
                            #cenario
                            time.sleep(0.5)
                            self.esperar_selecionar_value('cbScenario','difusion') #Fibra óptica 1:1 Splitter n:n Fibra óptica
                            wdw.until(element_to_be_clickable(('id', 'splitter_ratio_inout_2main')))
                            self.esperar_clicar_ID('splitter_ratio_inout_2main')
                            #cabo
                            self.esperar_selecionar_index('cable_inout_1main',1)
                            #fibra
                            self.esperar_selecionar_value('fiber_inout_1main','1')
                            #spliter
                            self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:2
                            #porta de entrada
                            self.esperar_selecionar_index('splitter_port_in_2main',1)
                            #porta saida inicial
                            self.esperar_selecionar_index('splitter_port_out_2main',1)
                            #cabo
                            self. esperar_selecionar_index('cable_inout_3main',1)
                            #Fibra Inicial
                            self.esperar_selecionar_index('fiber_inout_3main',1)
                            #ligar
                            self.esperar_clicar_ID('connectButton')
                            #confirmar
                            self.esperar_clicar_ID('attributesConfirmButton')
                            #OK
                            self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                            time.sleep(1.5)
                            #cenario
                            self.esperar_selecionar_value('cbScenario','doubledifusion_pdo') #Fibra óptica 1:1 Splitter 1:1 Splitter n:n Porta CDO
                            time.sleep(2)
                            #cabo
                            self.esperar_selecionar_index('cable_inout_1main',1)
                            #fibra
                            self.esperar_selecionar_value('fiber_inout_1main','1')
                            #spliter
                            self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #1:2
                            #porta de entrada
                            self.esperar_selecionar_index('splitter_port_in_2main',1)
                            #porta saida 
                            self.esperar_selecionar_index('splitter_port_out_2main',2)
                            #spliter
                            self.esperar_selecionar_index('splitter_ratio_inout_3main',1)  #1:8
                            #porta entrada
                            self.esperar_selecionar_index('splitter_port_in_3main',1)
                            #porta saida inicial
                            self.esperar_selecionar_index('splitter_port_out_3main',1)
                            #porta saida final
                            self.esperar_selecionar_index('splitter_port_out_3main_final',8)
                            #porta inicial
                            self.esperar_selecionar_index('pdoport_inout_4main',1)
                            #porta final
                            self.esperar_selecionar_index('pdoport_inout_4main_final',8)
                            #ligar
                            self.esperar_clicar_ID('connectButton')
                            #tipo ligador
                            self.esperar_selecionar_value('link_LinkConnectionPhysicalType_2','FO.PIGTAIL')
                            #tipo ligador
                            self.esperar_selecionar_value('link_LinkConnectionPhysicalType_3','FO.PIGTAIL')
                            #confirmar
                            self.esperar_clicar_ID('attributesConfirmButton')
                            print(f'{xpath_mancha}\n,Conectividade feita')
                            sair()    
                
                elif '64' in capacidade:
                    try:
                        if self.driver.find_element(By.XPATH,'//*[@id="externalArea"]'):
                            #Esperando até seja visivel as Iframe da pagina
                            wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
                        #cenario
                        time.sleep(1)
                        self.esperar_selecionar_value('cbScenario','pdo_splitter') #Fibra óptica 1:1 Splitter n:n Porta CDO
                        time.sleep(2)
                        #cabo
                        self.esperar_selecionar_index('cable_inout_1main',1)
                        #fibra
                        self.esperar_selecionar_value('fiber_inout_1main','1')
                        time.sleep(.5)
                        #spliter
                        self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1/64
                        #porta de entrada
                        self.esperar_selecionar_index('splitter_port_in_2main',1)
                        #porta saida inicial
                        self.esperar_selecionar_index('splitter_port_out_2main',1)
                        time.sleep(1)
                        opcao = self.driver.find_element(By.ID,'splitter_port_out_2main_final')
                        splitter_s1 = opcao.find_element(By.XPATH,'//*[@id="splitter_ratio_inout_2main"]/option[2]').get_attribute('text')
                        
                        if splitter_s1 == 'S64_1':
                            #spltter de 64
                            #spliter
                            self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #S64_1
                            #porta de entrada
                            self.esperar_selecionar_index('splitter_port_in_2main',1)
                            #porta saida inicial
                            self.esperar_selecionar_index('splitter_port_out_2main',1) 
                            #porta saida final
                            self.esperar_selecionar_index('splitter_port_out_2main_final','64')
                            #Fibra Inicial
                            self.esperar_selecionar_index('pdoport_inout_3main',1)       
                            #porta final
                            self.esperar_selecionar_index('pdoport_inout_3main_final','64')
                            #ligar
                            self.esperar_clicar_ID('connectButton')
                            time.sleep(.05)
                            #tipo ligador
                            self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                            #confimar
                            self.esperar_clicar_ID('attributesConfirmButton')
                            sair()

                        else:
                            try:
                                #####splitter 1 #####
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #S8_1
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_2main',1)   
                                #porta saida final
                                self.esperar_selecionar_index('splitter_port_out_2main_final','8')
                                #Fibra Inicial
                                self.esperar_selecionar_index('pdoport_inout_3main',1)
                                #porta final
                                self.esperar_selecionar_index('pdoport_inout_3main_final','8')
                                #ligar
                                self.esperar_clicar_ID('connectButton')
                                time.sleep(.05)
                                #tipo ligador
                                self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                                #confimar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                time.sleep(.05)
                                #OK
                                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                                sair()
                                time.sleep(1)
                                self.driver.find_element(By.XPATH,xpath_mancha).click()
                                self.driver.switch_to.default_content()
                                #Esperando até seja visivel as Iframe da pagina
                                wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                                wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))

                                #####splitter 2 #####
                                #cenario
                                time.sleep(0.5)
                                self.esperar_selecionar_value('cbScenario','pdo_splitter') #Fibra óptica 1:1 Splitter n:n Porta CDO
                                time.sleep(2)
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','2')
                                time.sleep(.5)
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #S8_2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_2main',1)   
                                #porta saida final
                                self.esperar_selecionar_index('splitter_port_out_2main_final','8')
                                try:
                                    #Fibra Inicial
                                    self.esperar_selecionar_index('pdoport_inout_3main',9)
                                    #porta final
                                    self.esperar_selecionar_index('pdoport_inout_3main_final','16')
                                except:
                                    sair()
                                time.sleep(1.5)
                                #ligar
                                self.esperar_clicar_xpath('//*[@id="connectButton"]')
                                time.sleep(.05)
                                #tipo ligador
                                self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                                #confimar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                time.sleep(.05)
                                #OK
                                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                                sair()
                                time.sleep(1)
                                self.driver.find_element(By.XPATH,xpath_mancha).click()
                                self.driver.switch_to.default_content()
                                #Esperando até seja visivel as Iframe da pagina
                                wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                                wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
                                
                                #####splitter 3 #####
                                #cenario
                                time.sleep(0.5)
                                self.esperar_selecionar_value('cbScenario','pdo_splitter') #Fibra óptica 1:1 Splitter n:n Porta CDO
                                time.sleep(2)
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','3')
                                time.sleep(.5)
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',3) #S8_2
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_2main',1)   
                                #porta saida final
                                self.esperar_selecionar_index('splitter_port_out_2main_final','8')
                                try:
                                    #Fibra Inicial
                                    self.esperar_selecionar_index('pdoport_inout_3main',17)
                                    #porta final
                                    self.esperar_selecionar_index('pdoport_inout_3main_final','24')
                                except:
                                    sair()
                                time.sleep(1.5)
                                #ligar
                                self.esperar_clicar_xpath('//*[@id="connectButton"]')
                                time.sleep(.05)
                                #tipo ligador
                                self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                                #confimar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                time.sleep(.05)
                                #OK
                                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                                sair()
                                time.sleep(1)
                                self.driver.find_element(By.XPATH,xpath_mancha).click()
                                self.driver.switch_to.default_content()
                                #Esperando até seja visivel as Iframe da pagina
                                wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                                wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))

                                #####splitter 4 #####
                                #cenario
                                time.sleep(0.5)
                                self.esperar_selecionar_value('cbScenario','pdo_splitter') #Fibra óptica 1:1 Splitter n:n Porta CDO
                                time.sleep(2)
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','4')
                                time.sleep(.5)
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',4) #S8_4
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_2main',1)   
                                #porta saida final
                                self.esperar_selecionar_index('splitter_port_out_2main_final','8')
                                try:
                                    #Fibra Inicial
                                    self.esperar_selecionar_index('pdoport_inout_3main',25)
                                    #porta final
                                    self.esperar_selecionar_index('pdoport_inout_3main_final','32')
                                except:
                                    sair()
                                time.sleep(1.5)
                                #ligar
                                self.esperar_clicar_xpath('//*[@id="connectButton"]')
                                time.sleep(.05)
                                #tipo ligador
                                self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                                #confimar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                time.sleep(.05)
                                #OK
                                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                                sair()
                                time.sleep(1)
                                self.driver.find_element(By.XPATH,xpath_mancha).click()
                                self.driver.switch_to.default_content()
                                #Esperando até seja visivel as Iframe da pagina
                                wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                                wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
                                
                                #####splitter 5 #####
                                #cenario
                                time.sleep(0.5)
                                self.esperar_selecionar_value('cbScenario','pdo_splitter') #Fibra óptica 1:1 Splitter n:n Porta CDO
                                time.sleep(2)
                                #cabo
                                self.esperar_selecionar_index('cable_inout_1main',1)
                                #fibra
                                self.esperar_selecionar_value('fiber_inout_1main','5')
                                time.sleep(.5)
                                #spliter
                                self.esperar_selecionar_index('splitter_ratio_inout_2main',5) #S8_5
                                #porta de entrada
                                self.esperar_selecionar_index('splitter_port_in_2main',1)
                                #porta saida inicial
                                self.esperar_selecionar_index('splitter_port_out_2main',1)   
                                #porta saida final
                                self.esperar_selecionar_index('splitter_port_out_2main_final','8')
                                try:
                                    #Fibra Inicial
                                    self.esperar_selecionar_index('pdoport_inout_3main',33)
                                    #porta final
                                    self.esperar_selecionar_index('pdoport_inout_3main_final','40')
                                except:
                                    sair()
                                time.sleep(1.5)
                                #ligar
                                self.esperar_clicar_xpath('//*[@id="connectButton"]')
                                time.sleep(.05)
                                #tipo ligador
                                self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                                #confimar
                                self.esperar_clicar_ID('attributesConfirmButton')
                                time.sleep(.05)
                                #OK
                                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')
                                sair()
                                time.sleep(1)
                                self.driver.find_element(By.XPATH,xpath_mancha).click()
                                self.driver.switch_to.default_content()
                                #Esperando até seja visivel as Iframe da pagina
                                wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                                wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))

                            except Exception as e:
                                print(e)
                                sg.popup_error('Tem que prestar atenção no cadastro pow\n','Evite conversar\n','Mexer no celular\n', 'Desviar atenção na hora de acionar o programa\n','Reinicie o programa',keep_on_top=True)
                                sair()
                                
                    except Exception as e:
                        print(e)
                        sg.popup_error('Tem que prestar atenção no cadastro pow\n','Evite conversar\n','Mexer no celular\n', 'Desviar atenção na hora de acionar o programa\n','Reinicie o programa',keep_on_top=True)
                        sair()
                else:
                    sair()
            else:
                sair()        
    
    def operacoes_mud_est(self,id_sicon,projeto=True,botao=True):
        wdw = WebDriverWait(self.driver, 1)
        self.driver.implicitly_wait(.05)
        try:
            try:  
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="operational-module-osp"]')))    
                self.driver.find_element(By.XPATH,'//*[@id="operational-module-osp"]').click()
                time.sleep(1.3)
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="operation-module-link-osp-2-0"]')))    
                self.driver.find_element(By.XPATH,'//*[@id="operation-module-link-osp-2-0"]').click()
            except:
                pass

            self.iframe('iframe-content-wrapper')
            self.iframe('elementSearchFrame')
            wdw.until(element_to_be_clickable(('xpath', '//*[@id="searchForm"]/table[*]/tbody/tr/td/div/div/div[1]')))
            operacao = self.driver.find_element(By.XPATH,'//*[@id="searchForm"]/table[*]/tbody/tr/td/div/div/div[1]').text
            if operacao and projeto:
                #operações
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="operationSelected"]')))
                Select(self.driver.find_element(By.XPATH,'//*[@id="operationSelected"]')).select_by_index(2)
                time.sleep(1)
                #id sicon
                self.esperar_xpath_txt('//*[@id="idsicom"]',id_sicon)
                #pesquisar
                self.esperar_clicar_xpath('//*[@id="formContainer"]/table/tbody/tr[*]/td/div/div[3]/a/span')
            else:
                #sg.popup_error('Ainda não faro',keep_on_top=True)
                #operações
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="operationSelected"]')))
                Select(self.driver.find_element(By.XPATH,'//*[@id="operationSelected"]')).select_by_index(2)
                time.sleep(1)
                #projeto
                wdw.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="codigoProj"]')))
                self.driver.find_element(By.XPATH,'//*[@id="codigoProj"]').click()
                time.sleep(.5)
                self.driver.find_element(By.XPATH,'//*[@id="codigoProj"]').send_keys(id_sicon)
                time.sleep(.5)
                self.driver.find_element(By.XPATH,'//*[@id="codigoProj"]').send_keys(Keys.ENTER)
            
        except:
            print('deu erro ae')
        # Retorna para a janela principal (fora do iframe)
        self.driver.switch_to.default_content()
    
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
    
    def preencher_form(self, descricao, conectada, quantidade, denovo='True', primario=True):
        self.driver.implicitly_wait(.05)
        wdw = WebDriverWait(self.driver, 30)
        with open("credenciais.json", encoding='utf-8') as meu_json:
                dado = json.load(meu_json)
        try:      
            if denovo:   
                self.driver.get('https://forms.office.com/pages/responsepage.aspx?id=MuENFAeIYEyrkDA2RpBAQqODTOU3hFJOjWuPUZz-qlpUMUlYVDlKMjhEQkZTTk5IOTVERlhRTzczVi4u')
                time.sleep(1)
                #preencher email
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="i0116"]')))
                self.driver.find_element(By.XPATH,'//*[@id="i0116"]').clear()
                self.driver.find_element(By.XPATH,'//*[@id="i0116"]').send_keys(dado['email'])
                time.sleep(.5)
                #clicar no avançar
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="idSIButton9"]')))
                self.driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
                time.sleep(1)
                #senha
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="i0118"]')))
                self.driver.find_element(By.XPATH,'//*[@id="i0118"]').clear()
                self.driver.find_element(By.XPATH,'//*[@id="i0118"]').send_keys(dado['senha_email'])
                #clicar entrar
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="idSIButton9"]')))
                self.driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
                time.sleep(1)
                #sim
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="idSIButton9"]')))
                self.driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
                if primario:
                    #1 cadastro netwin
                    wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[*]/div[*]/div[*]/div/div/div[*]/div/div[2]/div/label/input')))
                    self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[*]/div[*]/div[*]/div/div/div[*]/div/div[2]/div/label/input').click()

                    #3 etapa concluida
                    wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[*]/div[*]/div[*]/div[3]/div/div[*]/div/div[3]/div/label/input')))
                    self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[*]/div[*]/div[*]/div[3]/div/div[*]/div/div[3]/div/label/input').click()
                    
                    #enviar por email
                    time.sleep(2)
                    wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div/div/label/input')))
                    self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div/div/label/input').click()
                    time.sleep(1)
                else:
                    #1 cadastro netwin
                    wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[*]/div[*]/div[*]/div/div/div[*]/div/div[2]/div/label/input')))
                    self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[*]/div[*]/div[*]/div/div/div[*]/div/div[2]/div/label/input').click()

                    #3 etapa concluida
                    wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[*]/div[*]/div[*]/div[3]/div/div[*]/div/div[2]/div/label/input')))
                    self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[*]/div[*]/div[*]/div[3]/div/div[*]/div/div[2]/div/label/input').click()
                    
                    #enviar por email
                    time.sleep(2)
                    wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div/div/label/input')))
                    self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div/div/label/input').click()
                    time.sleep(1)
            else:
                pass
            if primario:
                #2 descrição
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input')))
                self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').clear()
                self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys(descricao)
                time.sleep(.5)

                #4 CELULA CONECTADA
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input')))
                self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').clear()
                self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys(conectada)
                time.sleep(.5)

                #5 INFORME A QUANTIDADE DE CÉLULAS
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div/input')))
                self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div/input').clear()
                self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div/input').send_keys(quantidade)
                time.sleep(.5)

                #enviar 
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[4]/div[1]/button/div')))
                self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[4]/div[1]/button/div').click()
            else:
                #2 descrição
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input')))
                self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').clear()
                self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input').send_keys(descricao)
                time.sleep(.5)

                #4 CELULA CONECTADA
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input')))
                self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').clear()
                self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys(conectada)
                time.sleep(.5)

                #enviar 
                wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[4]/div[1]/button/div')))
                self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[4]/div[1]/button/div').click()

            time.sleep(2)
            #enviar outra resposta
            wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[2]/div[2]/div[2]/a')))
            self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[2]/div[2]/div[2]/a').click()

            #1 cadastro netwin
            wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[*]/div[*]/div[*]/div/div/div[*]/div/div[2]/div/label/input')))
            self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[*]/div[*]/div[*]/div/div/div[*]/div/div[2]/div/label/input').click()

            #3 etapa concluida
            wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[*]/div[*]/div[*]/div[3]/div/div[*]/div/div[2]/div/label/input')))
            self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[*]/div[*]/div[*]/div[3]/div/div[*]/div/div[2]/div/label/input').click()
                
            #enviar por email
            time.sleep(2)
            wdw.until(element_to_be_clickable(('xpath', '//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div/div/label/input')))
            self.driver.find_element(By.XPATH,'//*[@id="form-main-content"]/div/div[1]/div[2]/div[3]/div/div/label/input').click()
            time.sleep(1)

            lol = None
            infra = f'INFORMAÇÕES DO CADASTRO DE INFRA\nCÉLULA:{lol}\nID SICOM:{lol}\nTOTAL DE HPS:{lol}\nOBS:{lol}'
                     
            mail = dado['email']
            print(f'Formulario enviado\nCopia enviada para o email:\n{mail}')
           
        except:
            sg.popup_error(f'Ixi deu um erro ae O_O',keep_on_top=True)

    def conectividade_cdoi_avulsa(self,elemento=True):
        self.driver.implicitly_wait(.05)
        wdw = WebDriverWait(self.driver, 5)
        self.iframe('iframe-content-wrapper')
        self.iframe('externalFrame') 

        def sair():
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()
            wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
            time.sleep(0.5)
            #fechar
            self.esperar_xpath('.//span[@class="ui-icon ui-icon-closethick"]')
            wdw.until(frame_to_be_available_and_switch_to_it(('id','elementSearchFrame')))

        if elemento:
            #cenario
            time.sleep(0.5)
            self.esperar_selecionar_value('cbScenario','pdo_splitter') #Fibra óptica 1:1 Splitter n:n Porta CDO
            time.sleep(2)
            #cabo
            self.esperar_selecionar_index('cable_inout_1main',1)
            #fibra
            self.esperar_selecionar_value('fiber_inout_1main','1')
            time.sleep(.5)
            #spliter
            self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #1/64
            #porta de entrada
            self.esperar_selecionar_index('splitter_port_in_2main',1)
            #porta saida inicial
            self.esperar_selecionar_index('splitter_port_out_2main',1)
                                
            #porta saida final
            self.esperar_selecionar_index('splitter_port_out_2main_final','64')
            #Fibra Inicial
            self.esperar_selecionar_index('pdoport_inout_3main',1)
                                
            #porta final
            self.esperar_selecionar_index('pdoport_inout_3main_final','64')
            #ligar
            self.esperar_clicar_ID('connectButton')
            time.sleep(.05)
            #tipo ligador
            self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
            #confimar
            self.esperar_clicar_ID('attributesConfirmButton')
            sair()
        else:
            try:
                #####splitter 1 #####
                #cenario
                time.sleep(0.5)
                self.esperar_selecionar_value('cbScenario','pdo_splitter') #Fibra óptica 1:1 Splitter n:n Porta CDO
                time.sleep(1.2)
                #cabo
                self.esperar_selecionar_index('cable_inout_1main',1)
                #fibra
                self.esperar_selecionar_value('fiber_inout_1main','1')
                time.sleep(.5)
                #spliter
                self.esperar_selecionar_index('splitter_ratio_inout_2main',1) #S8_1
                #porta de entrada
                self.esperar_selecionar_index('splitter_port_in_2main',1)
                #porta saida inicial
                self.esperar_selecionar_index('splitter_port_out_2main',1)            
                #porta saida final
                self.esperar_selecionar_index('splitter_port_out_2main_final','8')
                #Fibra Inicial
                self.esperar_selecionar_index('pdoport_inout_3main',1)            
                #porta final
                self.esperar_selecionar_index('pdoport_inout_3main_final','8')
                #ligar
                self.esperar_clicar_ID('connectButton')
                time.sleep(.05)
                #tipo ligador
                self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                #confimar
                self.esperar_clicar_ID('attributesConfirmButton')
                time.sleep(.05)
                #OK
                self.esperar_xpath('//*[@class="linkbutton no-image confirm button"]')

                #####splitter 2 #####
                #fibra
                self.esperar_selecionar_value('fiber_inout_1main','2')
                time.sleep(.5)
                #spliter
                self.esperar_selecionar_index('splitter_ratio_inout_2main',2) #S8_2
                #porta de entrada
                self.esperar_selecionar_index('splitter_port_in_2main',1)
                #porta saida inicial
                self.esperar_selecionar_index('splitter_port_out_2main',1)
                #porta saida final
                self.esperar_selecionar_index('splitter_port_out_2main_final','8')
                #Fibra Inicial
                self.esperar_selecionar_index('pdoport_inout_3main',9)
                #porta final
                self.esperar_selecionar_index('pdoport_inout_3main_final','16')
                #ligar
                self.esperar_clicar_ID('connectButton')
                time.sleep(.05)
                #tipo ligador
                self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                #confimar
                self.esperar_clicar_ID('attributesConfirmButton')
                time.sleep(1)
                wdw.until(EC.element_to_be_clickable(('xpath', '//*[@class="linkbutton no-image confirm button"]')))
                #confirmar
                self.driver.find_element(By.XPATH,'//*[@class="linkbutton no-image confirm button"]').click()

                #####splitter 3 #####
                #fibra
                self.esperar_selecionar_value('fiber_inout_1main','3')
                time.sleep(.5)
                #spliter
                self.esperar_selecionar_index('splitter_ratio_inout_2main',3) #S8_2
                #porta de entrada
                self.esperar_selecionar_index('splitter_port_in_2main',1)
                #porta saida inicial
                self.esperar_selecionar_index('splitter_port_out_2main',1)
                #porta saida final
                self.esperar_selecionar_index('splitter_port_out_2main_final','8')
                #Fibra Inicial
                self.esperar_selecionar_index('pdoport_inout_3main',17)
                #porta final
                self.esperar_selecionar_index('pdoport_inout_3main_final','24')
                #ligar
                self.esperar_clicar_ID('connectButton')
                time.sleep(.05)
                #tipo ligador
                self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                #confimar
                self.esperar_clicar_ID('attributesConfirmButton')
                time.sleep(1)
                wdw.until(EC.element_to_be_clickable(('xpath', '//*[@class="linkbutton no-image confirm button"]')))
                #confirmar
                self.driver.find_element(By.XPATH,'//*[@class="linkbutton no-image confirm button"]').click()


                #####splitter 4 #####
                #fibra
                self.esperar_selecionar_value('fiber_inout_1main','4')
                time.sleep(.5)
                #spliter
                self.esperar_selecionar_index('splitter_ratio_inout_2main',4) #S8_2
                #porta de entrada
                self.esperar_selecionar_index('splitter_port_in_2main',1)
                #porta saida inicial
                self.esperar_selecionar_index('splitter_port_out_2main',1)  
                #porta saida final
                self.esperar_selecionar_index('splitter_port_out_2main_final','8')
                #Fibra Inicial
                self.esperar_selecionar_index('pdoport_inout_3main',25)
                #porta final
                self.esperar_selecionar_index('pdoport_inout_3main_final','32')
                #ligar
                self.esperar_clicar_ID('connectButton')
                time.sleep(.05)
                #tipo ligador
                self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                #confimar
                self.esperar_clicar_ID('attributesConfirmButton')
                time.sleep(1)
                wdw.until(EC.element_to_be_clickable(('xpath', '//*[@class="linkbutton no-image confirm button"]')))
                #confirmar
                self.driver.find_element(By.XPATH,'//*[@class="linkbutton no-image confirm button"]').click()


                #####splitter 5 #####
                #fibra
                self.esperar_selecionar_value('fiber_inout_1main','4')
                time.sleep(.5)
                #spliter
                self.esperar_selecionar_index('splitter_ratio_inout_2main',5) #S8_2
                #porta de entrada
                self.esperar_selecionar_index('splitter_port_in_2main',1)
                #porta saida inicial
                self.esperar_selecionar_index('splitter_port_out_2main',1)  
                #porta saida final
                self.esperar_selecionar_index('splitter_port_out_2main_final','8')
                #Fibra Inicial
                self.esperar_selecionar_index('pdoport_inout_3main',33)
                #porta final
                self.esperar_selecionar_index('pdoport_inout_3main_final','42')
                #ligar
                self.esperar_clicar_ID('connectButton')
                time.sleep(.05)
                #tipo ligador
                self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                #confimar
                self.esperar_clicar_ID('attributesConfirmButton')
                time.sleep(1)
                wdw.until(EC.element_to_be_clickable(('xpath', '//*[@class="linkbutton no-image confirm button"]')))
                #confirmar
                self.driver.find_element(By.XPATH,'//*[@class="linkbutton no-image confirm button"]').click()

                #####splitter 6 #####
                #fibra
                self.esperar_selecionar_value('fiber_inout_1main','4')
                time.sleep(.5)
                #spliter
                self.esperar_selecionar_index('splitter_ratio_inout_2main',6) #S8_2
                #porta de entrada
                self.esperar_selecionar_index('splitter_port_in_2main',1)
                #porta saida inicial
                self.esperar_selecionar_index('splitter_port_out_2main',1)  
                #porta saida final
                self.esperar_selecionar_index('splitter_port_out_2main_final','8')
                #Fibra Inicial
                self.esperar_selecionar_index('pdoport_inout_3main',43)
                #porta final
                self.esperar_selecionar_index('pdoport_inout_3main_final','51')
                #ligar
                self.esperar_clicar_ID('connectButton')
                time.sleep(.05)
                #tipo ligador
                self.esperar_selecionar_ID('link_LinkConnectionPhysicalType_2','FO.PIGTAIL') #pigtail
                #confimar
                self.esperar_clicar_ID('attributesConfirmButton')
                time.sleep(1)
                wdw.until(EC.element_to_be_clickable(('xpath', '//*[@class="linkbutton no-image confirm button"]')))
                #confirmar
                self.driver.find_element(By.XPATH,'//*[@class="linkbutton no-image confirm button"]').click()

            except Exception as e:
                print(e)
                sair()  
        
        # Retorna para a janela principal (fora do iframe)
        self.driver.switch_to.default_content()

    def abastecimento_completa_cdoi(self,iframe=True):
        self.driver.implicitly_wait(.05)
        wdw = WebDriverWait(self.driver, 30)
        
        if iframe:
            # Esperando até seja visivel as Iframe da pagina
            wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
            wdw.until(frame_to_be_available_and_switch_to_it(('id','elementSearchFrame')))
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
            time.sleep(.05)
            xpath_linha = f'.//*[@id="results"]/tbody/tr[{mancha}]'
            xpath_capacidade = '/td[4]'
            time.sleep(1)
            xpath_mancha = f'.//*[@id="results"]/tbody/tr[{mancha}]/td[12]/i'
            try:
                capacidade = self.driver.find_element(By.XPATH,xpath_linha + xpath_capacidade ).text
                time.sleep(1)
                self.driver.find_element(By.XPATH,xpath_mancha).click()
            except:
                print('Não encontrei a linha para fazer a conectividade :)')
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content()
                break
            time.sleep(1)
            #espera até o elemento esteja presente na DOM
            if self.driver.find_element(By.XPATH,xpath_linha):
                self.driver.switch_to.default_content()
                #Esperando até seja visivel as Iframe da pagina
                wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                if capacidade == '64':
                    try:
                        if self.driver.find_element(By.XPATH,'//*[@id="externalArea"]'):
                            #Esperando até seja visivel as Iframe da pagina
                            wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
                    except:
                        break
                    time.sleep(1)
                    self.driver.find_element(By.XPATH,'//*[@id="influenceAreaButton"]').click()
                    wdw.until(element_to_be_clickable(('xpath', ".//table[@class='connectionsTable']/tbody/tr[1]/td[1]/a")))
                    self.driver.find_element(By.XPATH,".//table[@class='connectionsTable']/tbody/tr[1]/td[1]/a").click()
                    time.sleep(1)
                    sair()
                else:    
                    sair()
            else:
                sair()

    def poste_traçado(self):
        def coordenada():
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
            x, y = pt.position()
            time.sleep(2)

            pt.click(x,y)
            time.sleep(1)
            pt.rightClick(x,y)


            print(x,y)

        coordenada()

        

if __name__ == "__main__": 
    #navegador = Internet()
    #navegador.navegador_driver(False,True,False)
    #navegador.entrar_driver()
    sg.theme('Reddit')
    sg.popup_error(f'ta no arquivo algoritimo pow',keep_on_top=True)