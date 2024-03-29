from check_tr import check_tr
from bibliotecas import *

check_tr()

sg.popup_notify(f'Carregando biblioteca...')

esperar = time.sleep(.05)
esperar1 = time.sleep(1)
esperar2 = time.sleep(2)
esperar3 = time.sleep(.01)
esperar4 = time.sleep(3)
esperar5 = time.sleep(3.5)

class Internet:
    def __init__(self):
        pass
    def navegador_driver(self,usar_edge=True,usar_chrome=True,usar_Iexplorer=True,usar_interno=True):
        # Verifica qual browser será utilizado e inicia o serviço correspondente
        if usar_edge: 
            service = EdgeService()
            #self.driver = Edge(executable_path=EdgeDriverManager().install())
        elif usar_chrome: 
            self.driver = Chrome(executable_path=ChromeDriverManager().install())
        elif usar_Iexplorer: 
            service = IEService()
            self.driver = Ie(executable_path=IEDriverManager().install())
        else: 
            self.driver = Firefox(executable_path=GeckoDriverManager().install())
        # Maximiza a janela do navegador  
        self.driver.maximize_window()
        # Abre a página inicial do sistema
        if usar_interno: #interno
            self.driver.get("http://netwin-vtal.interno/")
        else: #externo
            self.driver.get("http://netwin.intranet/")
        # Define um tempo de espera implícito para aguardar a página carregar completamente
        self.driver.implicitly_wait(20)
       
    def entrar_driver(self, login = True):
        # Espera por até 60 segundos para a página carregar completamente
        wdw = WebDriverWait(self.driver, 60)
        # Carrega as credenciais a partir do arquivo "credenciais.json"
        with open("credenciais.json", encoding='utf-8') as meu_json:
            dado = json.load(meu_json)
        # Define uma função para preencher os campos de login e senha    
        def preencher_campo(elemento,texto):
            # Espera até que o elemento esteja clicável
            wdw.until(element_to_be_clickable(('id', elemento)))
            # Seleciona o campo de texto
            campo = self.driver.find_element(By.ID, elemento)
            # Limpa o campo de texto
            campo.clear()
            # Insere o texto no campo
            campo.send_keys(texto)
            
        # Preenche o campo de login e o campo de senha    
        preencher_campo('inputLogin',dado['login'])
        preencher_campo('inputPassword',dado['senha'])
       
    def esperar_clicar_ID(self,elemento):
        try:
            wdw = WebDriverWait(self.driver, 60)
            wdw.until(EC.element_to_be_clickable(('id', elemento)))
            self.driver.find_element(By.ID,elemento).click()
        except:
            pass

    def esperar_clicar_xpath(self,elemento):
        try:
            wdw = WebDriverWait(self.driver, 60)
            wdw.until(EC.element_to_be_clickable((By.XPATH, elemento)))
            self.driver.find_element(By.XPATH,elemento).click()
        except:
            pass
    
    def esperar_txt_ID(self,elemento, txt):
        try:
            wdw = WebDriverWait(self.driver, 60)    
            wdw.until(element_to_be_clickable(('id', elemento)))
            self.driver.find_element(By.ID,elemento).clear()
            self.driver.find_element(By.ID,elemento).send_keys(txt)
        except:
            pass

    def esperar_link_txt(self,elemento):
        try:
            wdw = WebDriverWait(self.driver, 60)
            wdw.until(element_to_be_clickable(('link text', elemento))) 
            self.driver.find_element(By.LINK_TEXT,elemento).click()
        except:
            pass

    def esperar_selecionar_ID(self,elemento, value):
        try:
            wdw = WebDriverWait(self.driver, 60)
            wdw.until((element_to_be_clickable(('id', elemento))))
            selecionar = Select(self.driver.find_element(By.ID,elemento))
            esperar
            selecionar.select_by_value(value)
        except:
            pass

    def esperar_selecionar_value(self,elemento, value):
        try:
            wdw = WebDriverWait(self.driver, 60)
            wdw.until((element_to_be_clickable(('id', elemento))))
            selecionar = Select(self.driver.find_element(By.ID,elemento))
            esperar
            selecionar.select_by_value(value)
        except:
            pass

    def esperar_selecionar_value_xpath(self,elemento, value):
        try:
            wdw = WebDriverWait(self.driver, 60)
            wdw.until((element_to_be_clickable(('xpath', elemento))))
            selecionar = Select(self.driver.find_element(By.ID,elemento))
            esperar
            selecionar.select_by_value(value)
        except:
            pass
    
    def esperar_selecionar_ID_txt(self,elemento,txt):
        try:
            wdw = WebDriverWait(self.driver, 60)
            wdw.until(element_to_be_clickable(('id', elemento)))
            self.driver.find_element(By.ID,elemento).clear()
            self.driver.find_element(By.ID,elemento).send_keys(txt)
            esperar2
            self.driver.find_element(By.ID,elemento).send_keys(Keys.ENTER)
        except:
            pass
        
    def iframe(self,elemento):
        try:
            wdw = WebDriverWait(self.driver, 60)
            wdw.until(frame_to_be_available_and_switch_to_it((
                'id',elemento)))
        except:
            sg.popup_error('i carai\nnem encontrou oque vc queria, tem que reiniciar o programa',keep_on_top=True)   
            exit()

    def esperar_xpath_txt(self,elemento,txt):
        try:
            wdw = WebDriverWait(self.driver, 60)
            wdw.until(element_to_be_clickable(('xpath', elemento)))    
            time.sleep(.15)
            self.driver.find_element(By.XPATH,elemento).clear()
            self.driver.find_element(By.XPATH,elemento).send_keys(txt)
        except:
            pass
    
    def esperar_selecionar_index(self,elemento,num):
        try:
            wdw = WebDriverWait(self.driver, 60)
            wdw.until(element_to_be_clickable(('id', elemento)))
            selecionar = Select(self.driver.find_element(By.ID,elemento))
            selecionar.select_by_index(num)
        except:
            pass

    def esperar_xpath(self,elemento):
        try:
            wdw = WebDriverWait(self.driver, 60)
            wdw.until(element_to_be_clickable(('xpath', elemento)))    
            esperar
            self.driver.find_element(By.XPATH,elemento).click()
        except:
            pass

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

    def cdoe_precon(self,id_sicon,estação,numero,est=True,confirmar=True,frame=True,sap=True,sap_1=True,campo=True,tbd=True,projeto=True):
        
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
            if objeto_aereo == '    CDOE' or objeto_aereo == 'CDOE':
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
                    self.esperar_xpath_txt('//*[@id="nomecNumber"]', numero)
                else:
                    #tbd
                    self.esperar_clicar_xpath('//*[@id="outOfPattern_check"]') #fora de padrão
                    time.sleep(1)
                    self.esperar_xpath('//*[@id="onPatternTag"]')
                    '''
                    time.sleep(1)
                    etiqueta_padrao = self.driver.find_element(By.XPATH,'//*[@id="onPatternTag"]').text()
                    '''
                    time.sleep(.5)
                    self.esperar_xpath_txt('//*[@id="tagOnField"]','CDOE-'+ numero +'-TBD')
                    self.esperar_xpath_txt('//*[@id="nomecNumber"]', '0')

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

    def cdoe_precon_2022(self,id_sicon,estação,numero,est=True,confirmar=True,frame=True,precom_rs=True,tbd=True,projeto=True,):
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
            print(objeto_aereo)

            if objeto_aereo == 'CDOE' or objeto_aereo == '    CDOE':
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
                    self.esperar_xpath_txt('//*[@id="nomecNumber"]', numero)
                else:
                    #tbd
                    self.esperar_clicar_xpath('//*[@id="outOfPattern_check"]') #fora de padrão
                    time.sleep(1)
                    self.esperar_xpath('//*[@id="onPatternTag"]')
                    '''
                    time.sleep(1)
                    etiqueta_padrao = self.driver.find_element(By.XPATH,'//*[@id="onPatternTag"]').text()
                    '''
                    time.sleep(.5)
                    self.esperar_xpath_txt('//*[@id="tagOnField"]','CDOE-'+ numero +'-TBD')
                    self.esperar_xpath_txt('//*[@id="nomecNumber"]', '0')

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
           
    def componentes(self,modelo=True):
            self.iframe('iframe-content-wrapper')
            self.iframe('externalIspIframe')
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
            self.iframe('externalIspIframe')
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
                
                #etiqueta de campo
                if cap == None:
                    pass
                else:
                    if cap == '':
                        fornecedor =  poste 
                    else:
                        fornecedor =  poste ,  '-'  , cap
                    time.sleep(.5)
                    self.esperar_xpath_txt('//*[@id="location_input_etiquetaEmCampo"]', fornecedor )

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

                #localização
                self.esperar_xpath('//*[@id="location_tab_localization"]')
                
                sg.popup_no_buttons('Confere a localização antes de guardar dmr\nTMJ!',keep_on_top='True')

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
                 
    def ler_pdf(self):
        dataframe = pd.read_excel('Loc_Est_RMS.xlsx', index_col=0,usecols="D,E") 
        for i in dataframe:
            pass

    def abastecimento(self,hp,iframe=True):
        try:
            self.driver.implicitly_wait(5)
            wdw = WebDriverWait(self.driver, .1)
            if iframe:
                # Esperando até seja visivel as Iframe da pagina
                wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                wdw.until(frame_to_be_available_and_switch_to_it(('id','externalFrame')))
            else:
                # Esperando até seja visivel as Iframe da pagina
                wdw.until(frame_to_be_available_and_switch_to_it(('id','iframe-content-wrapper')))
                wdw.until(frame_to_be_available_and_switch_to_it(('id','externalConnectivityIframe'))) 

            #ir para aba de abastecimento
            wdw.until(EC.element_to_be_clickable((By.ID, 'influenceAreaButton'))).click()
            
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
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()
         
    def encontrar_projetado(self):
        self.iframe('iframe-content-wrapper')
        self.iframe('elementSearchFrame')
        tabela = self.driver.find_elements(By.ID,'results')
        for i in tabela:
            if 'Projetado' in i.text:
                self.driver.find_element(By.ID,'results').get_property
            else:
                print('nem encontrei')

    def hub_box_p(self,id_sicon,estacao,numero, hub_box=True,projeto=True):
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
            if projeto:
                #Id-sicon
                self.esperar_txt_ID('id_sicom_name',id_sicon)
                self.esperar_xpath('//li[@class="ac_even ac_over"]')
            else:
                #nome projeto
                self.esperar_txt_ID('projecto_name',id_sicon)
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

    def cdoi(self,id_sicon,estacao,topologia=True,id_projeto=True):
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
            if id_projeto:
                #Id-sicon
                self.esperar_txt_ID('id_sicom_name',id_sicon)
                self.esperar_xpath('//li[@class="ac_even ac_over"]')
            else:
                #Nome projeto
                self.esperar_txt_ID('projecto_name',id_sicon)
                self.esperar_xpath('/html/body/div[*]/ul/li/strong')

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
                                try:
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
                                except:
                                    sg.popup_error('Esqueceu de colocar cabo e splitter pow\n','Reinicie o programa',keep_on_top=True)
                                    pass

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
                                try:
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
                                except:
                                    pass
                                    
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
                                try:
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
                                except:
                                    pass

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
                                try:
                                    #spliter
                                    self.esperar_selecionar_index('splitter_ratio_inout_2main',4) #S8_4
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
                                except:
                                    pass

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
                                try:
                                    #spliter
                                    self.esperar_selecionar_index('splitter_ratio_inout_2main',5) #S8_5
                                    #porta de entrada
                                    self.esperar_selecionar_index('splitter_port_in_2main',1)
                                    #porta saida inicial
                                    self.esperar_selecionar_index('splitter_port_out_2main',1)   
                                    #porta saida final
                                    self.esperar_selecionar_index('splitter_port_out_2main_final','8')
                                    #Fibra Inicial
                                    self.esperar_selecionar_index('pdoport_inout_3main',33)
                                    #porta final
                                    self.esperar_selecionar_index('pdoport_inout_3main_final','40')
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

                                except:
                                    sair()

                            except Exception as e:
                                print(e)
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
        email = dado['email']
        for i in dado:
            if email == 'klayton.dias@telemontrms.com.br':
                sg.popup('tem que alterar la no none de utilizador \nemail: xxxxx@telemont.com.br\nsenha: xxxxx ', keep_on_top=True)
                break
            
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

    def poste_inicio(self):
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
        #iframe
        self.iframe('iframe-content-wrapper')
        #Modificar atributos
        self.esperar_clicar_xpath('//*[@id="paneldiv"]/div[23]')
        #Quebrar traçado
        self.esperar_clicar_xpath('//*[@id="olControlSplitRouteOi"]')
        time.sleep(1)
        #poste
        self.esperar_clicar_xpath('//*[@id="ulCatalogMenu"]/li[17]/a/div[2]')
        #poste_2
        self.esperar_clicar_xpath('//*[@id="ulCatalogMenu"]/li[17]/ul/li/a/div[2]')
        #clicar no local escolhido
        pt.click(x,y)
        time.sleep(.5)
        #clicar com direito
        pt.click(1321,310)

        self.driver.switch_to.default_content()

    def tracado_inicio(self):
        def on_click(x, y,button,pressed):
            if button == mouse.Button.left and pressed:
                # Retornar False para a execução do listener de eventos
                return False

        def esperar_clicar():
            # Listener irá verificar quando o mouse clicará
            with mouse.Listener(on_click=on_click) as listener:
                while True:
                    # Assim que o mouse clicar, o listener irá encerrar e parar o loop
                    if not listener.running:
                        break  
        
        # Listener irá verificar quando o mouse clicará
        with mouse.Listener(on_click=on_click) as listener:
            while True:
                # Assim que o mouse clicar, o listener irá encerrar e parar o loop
                if not listener.running:
                    break     
        #definição da posição do mouse              
        x , y = pt.position()

        # Listener irá verificar quando o mouse clicará
        with mouse.Listener(on_click=on_click) as listener:
            while True:
                # Assim que o mouse clicar, o listener irá encerrar e parar o loop
                if not listener.running:
                    break    

        #definição da posição do mouse              
        a , b = pt.position()

        '''
        # Listener irá verificar quando o mouse clicará
        with mouse.Listener(on_click=on_click) as listener:
            while True:
                # Assim que o mouse clicar, o listener irá encerrar e parar o loop
                if not listener.running:
                    break    

        #definição da posição do mouse              
        c , d = pt.position()

        # Listener irá verificar quando o mouse clicará
        with mouse.Listener(on_click=on_click) as listener:
            while True:
                # Assim que o mouse clicar, o listener irá encerrar e parar o loop
                if not listener.running:
                    break    

        #definição da posição do mouse              
        k , l = pt.position()

        '''

        time.sleep(1.5)
        
        #iframe
        self.iframe('iframe-content-wrapper')
        time.sleep(.5)
        #adicionar
        self.esperar_clicar_xpath('//*[@id="paneldiv"]/div[22]')
        #traçado
        self.esperar_clicar_xpath('//*[@id="olControlAddRouteOi"]')
        #Aéreo
        self.esperar_clicar_xpath('//*[@id="ulCatalogMenu"]/li[1]/a/div[2]')
        #Aéreo em apoio
        self.esperar_clicar_xpath('//*[@id="ulCatalogMenu"]/li[1]/ul/li[2]/a/div')
        
        pt.click(x , y)
        time.sleep(1)
        
        pt.doubleClick(a , b)
        time.sleep(.5)

        esperar_clicar()
        time.sleep(.5)
        esperar_clicar()
        time.sleep(2)

        self.esperar_clicar_xpath('//*[@id="finish"]/span')

        #pt.click(a , b)
        #time.sleep(.5)

        #pt.doubleClick(c , d)
        #time.sleep(.5)

        #pt.click(c , d)
        #time.sleep(.5)

        #pt.doubleClick(k , l)

    def mudar_cabo(self):
        wdw = WebDriverWait(self.driver, 5)
        self.iframe('iframe-content-wrapper')
        
        #comp lance (netwin)
        tot_cl = self.driver.find_element(By.XPATH,'/html/body/div[*]/div[2]/form/div/div[5]/div/div[3]/div[4]/div/table/tbody/tr/td[3]')
        cl_folgas = tot_cl.get_attribute('title')

        #CL e folgas
        self.esperar_xpath('//*[@id="tab-entity"]/ul/li[4]/a/label')
        time.sleep(.5)
    
        
        self.driver.switch_to.default_content()

    def endereco_survey(self,endereco,numero):
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
        try:     
            #definição da posição do mouse              
            x , y = pt.position()
            #iframe
            self.iframe('iframe-content-wrapper')
            #Modificar atributos
            self.esperar_clicar_xpath('//*[@id="paneldiv"]/div[23]')
            #local
            self.esperar_clicar_xpath('//*[@id="olControlModifyInfranode"]')
            time.sleep(1)
            #clicar no local escolhido
            pt.click(x,y)
            time.sleep(1)
            #iframe
            self.iframe('externalLocationIframe')
            #localização
            self.esperar_clicar_xpath('//*[@id="location_tab_localization"]')
            time.sleep(.5)
            #editar
            self.esperar_clicar_xpath('/html/body/div[5]/div/div/div/form/div[2]/div/div[2]/div/div/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[4]/a[2]')
            time.sleep(1.5)
            #Filtro Logradouro
            self.esperar_clicar_xpath('//*[@id="select2-location_addresses_select_baseAddress-container"]')
            time.sleep(.7)
            #digite algo ae
            self.esperar_xpath_txt('/html/body/span/span/span[1]/input',endereco)
            time.sleep(1.5)
            resultado = self.driver.find_element(By.XPATH,'//*[@id="select2-location_addresses_select_baseAddress-results"]/li[1]').text
            self.esperar_clicar_xpath('//*[@id="select2-location_addresses_select_baseAddress-results"]/li[1]')
            time.sleep(1.3)
            
            if resultado == 'Nenhum resultado encontrado':
                sg.popup_ok('Não encontrei o CEP\nPreencha manualmente')
            else:
                self.esperar_xpath_txt('//*[@id="location_addresses_input_numFachada"]',numero)
                time.sleep(.3)
                #self.esperar_clicar_xpath('//*[@id="modal_button_ok"]"]',numero)
            self.driver.switch_to.default_content()
        except:
            self.driver.switch_to.default_content()
            #iframe
            self.iframe('iframe-content-wrapper')
            #Fechar
            self.esperar_clicar_xpath('/html/body/div[7]/div[1]/a[1]/span')
            self.driver.switch_to.default_content()

    def procurar_cep(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = Chrome(executable_path=ChromeDriverManager().install(),options=options)

        def esperar_xpath_txt(elemento,txt):
            wdw = WebDriverWait(driver, 60)
            wdw.until(element_to_be_clickable(('xpath', elemento)))    
            time.sleep(.15)
            driver.find_element(By.XPATH,elemento).clear()
            driver.find_element(By.XPATH,elemento).send_keys(txt)

        def esperar_clicar_xpath(elemento):
            wdw = WebDriverWait(driver, 60)
            wdw.until(EC.element_to_be_clickable((By.XPATH, elemento)))
            driver.find_element(By.XPATH,elemento).click()
        
        for i in tqdm(range(2,402), desc ="Carregando..." ):
            wb = load_workbook('Arquivos xlsx//survey.xlsx')
            ws = wb.active
            coord = ws[f'D{i}'].value
            try:
                coordenada = coord.split(",")
            except:
                break
            #coordenadas x e y
            coordx = coordenada[0]
            coordy = coordenada[1]
            
            cell1 = ws.cell(row=1, column=6)
            cell = ws.cell(row=i, column=6)
            cell1.value = 'CEP GOOGLE MAPS'
        
            if coord == 'None':
                break
            else:
                try:
                    driver.get("https://www.google.com.br/maps")
                    time.sleep(.5)
                    esperar_xpath_txt('//*[@id="searchboxinput"]', coordy + ',' + coordx)
                    time.sleep(.3)
                    esperar_clicar_xpath('//*[@id="searchbox-searchbutton"]') #pesquisar

                    time.sleep(1)
                    wdw = WebDriverWait(driver, 10)
                    wdw.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[*]/div[*]/div/div[*]/div/div/div[10]/div[*]/div[*]/span[2]')))
                    cood1 = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[*]/div[*]/div/div[*]/div/div/div[10]/div[*]/div[*]/span[2]').text
                    sem_acento = unidecode(cood1)
                    minuscula = sem_acento.lower()
                    str_tabela = minuscula.split()
                    letras_remover = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','z','.',',','-']
                    for letra in letras_remover:
                        str_tabela = [ l.replace(letra, '') for l in str_tabela ]

                    sem_espaco_vazio = [elemento for elemento in str_tabela if elemento.strip() != ""]
                    try:
                        if sem_espaco_vazio[1] == None:
                            cell.value = 'Tem que usar o CEP padrão'
                        else:
                            try:
                                cell.value = sem_espaco_vazio[2]
                                 
                            except:
                                cell.value = sem_espaco_vazio[1]
                    except:
                        try:
                            cell.value = sem_espaco_vazio[0]
                        except:
                            cell.value = 'Tem que usar o CEP padrão'
                            
                except: 
                    sg.popup_ok('Tente novamente', keep_on_top=True)
                    break

                wb.save('Arquivos xlsx//survey.xlsx')
                
    def cadastro_poste_kmz(self,coodx,coody):
        minha_lista = []
        for i in range (6):
            minha_lista.append(random.randint(1,9))
        num = int(''.join(map(str,minha_lista)))
        novo_numero = '20200824091321' + str(num)
        #ler arquivo
        tree = et.parse('hp.xml')
        root = tree.getroot()
        #modificar corrdenada no arquivo xml
        root.find('coordX').text = coodx
        root.find('coordY').text = coody
        #escrever xml
        tree.write('moradia1//moradia1.xml')
        #tarnsformar em zip
        shutil.make_archive(f'survey//KLAYTON_{novo_numero}','zip','./','moradia1//moradia1.xml',)
        caminho_do_arquivo = os.path.abspath('moradia1//moradia1.xml') 
        #deletar arquivo xml
        try: 
            os.remove(caminho_do_arquivo) 
            print("Arquivo XML removido com sucesso!")     
        except FileNotFoundError: 
            print("Arquivo XML não encontrado!") 
        except PermissionError: 
            print("Sem permissão para excluir o arquivo XML!") 
        except Exception as e: 
            print("Erro ao tentar excluir o arquivo XML:", e)
            #tqdm(range(2,402), desc ="Carregando..."):
            
    def criar_hp_coord(self):
        #logando os arquivos xlsx, com um laço de tentativa
        try:
            wb = load_workbook('Arquivos xlsx//survey.xlsx')
            ws = wb.active
            workbook = load_workbook('Arquivos xlsx//roteiro.xlsx')
            worksheet = workbook.active
        except:
            sg.popup('Não tem os arquivo nescessario na pasta!\n','1-survey.xlsx\n','2-roteiro.xlsx',keep_on_top=True)
            
        def pasta(caminho):
            pasta = caminho
            #verificar se a pasta existe se não existir ele ira criar
            if not os.path.exists(pasta):
                os.makedirs(pasta)

        pasta(os.path.abspath('moradia1//'))
        pasta(os.path.abspath('edificio1//'))
        pasta(os.path.abspath('edificio1//edificio'))
        pasta(os.path.abspath('edificio1//apartamentos//'))
        pasta(os.path.abspath('moradia1//'))
                                    
        #laço de repetição com tempo determinado max 400 tentativa
        for i in tqdm(range(2,402), desc ="Carregando..." ):
            selected_theme = 'Reddit'
            sg.theme(selected_theme)  
            sleep(.1)
            #encontrar e atribuir valores as variaveis dde uma planilha xlsx
            coord = str(ws[f'E{i}'].value)
            if coord == 'None':
                break
            #uma variavel recebendo coordenadas, trocando ',' por '.' e concatenando com uma virgula no meio
            coordenada = coord.split(",")
            #coordenadas x e y
            coordx = coordenada[0]
            coordy = coordenada[1]
     
            google_cep = str(ws[f'G{i}'].value)
            numero = str(ws[f'A{i}'].value)
            num_novo = numero.lower()
            quantidade = str(ws[f'B{i}'].value)
            predio = str(ws[f'C{i}'].value)
            bloco = str(ws[f'D{i}'].value)
            #uma condição para que quando valor da variavel for vazio, quebre o laço
            if num_novo == 'lv' or num_novo == 'sn' or num_novo == 'tbd' or num_novo == 's/n':
                continue
            #uma condição para que quando valor da variavel for vazio, quebre o laço
            if google_cep == 'None':
                cep = str(ws[f'F{i}'].value)
            else:
                cep = str(ws[f'G{i}'].value)
                
            #encontrar e atribuir valores as variaveis de uma planilha xlsx
            column_cep = worksheet['V']
            for cell in column_cep:
                cep_planilha = str(cell.value)
                if cep_planilha == cep:
                    row_number = cell.row  # Número da linha onde o valor foi encontrado
                    bairro = str(worksheet[f'M{row_number}'].value)
                    roteiro = str(worksheet[f'C{row_number}'].value)
                    localidade = str(worksheet[f'H{row_number}'].value)
                    cod_logradouro = str(worksheet[f'N{row_number}'].value)
                    logradouro = str(worksheet[f'Q{row_number}'].value) + ' ' + str(worksheet[f'O{row_number}'].value) + ', ' + str(worksheet[f'M{row_number}'].value) + ', ' + str(worksheet[f'G{row_number}'].value) + ', ' + str(worksheet[f'J{row_number}'].value) + ', ' + str(worksheet[f'G{row_number}'].value) + ' - ' + str(worksheet[f'E{row_number}'].value) + ' ' + f'({cod_logradouro})'
                    break
                
            if cep_planilha != cep:
                    row_number = cell.row  # Número da linha onde o valor foi encontrado
                    bairro = str(worksheet[f'M{row_number}'].value)
                    roteiro = str(worksheet[f'C{row_number}'].value)
                    localidade = str(worksheet[f'H{row_number}'].value)
                    cod_logradouro = str(worksheet[f'N{row_number}'].value)
                    logradouro = str(worksheet[f'Q{row_number}'].value) + ' ' + str(worksheet[f'O{row_number}'].value) + ', ' + str(worksheet[f'M{row_number}'].value) + ', ' + str(worksheet[f'G{row_number}'].value) + ', ' + str(worksheet[f'J{row_number}'].value) + ', ' + str(worksheet[f'G{row_number}'].value) + ' - ' + str(worksheet[f'E{row_number}'].value) + ' ' + f'({cod_logradouro})'
                    
            #condição para fazer uma casa
            if quantidade == 'None':
                try:
                    tree = et.parse('Arquivos xml//hp.xml')
                    root = tree.getroot()    
                    #encontrando e atribuindo novos valores ao xml
                    for country in root.findall('enderecoEdificio'):
                        country.find('logradouro').text = logradouro
                        country.find('numero_fachada').text = numero
                        country.find('cep').text = cep
                        country.find('bairro').text = bairro
                        country.find('id_roteiro').text = roteiro
                        country.find('id_localidade').text = localidade
                        country.find('cod_lograd').text = cod_logradouro

                    #trecho que perimite criar uma lista de numeros e uma sequecia para o winrar
                    def criar_arquivo(caminho, nome_arquivo):
                        arquivo = os.path.join(caminho, nome_arquivo)

                        # Verificar se o arquivo já existe
                        if os.path.exists(arquivo):
                            return

                        # Criar o arquivo
                        with open(arquivo, 'w') as f:
                            f.write('')  # Escrever conteúdo inicial se necessário

                    caminho = os.path.abspath('Arquivos xml')
                    nome_arquivo = 'numeros_gerados.txt'
                    criar_arquivo(caminho, nome_arquivo)

                    # Nome do arquivo para armazenar os números gerados
                    nome_arquivo = os.path.join(caminho, 'numeros_gerados.txt')

                    # Função para verificar se um número já foi gerado anteriormente
                    def numero_existe(numero, numeros_existentes):
                        return numero in numeros_existentes

                    numeros_existentes = set()

                    # Abrir o arquivo em modo de leitura para obter os números já gerados
                    with open(nome_arquivo, 'r') as f:
                        numeros_existentes = set(f.read().split())

                    nova_lista = []

                    # Gerar números até ter 6 números diferentes
                    while len(nova_lista) < 6:
                        novo_numero = random.randint(0, 9)
                        nova_lista.append(str(novo_numero))

                    # Gerar número com 20 dígitos
                    num = ''.join(nova_lista)
                    if len(num) == 5:
                        num += str(random.randint(0, 9))

                    novo_num = '20200824091322' + num

                    # Verificar se o número já existe na lista atual ou no arquivo
                    while num in numeros_existentes:
                        nova_lista = []
                        while len(nova_lista) < 6:
                            novo_numero = random.randint(0, 9)
                            nova_lista.append(str(novo_numero))

                        num = ''.join(nova_lista)
                        if len(num) == 5:
                            num += str(random.randint(0, 9))

                        novo_num = '20200824091322' + num

                    # Atualizar o arquivo com o número gerado
                    with open(nome_arquivo, 'a') as f:
                        f.write(num + '\n')

                    #modificar corrdenada no arquivo xml
                    root.find('coordX').text = str(coordx)
                    root.find('coordY').text = str(coordy)
                    root.find('localidade').text = str(worksheet[f'J{i}'].value)
                    #escrever xml
                    tree.write('moradia1//moradia1.xml')
                    #transformar arquivo zip na pasta moradia1
                    shutil.make_archive(f'survey//KLAYTON_{novo_num}','zip','./','moradia1//moradia1.xml',)
                    caminho_do_arquivo = os.path.abspath('moradia1//moradia1.xml') 
                    #deletar arquivo xml
                    os.remove(caminho_do_arquivo)      
                except FileNotFoundError: 
                    sg.popup_no_wait("Certifique-se de que o arquivo esteja na pasta:\nhp.xml\n",keep_on_top=True)
                    sleep(2) 
                except PermissionError: 
                    sg.popup_no_wait("Sem permissão para excluir o arquivo XML!\nmoradia1.xml",keep_on_top=True)
                    sleep(2)
                except Exception as e: 
                    sg.popup_no_wait("Erro ao tentar excluir o arquivo XML:\nmoradia1.xml,keep_on_top=True", e)
                    sleep(2)

            #condição para fazer casa com casas secundaria ex: casa 1, casa 2, casa 3
            elif quantidade != 'None' and predio == 'None':
                try: 
                    #logando os arquivos xml
                    tree = et.parse('Arquivos xml//hp2.xml')
                    root = tree.getroot()
                    #transformando quantidade em um inteiro para iteirar no loop de repetição com tempo determinado
                    quant = int(quantidade)
                    for i in range(1,quant+1):
                        sleep(0.1) 
                        def criar_arquivo(caminho, nome_arquivo):
                            arquivo = os.path.join(caminho, nome_arquivo)

                            # Verificar se o arquivo já existe
                            if os.path.exists(arquivo):
                                return

                            # Criar o arquivo
                            with open(arquivo, 'w') as f:
                                f.write('')  # Escrever conteúdo inicial se necessário

                        caminho = os.path.abspath('Arquivos xml')
                        nome_arquivo = 'numeros_gerados.txt'
                        criar_arquivo(caminho, nome_arquivo)

                        # Nome do arquivo para armazenar os números gerados
                        nome_arquivo = os.path.join(caminho, 'numeros_gerados.txt')

                        # Função para verificar se um número já foi gerado anteriormente
                        def numero_existe(numero, numeros_existentes):
                            return numero in numeros_existentes

                        numeros_existentes = set()

                        # Abrir o arquivo em modo de leitura para obter os números já gerados
                        with open(nome_arquivo, 'r') as f:
                            numeros_existentes = set(f.read().split())

                        nova_lista = []

                        # Gerar números até ter 6 números diferentes
                        while len(nova_lista) < 6:
                            novo_numero = random.randint(0, 9)
                            nova_lista.append(str(novo_numero))

                        # Gerar número com 20 dígitos
                        num = ''.join(nova_lista)
                        if len(num) == 5:
                            num += str(random.randint(0, 9))

                        novo_num = '20200824091322' + num

                        # Verificar se o número já existe na lista atual ou no arquivo
                        while num in numeros_existentes:
                            nova_lista = []
                            while len(nova_lista) < 6:
                                novo_numero = random.randint(0, 9)
                                nova_lista.append(str(novo_numero))

                            num = ''.join(nova_lista)
                            if len(num) == 5:
                                num += str(random.randint(0, 9))

                            novo_num = '20200824091322' + num

                        # Atualizar o arquivo com o número gerado
                        with open(nome_arquivo, 'a') as f:
                            f.write(num + '\n')

                        #encontrando e atribuindo novos valores ao xml
                        for country in root.findall('enderecoEdificio'):
                            country.find('argumento1').text = str(i)
                            country.find('logradouro').text = logradouro
                            country.find('numero_fachada').text = numero
                            country.find('cep').text = cep
                            country.find('bairro').text = bairro
                            country.find('id_roteiro').text = roteiro
                            country.find('id_localidade').text = localidade
                            country.find('cod_lograd').text = cod_logradouro
                        #encontrar e atribuir valores ao atributo do xml
                        root.find('coordX').text = str(coordx)
                        root.find('coordY').text = str(coordy)
                        root.find('localidade').text = str(worksheet[f'J{i}'].value) 
                        sleep(0.2)    
                        #escrever xml
                        tree.write(f'moradia1//moradia1.xml')
                        sleep(.5)
                        #transformar arquivo zip na pasta moradia1
                        shutil.make_archive(f'survey//KLAYTON_{novo_num}','zip','./','moradia1//moradia1.xml',)
                        #remover o arquivo moradia1.xml
                        caminho_do_arquivo = os.path.abspath('moradia1//moradia1.xml') 
                        #deletar arquivo xml
                        os.remove(caminho_do_arquivo) 
                except FileNotFoundError:
                    sg.popup_no_wait("Certifique-se de que o arquivo esteja na pasta:\nhp2.xml\n",keep_on_top=True)
                    sleep(2)
                except PermissionError: 
                    sg.popup_no_wait("Sem permissão para excluir o arquivo XML!\nmoradia1.xml",keep_on_top=True)
                    sleep(2)
                except Exception as e: 
                    sg.popup_no_wait("Erro ao tentar excluir o arquivo XML:\nmoradia1.xml,keep_on_top=True", e)
                    sleep(2)
            
            #condição para fazer predio
            else:
                #logando os arquivos xml
                if bloco != 'None':
                    tree = et.parse('Arquivos xml//arquivo2.xml')
                    root = tree.getroot()
                else:
                    tree = et.parse('Arquivos xml//arquivo.xml')
                    root = tree.getroot()

                tree_apartamento = et.parse('Arquivos xml//apartamento.xml') 
                root_apartamento = tree_apartamento.getroot()
                
                def criar_arquivo(caminho, nome_arquivo):
                    arquivo = os.path.join(caminho, nome_arquivo)

                    # Verificar se o arquivo já existe
                    if os.path.exists(arquivo):
                        return

                    # Criar o arquivo
                    with open(arquivo, 'w') as f:
                        f.write('')  # Escrever conteúdo inicial se necessário

                caminho = os.path.abspath('Arquivos xml')
                nome_arquivo = 'numeros_gerados.txt'
                criar_arquivo(caminho, nome_arquivo)

                # Nome do arquivo para armazenar os números gerados
                nome_arquivo = os.path.join(caminho, 'numeros_gerados.txt')

                # Função para verificar se um número já foi gerado anteriormente
                def numero_existe(numero, numeros_existentes):
                    return numero in numeros_existentes

                numeros_existentes = set()

                # Abrir o arquivo em modo de leitura para obter os números já gerados
                with open(nome_arquivo, 'r') as f:
                    numeros_existentes = set(f.read().split())

                nova_lista = []

                # Gerar números até ter 6 números diferentes
                while len(nova_lista) < 6:
                    novo_numero = random.randint(0, 9)
                    nova_lista.append(str(novo_numero))

                # Gerar número com 20 dígitos
                num = ''.join(nova_lista)
                if len(num) == 5:
                    num += str(random.randint(0, 9))

                novo_num = '20200824091322' + num

                # Verificar se o número já existe na lista atual ou no arquivo
                while num in numeros_existentes:
                    nova_lista = []
                    while len(nova_lista) < 6:
                        novo_numero = random.randint(0, 9)
                        nova_lista.append(str(novo_numero))

                    num = ''.join(nova_lista)
                    if len(num) == 5:
                        num += str(random.randint(0, 9))

                    novo_num = '20200824091322' + num

                # Atualizar o arquivo com o número gerado
                with open(nome_arquivo, 'a') as f:
                    f.write(num + '\n')

                #encontrando e atribuindo novos valores ao xml
                for country in root.findall('enderecoEdificio'):
                    country.find('logradouro').text = logradouro
                    country.find('numero_fachada').text = numero
                    country.find('cep').text = cep
                    country.find('bairro').text = bairro
                    country.find('id_roteiro').text = roteiro
                    country.find('id_localidade').text = localidade
                    country.find('cod_lograd').text = cod_logradouro
                    if bloco == 'None':
                        pass
                    else:
                        country.find('argumento1').text = bloco

                #encontrar e atribuir valores ao atributo do xml
                root.find('coordX').text = str(coordx) 
                root.find('coordY').text = str(coordy)
                root.find('localidade').text = str(worksheet[f'J{i}'].value) 
                sleep(0.2)    
                #escrever xml
                tree.write(f'edificio1//edificio//edificio1.xml')
                #edição da quantidade de hp no predio
                final = int(quantidade)
                for i in range(1, final):
                    tree_apartamento.write(f'edificio1//apartamentos//apartamento{i}.xml')
                    xml_inserir = et.parse(f'edificio1//apartamentos//apartamento{i}.xml')
                    elemento_pai_inserir = xml_inserir.getroot()
                    xml_principal = et.parse(f'edificio1//edificio//edificio{i}.xml')  
                    elemento_pai_princial = xml_principal.find('.//ucs')
                    elemento_pai_princial.append(elemento_pai_inserir)
                    xml_principal.write(f'edificio1//edificio//edificio{i+1}.xml')
                    caminho_origem = f'edificio1//edificio//edificio{final}.xml'
                    caminho_destino = f'edificio1//edificio.xml'
                #movendo o ultimo arquivo xml editado com a quantidade de hp para pasta edificio1
                shutil.move(caminho_origem,caminho_destino)
                #modificar edificio1.xml
                def modificar_xml():
                    # Carregando o arquivo XML 
                    tree = et.parse('edificio1//edificio.xml') 
                    root = tree.getroot()
                    #procurar elementos para alterar
                    elementos_id = root.findall(".//uc/id")
                    elementos_destinacao = root.findall(".//uc/destinacao")
                    elementos_complemento3 = root.findall(".//uc/id_complemento3")
                    elementos_argumento = root.findall(".//uc/argumento3")
                    elementos_complemento4 = root.findall(".//uc/id_complemento4")
                    elementos_logico = root.findall(".//uc/argumento4_logico")
                    elementos_real = root.findall(".//uc/argumento4_real")
                    contador = 0
                    piso_real = -1
                    piso_logico = 0
                    #alterando esses elementos
                    #id apartamento
                    for i, elemento in enumerate(elementos_id):
                        elemento.text = f'27385916{79+i}'
                    #utilização    
                    for i, elemento in enumerate(elementos_destinacao):
                        elemento.text = f'RESIDENCIA'
                    #não pode modificar    
                    for i, elemento in enumerate(elementos_complemento3):
                        elemento.text = '9'
                    #numero do apartamento    
                    for i, elemento in enumerate(elementos_argumento):
                        if (i+1) % 4 == 1:
                            contador += 1
                        elemento.text = f'{contador}0{i % 4}'
                    #não pode modificar    
                    for i, elemento in enumerate(elementos_complemento4):
                        elemento.text = '7'
                    #piso que logico
                    for i, elemento in enumerate(elementos_logico):
                        if (i+1) % 4 == 1:
                            piso_logico += 1
                        elemento.text = f'{piso_logico}'
                    #piso real    
                    for i, elemento in enumerate(elementos_real):
                        if (i+1) % 4 == 1:
                            piso_real += 1
                        elemento.text = f'{piso_real}' 
                    #escrever xml                                                                   
                    tree.write('edificio1//edificio1.xml')
                    
                modificar_xml()
                #gravar em zip arquivo
                shutil.make_archive(f'survey//KLAYTON_{novo_num}','zip','./','edificio1//edificio1.xml',)
                minha_lista = []
                for linha in range (6):
                    minha_lista.append(random.randint(1,9))
                    num = int(''.join(map(str,minha_lista)))
                    novo_numero = '20200824091321' + str(num)
                #caminho dos aquivo que serão deletados 
                for linha in range(0,final):
                    caminho_do_arquivo_edificio0 = os.path.abspath(f'edificio1//edificio//edificio{linha}.xml')
                    caminho_do_arquivo_apartamentos = os.path.abspath(f'edificio1//apartamentos//apartamento{linha}.xml')
                    caminho_do_arquivo_edificio = os.path.abspath(f'edificio1//edificio.xml')
                    caminho_do_arquivo_edificio1 = os.path.abspath(f'edificio1//edificio1.xml')
                    #deletar arquivo xml
                    try:
                        os.remove(caminho_do_arquivo_apartamentos)
                        os.remove(caminho_do_arquivo_edificio0)
                        os.remove(caminho_do_arquivo_edificio)
                        os.remove(caminho_do_arquivo_edificio1)      
                    except:
                        pass
                
        sg.popup('criação concluida',keep_on_top=True)    

    def cep_geopy(self):
        def buscar_cep(lat, lon): 
            url = f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={lon}" 
            response = requests.get(url) 
            if response.status_code == 200: 
                data = response.json() 
                if 'address' in data: 
                    address = data['address'] 
                    if 'postcode' in address: 
                        return address['postcode'].replace("-", "")

        wb = load_workbook('Arquivos xlsx//survey.xlsx')
        ws = wb.active 

        '''cep_final = buscar_cep(-27.45179655,-48.37881658)
        print(cep_final) '''

        for i in tqdm(range(2,402), desc="Carregando..."):
            coord = str(ws[f'D{i}'].value)
            cell1 = ws.cell(row=1, column=5)
            cell2 = ws.cell(row=1, column=1)
            cell3 = ws.cell(row=1, column=2)
            cell4 = ws.cell(row=1, column=3)
            cell5 = ws.cell(row=1, column=7)
            cell6 = ws.cell(row=1, column=8)
            cell7 = ws.cell(row=1, column=9)
            cell8 = ws.cell(row=1, column=10)

            cell = ws.cell(row=i, column=5)
            
            coordenada = coord.split(",")

            if coordenada[0] == 'None':
                break
            try:
                #coordenadas x e y
                coordy = str(coordenada[0])
                coordx = str(coordenada[1])
                cep_final = buscar_cep(coordx,coordy)
                if cep_final is not None:
                    cell1.value = 'CEP GEOPY'
                    cell2.value = 'NUMERO'
                    cell3.value = 'QUANTIDADE'
                    cell4.value = 'PREDIO'
                    cell5.value = 'LOGRADOURO'
                    cell6.value = 'BAIRRO'
                    cell7.value = 'CIDADE'
                    cell8.value = 'UF'
                    cell.value = cep_final
                else:
                    cell.value = 'CEP NÃO ENCONTRADO'
            except requests.exceptions.RequestException as e:
                cell.value = 'CEP NÃO ENCONTRADO'
                print(f"Erro ao buscar o CEP: {e}")
                
        wb.save('Arquivos xlsx//survey.xlsx')
        print('Arquivo salvo')

    def endereco_cep(self):
        wb = load_workbook('Arquivos xlsx//survey.xlsx')
        ws = wb.active  
        for i in tqdm(range(2,402), desc ="Carregando..."):
            cell = ws.cell(row=i, column=7)
            cell_1 = ws.cell(row=i, column=8)
            cell_2 = ws.cell(row=i, column=9)
            cell_3 = ws.cell(row=i, column=10)
            cep = ws[f'F{i}'].value
            try:
                if len(cep) == 8:
                    link = f'https://viacep.com.br/ws/{cep}/json/'

                    requisicao = requests.get(link)

                    dic_requisicao = requisicao.json()

                    uf = dic_requisicao['uf']
                    cidade = dic_requisicao['localidade']
                    bairro = dic_requisicao['bairro']
                    logradouro = dic_requisicao['logradouro']
                    cell.value = logradouro
                    cell_1.value = bairro
                    cell_2.value = cidade
                    cell_3.value = uf
                    
                    wb.save('Arquivos xlsx//survey.xlsx')
                else:
                    print("CEP Inválido")
            except:
                pass

    def google_maps(self):
        gmaps = googlemaps.Client(key='AIzaSyCrvhqOWCsosiVtza5JoktlMCuJ_qFUSCA')
        reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
        print(reverse_geocode_result.adress)
    
    def clicar_mapa_poste(self,celula): #inicio
        #variavel qe define o tema
        selected_theme = 'Reddit'
        sg.theme(selected_theme)
        wb = load_workbook('Arquivos xlsx//poste.xlsx')
        ws = wb.active

        def on_click(x, y,button,pressed):
            if button == mouse.Button.left and pressed:
                # Retornar False para a execução do listener de eventos
                return False
        # Listener irá verificar quando o mouse clicará
        with mouse.Listener(on_click=on_click) as listener:
            while True:
                # Verificar se a tecla Esc foi pressionada para encerrar o programa
                if keyboard.is_pressed('Enter'):
                    break
                # Assim que o mouse clicar, o listener irá encerrar e parar o loop
                if not listener.running:
                    break
            
        #definição da posição do mouse              
        x , y = pt.position()
        a = x - 65
        b = y - 65

        #inicio da criação do poste
        for linha in range(2,402):
            # Verificar se a tecla Esc foi pressionada para encerrar o programa
            if keyboard.is_pressed('Esc'):
                break
            #valores da planilha
            capacidade = str(ws[f'A{linha}'].value)
            tr = str(ws[f'B{linha}'].value)
            coordenada = str(ws[f'D{linha}'].value)
            #condição para parar de ler planilha
            if coordenada == 'None':
                break
            coord = coordenada.split(",")
            #coordenadas x e y
            coordx = coord[0]
            coordy = coord[1]
                   
            #iframe para criação do poste
            self.iframe('iframe-content-wrapper')
            sleep(1.3)
            #mãozinha
            self.esperar_clicar_xpath('//*[@id="paneldiv"]/div[22]')
            #local
            self.esperar_clicar_xpath('//*[@id="olControlAddInfranode"]')
            #poste
            self.esperar_clicar_xpath('//*[@id="ulCatalogMenu"]/li[17]/a/div[2]')
            sleep(.5)
            self.esperar_clicar_xpath('//*[@id="ulCatalogMenu"]/li[17]/ul/li/a/div[2]')
            #movimento do mouse para crição do poste
            sleep(.5)
            pt.click(x , y)
            sleep(.5)
            pt.rightClick(a, b)
            sleep(1)            
            # Esperando até seja visivel as Iframe da pagina
            self.iframe('externalLocationIframe')
            #Fora de padão 
            time.sleep(.05)
            self.esperar_clicar_ID('location_input_FORA_PADRAO') 
            #Capacidade (Altura/Esforço)
            self.esperar_xpath('//span[@id="select2-location_select_poleCapacity-container"]')
            self.esperar_xpath_txt('//input[@class="select2-search__field"]', capacidade) # colocar aqui a capacidade do poste
            self.esperar_xpath('//li[@class="select2-results__option select2-results__option--highlighted"]') 
            #Identificação em campo
            self.esperar_xpath('//span[@id="select2-location_select_fieldId-container"]')
            self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Existente - Conforme')
            self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
            #tipo
            self.esperar_xpath('//*[@id="select2-location_select_poleType-container"]/span')
            self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('CONCRETO/CIRCULAR')
            self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
            if tr == 'sim':
                self.esperar_xpath('//*[@id="select2-location_select_transformer-container"]/span')
                self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Sim')
                self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()   
            else:  
                self.esperar_xpath('//*[@id="select2-location_select_transformer-container"]/span')
                self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Não')
                self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
                
            #historico
            self.esperar_xpath('//*[@id="location_tab_logs"]')   
            #Origem
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
            
            #caracteristica
            self.esperar_xpath('//*[@id="location_tab_caracterizacao"]')  
            #proprietario
            self.esperar_xpath('//*[@id="select2-location_select_owner-container"]')
            self.driver.find_element(By.XPATH,'//input[@class="select2-search__field"]').send_keys('Alugado de terceiros')
            self.driver.find_element(By.XPATH,'//li[@class="select2-results__option select2-results__option--highlighted"]').click()
            #etiqueta de campo
            time.sleep(.5)
            self.esperar_xpath_txt('//*[@id="location_input_etiquetaEmCampo"]',f'{celula} | {capacidade}' ) #colocar aqui a capacidade do poste
            
            #localização
            self.esperar_xpath('//*[@id="location_tab_localization"]')
            sleep(1.5)
            #coordenada longitude
            self.esperar_xpath('//*[@id="location_input_longitude"]')
            self.driver.find_element(By.XPATH,'//*[@id="location_input_longitude"]').clear()
            self.driver.find_element(By.XPATH,'//*[@id="location_input_longitude"]').send_keys(coordx.replace(".",","))
            #coordenada latitude
            self.esperar_xpath('//*[@id="location_input_latitude"]')
            self.driver.find_element(By.XPATH,'//*[@id="location_input_latitude"]').clear()
            self.driver.find_element(By.XPATH,'//*[@id="location_input_latitude"]').send_keys(coordy.replace(".",","))
            
            #pop up para confirmação
            sg.popup('Arguardando a confirmação:\nEndereço',keep_on_top=True, location=(1088, 593))
        
            #guardar
            self.esperar_xpath('//*[@id="forms_button_save"]')
            
            self.driver.switch_to.default_content()
            
    def clicar_mapa_traçado(self,id_Sicom,id_projeto=True):
        while True:
            # Inicializar uma lista vazia para salvar as coordenadas do mouse
            coordenadas = []
            def on_click(cx, cy, button, pressed):
                if button == mouse.Button.left and pressed:
                    coordenadas.append((cx, cy))
                
            #iframe para criação do poste
            self.iframe('iframe-content-wrapper')
            #mãozinha
            self.esperar_clicar_xpath('//*[@id="paneldiv"]/div[22]')
            #traçado
            self.esperar_clicar_xpath('//*[@id="olControlAddRouteOi"]')
            #areo
            self.esperar_clicar_xpath('//*[@id="ulCatalogMenu"]/li[1]/a/div[2]')
            #areo em apoio
            self.esperar_clicar_xpath('//*[@id="ulCatalogMenu"]/li[1]/ul/li[2]/a/div')    
            sleep(.5)

            # Listener irá verificar quando o mouse clicará
            with mouse.Listener(on_click=on_click) as listener:
                while True:
                    # Verificar se a tecla Esc foi pressionada para encerrar o programa
                    if keyboard.is_pressed('Enter'):
                        break
                    
            if keyboard.is_pressed('Esc'):
                break
            #proprietario
            self.esperar_selecionar_ID('ownerId','1') #oi
            if id_projeto:
                #id sicon
                self.esperar_txt_ID('idSicom',id_Sicom)
                self.esperar_xpath('/html/body/div[*]/div[2]/form/div/div[2]/table[4]/tbody/tr[2]/td[1]/div[2]/div/ul/li')
            else:
                #nome de projeto
                self.esperar_txt_ID('project',id_Sicom)
                self.esperar_xpath('//*[@id="project_div"]/ul/li[1]/a')
            #implantação concluido
            self.esperar_selecionar_value('catProjectStateId','191')
            #origem
            self.esperar_selecionar_index('sourceId',1) #netwim
            #guardar
            self.esperar_clicar_xpath('/html/body/div[*]/div[3]/div/button[1]')
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content()
           
    def clicar_mapa_cdoe(self,id_sicon,estação,numero,precon_1_8_final=False,precon_1_8_meio=False,precon_1_16_final=False,precon_1_16_meio=False,
                         projeto=True,tbd=False):
        
        # Inicializar uma lista vazia para salvar as coordenadas do mouse
        coordenadas = []

        def on_click(cx, cy, button, pressed):
            if button == mouse.Button.left and pressed:
                coordenadas.append((cx, cy))
            
        # Listener irá verificar quando o mouse clicará
        with mouse.Listener(on_click=on_click) as listener:
            while True:
                # Verificar se a tecla Esc foi pressionada para encerrar o programa
                if keyboard.is_pressed('Enter'):
                    break
        #definição da posição do mouse              
        for coord in coordenadas:
            x, y = coord
            
            #iframe para criação do poste
            self.iframe('iframe-content-wrapper')
            #lupa
            self.esperar_clicar_xpath('//*[@id="paneldiv"]/div[18]')
            sleep(.1)
            #clicar no poste
            pt.click(x, y)
            
            sleep(1)
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
            pt.click(1115,478)
            pt.rightClick(x=1215, y=518) #direito
            time.sleep(1)
            
            #iframe para criação do CDOE
            self.iframe('externalIspIframe')
            self.iframe('dados')
            #seleciona qual equipamento sera cadastrado
            if precon_1_8_final:
                self.esperar_selecionar_ID('elem_num_sap','331995') #final
            elif precon_1_8_meio:
                self.esperar_selecionar_ID('elem_num_sap','331688') #intermediaria
            elif precon_1_16_final:
                self.esperar_selecionar_ID('elem_tipo.outroNomeEquip','CAIXA DISTR OPT SEL 17 SC EXT TAP 1:16') #final
            elif precon_1_16_meio:
                self.esperar_selecionar_ID('elem_tipo.outroNomeEquip','CAIXA DISTR OPT SEL 18 SC EXT TAP 30/70') #intermediaria
                
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
            
            #Identif. campo
            self.esperar_selecionar_ID('nameCampId','Existente - Conforme')
            
            #Estação abastecedora 1
            def estacao_predial(elemento):
                wdw = WebDriverWait(self.driver, 60)
                wdw.until(element_to_be_clickable(('xpath', elemento)))
                self.driver.find_element(By.XPATH,elemento).text
            #e
            self.esperar_clicar_xpath('//*[@id="suppStationFilterButton"]')
            
            uf = estacao_predial('//*[@id="uf"]')
            municipio = estacao_predial('//*[@id="municipio"]')
            localidade = estacao_predial('//*[@id="localidade"]')

            try:
                # Aguardar até que o elemento com o id "estacao" esteja clicável
                wdw = WebDriverWait(self.driver, 10)
                estacao_element = wdw.until(EC.element_to_be_clickable((By.ID, 'estacao')))
                
                # Criar objeto Select para o menu suspenso
                select = Select(estacao_element)
                
                # Verificar se a opção "cpmo" está disponível
                option_cpmo = None
                for option in select.options:
                    if option.text == "cpmo":
                        option_cpmo = option
                        break
                
                # Selecionar a opção "cpmo" se estiver disponível
                if option_cpmo:
                    select.select_by_visible_text("cpmo")
                else:
                    print("A opção 'cpmo' não está disponível no menu suspenso.")
                    
            except NoSuchElementException as e:
                print("Elemento com o id 'estacao' não encontrado:", e)

            #escolher
            self.esperar_clicar_xpath('//*[@id="imgListaRelEquipamento"]/span')

            #Topologia
            self.esperar_selecionar_ID('topology','A/B')
            sleep(.05)
            
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
                #tbd
                self.esperar_clicar_xpath('//*[@id="outOfPattern_check"]') #fora de padrão
                time.sleep(.5)
                self.esperar_xpath('//*[@id="onPatternTag"]')
                time.sleep(.5)
                self.esperar_xpath_txt('//*[@id="tagOnField"]','CDOE-'+ numero +'-TBD')
                self.esperar_xpath_txt('//*[@id="nomecNumber"]', '0')
            else:
                self.esperar_xpath_txt('//*[@id="nomecNumber"]', numero)

            sg.popup('Aguardando confirmação das estações abastecedora',keep_on_top=True)
            
            #Confimar
            self.esperar_clicar_ID('confAssoc')
            #Sair
            self.esperar_xpath('/html/body/div[*]/div/div/table/tbody/tr/td[3]/button')
                
            # Retorna para a janela principal (fora do iframe)
            self.driver.switch_to.default_content() 
            
            if keyboard.is_pressed('Esc') or not coordenadas:
                break

    def transformar_kmz(self):
        def pasta(caminho):
            pasta = caminho
            #verificar se a pasta existe se não existir ele ira criar
            if not os.path.exists(pasta):
                os.makedirs(pasta)

        pasta(os.path.abspath('kmz//'))
        pasta(os.path.abspath('Arquivos xlsx//'))    
        
        try:
            with zipfile.ZipFile(os.path.abspath('kmz//HPS.kmz'), 'r') as zip_ref:
                zip_ref.extractall(os.path.abspath('kmz'))
           
            tree = etree.parse(os.path.abspath('kmz//doc.kml'))
            doc = tree.getroot()

            pontos = []
            for pm in doc.xpath('//kml:Placemark', namespaces={'kml': 'http://www.opengis.net/kml/2.2'}):
                titulo = pm.xpath('.//kml:name/text()', namespaces={'kml': 'http://www.opengis.net/kml/2.2'})[0].strip()
                descricao = pm.xpath('.//kml:description/text()', namespaces={'kml': 'http://www.opengis.net/kml/2.2'})
                if descricao:
                    descricao = descricao[0].strip()
                else:
                    descricao = ""
                coordenadas = pm.xpath('.//kml:coordinates/text()', namespaces={'kml': 'http://www.opengis.net/kml/2.2'})[0].strip()
                pontos.append((titulo, descricao, '', coordenadas))

            with open('pontos.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
                writer = csv.writer(arquivo_csv, delimiter=';')
                writer.writerow(['numero/capacidade', 'quantidade/tr', 'predio/none', 'coordenadas'])
                for ponto in pontos:
                    writer.writerow(ponto)

            # ler o arquivo CSV
            df = pd.read_csv('pontos.csv', sep=';')

            #remover arquivo
            os.remove('pontos.csv')
            os.remove('kmz//doc.kml')

            # gravar em um arquivo Excel
            df.to_excel('Arquivos xlsx//survey.xlsx', index=False)

        except:
            sg.popup('esta sem arquivo kmz para fazer a conversão', keep_on_top=True)

    def ajuste_survey(self,vezes):
        wb = load_workbook('CONTROLE AJUSTE SURVEY.xlsx')
        ws = wb.active

        for i in range(2,602):
            survey = str(ws[f'L{i}'].value)
            if survey == 'None':
                break
            try:
                for lin in range(7,8):
                    self.iframe('iframe-content-wrapper')
                    self.esperar_selecionar_index("area", lin)
                    sleep(.2)
                    self.esperar_txt_ID('codigo',survey)
                    sleep(.2)
                    self.esperar_clicar_xpath('//*[@id="submit"]')
                    sleep(.5)

                    if 'Pesquisa sem resultados' in self.driver.find_element(By.XPATH,'//*[@id="gview_pesquisaGrid"]/div[3]/div[2]/span').text:
                        abastecido = 'NÃO LOCALIZADO'
                        ws[f'O{i}'].value = abastecido
                        wb.save("CONTROLE AJUSTE SURVEY.xlsx")
                    else:
                        '''abastecido = 'ABASTECIDO PELA'
                        ws[f'O{i}'].value = abastecido
                        wb.save("CONTROLE AJUSTE SURVEY.xlsx")
                        break'''
                        
                        #modificar atributos
                        self.esperar_clicar_xpath('//*[@id="paneldiv"]/div[23]')
                        #local
                        self.esperar_clicar_xpath('//*[@id="olControlModifyInfranode"]')

                        # Localize o elemento com base na tag <td> e na posição na tabela
                        element_res = self.driver.find_element("xpath", "//tr[contains(@role, 'row')][2]/td[3]")
                        # Realize o clique no elemento
                        element_res.click()
                        # Localize o elemento cujo ID contém a parte específica
                        element = self.driver.find_element(By.XPATH,"//*[contains(@id, 'OpenLayers.Geometry.Point_')]")
                        
                        if element.is_displayed():  
                            element.click()
                        else:
                            print("O elemento não está visível")
                                                
                    # Retorna para a janela principal (fora do iframe)
                    self.driver.switch_to.default_content()
                    
            except Exception as e:
                # Retorna para a janela principal (fora do iframe)
                self.driver.switch_to.default_content()
                print(f"Erro ao salvar o arquivo: {str(e)}")
                print(survey, i) 

    def deligar_pc(self):
        # Obter a hora atual
        hora_atual = datetime.datetime.now().time()

        # Definir o horário para desligar o computador (exemplo: 23:00)
        hora_desligamento = datetime.time(23, 0)

        # Verificar se a hora atual é igual ou posterior ao horário de desligamento
        if hora_atual >= hora_desligamento:
            # Calcular a quantidade de segundos até o próximo dia no horário de desligamento
            delta_tempo = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), hora_desligamento) - datetime.datetime.now()

            # Converter o tempo restante em segundos
            segundos_restantes = delta_tempo.total_seconds()

            # Aguardar até o horário de desligamento
            print(f"Aguardando até o horário de desligamento: {hora_desligamento}")
            os.system(f"timeout /t {int(segundos_restantes)} /nobreak > NUL")

        # Desligar o computador
        print("Desligando o computador...")
        os.system("shutdown /s /t 0")            