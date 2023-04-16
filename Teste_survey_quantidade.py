from time import sleep
from openpyxl import load_workbook
import PySimpleGUI as sg
import xml.etree.ElementTree as et
import random
import shutil
import os

#logando os arquivos xlsx, com um laço de tentativa
try:
    wb = load_workbook('coordenada.xlsx')
    ws = wb.active
    workbook = load_workbook('roteiro.xlsx')
    worksheet = workbook.active
except:
    sg.popup('Não tem os arquivo nescessario na pasta!\n','1-coordenada.xlsx\n','2-roteiro.xlsx',keep_on_top=True)
    
#laço de repetição com tempo determinado max 400 tentativa
for i in range(2,402):
    sleep(.1)
    #encontrar e atribuir valores as variaveis dde uma planilha xlsx
    coordx = str(ws[f'A{i}'].value)
    coordy = str(ws[f'B{i}'].value)
    #uma variavel recebendo coordenadas, trocando ',' por '.' e concatenando com uma virgula no meio
    coordenada = coordy.replace(",",".") + ', ' + coordx.replace(",",".")
    #uma condição para que quando valor da variavel for vazio, quebre o laço
    if coordenada is not None:
        break
    google_cep = str(ws[f'G{i}'].value)
    numero = str(ws[f'C{i}'].value)
    quantidade = str(ws[f'D{i}'].value)
    predio = str(ws[f'E{i}'].value)
    #uma condição para que quando valor da variavel for vazio, quebre o laço
    if google_cep == 'None':
        cep = str(ws[f'F{i}'].value)
    else:
        cep = str(ws[f'G{i}'].value)
    #encontrar e atribuir valores as variaveis dde uma planilha xlsx
    bairro = str(worksheet[f'M{i}'].value)
    roteiro = str(worksheet[f'C{i}'].value)
    localidade = str(worksheet[f'H{i}'].value)
    cod_logradouro = str(worksheet[f'N{i}'].value)
    logradouro = str(worksheet[f'Q{i}'].value) + ' ' + str(worksheet[f'O{i}'].value) + ', ' + str(worksheet[f'M{i}'].value) + ', ' + str(worksheet[f'G{i}'].value)+ ', ' + str(worksheet[f'J{i}'].value)+ ', ' + str(worksheet[f'G{i}'].value)+ ' - ' + str(worksheet[f'E{i}'].value)+ ' ' + f'({cod_logradouro})'
    #condição para fazer casa
    if quantidade == 'None':
        print('consegui achar uma casa pra fazer')
        
    #condição para fazer casa com casas secundaria ex: casa 1, casa 2, casa 3
    elif quantidade != 'None' and predio == 'None':
        #logando os arquivos xml, com um laço de tentativa
        try:
            tree = et.parse('hp2.xml')
            root = tree.getroot()
        except:
            break
        #transformando quantidade em um inteiro para iteirar no loop de repetição com tempo determinado
        quantidade = int(quantidade)
        for i in range(1,quantidade+1):
            sleep(0.1)
            #encontrar e atribuir valores ao atributo do xml
            root.find('coordX').text = str(coordx) 
            root.find('coordY').text = str(coordy)
            root.find('localidade').text = str(worksheet[f'J{i}'].value) 
            #atribuindo uma condição que escolhe numeros de forma aleatoria   
            num = random.randint(1,int(quantidade+1))
            novo_numero = f'20200824091321{str(num)}4483{str(num)}'
            #tranformando num i em uma string
            num_arg = str(i)
            sleep(0.1)
            #encontrando e atribuindo novos valores ao xml
            for country in root.findall('enderecoEdificio'):
                country.find('argumento1').text = num_arg
                country.find('logradouro').text = logradouro
                country.find('numero_fachada').text = numero
                country.find('cep').text = cep
                country.find('bairro').text = bairro
                country.find('id_roteiro').text = roteiro
                country.find('id_localidade').text = localidade
                country.find('cod_lograd').text = cod_logradouro
            sleep(0.2)    
            #escrever xml
            tree.write(f'moradia1//moradia1.xml')
            sleep(1.5)
            salvar = 'vou salvar agora a hp blz'
            if 'vou salvar agora a hp blz' in salvar:
                shutil.make_archive(f'survey//KLAYTON_{novo_numero}','zip','./','moradia1//moradia1.xml',)
            else:
                pass
            try:
                caminho_do_arquivo = os.path.abspath('moradia1//moradia1.xml') 
                #deletar arquivo xml
                os.remove(caminho_do_arquivo)      
            except:
                pass
            
    #condição para fazer predio
    else:
        print('achei um predio para fazer')
        
        