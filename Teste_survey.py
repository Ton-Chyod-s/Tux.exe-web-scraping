import xml.etree.ElementTree as ET 
import os

def criar_xml():
    # Carregando o arquivo XML 
    tree = ET.parse('arquivo.xml') 
    root = tree.getroot()                                   

    def adicionar(text):   
        pessoa_nome = ET.SubElement(elemento, text)
        pessoa_nome.text = "exemplo\t"  

    elementos = root.findall(".//ucs")

    result = 5
    for i in range(1,int(result)+1):
        for elemento in elementos:
            pessoa_nome = ET.Element('uc')
            pessoa_nome.text = "\t"
            elemento.append(pessoa_nome)

    elementos1 = root.findall(".//uc")
    
    for elemento in elementos1:
        adicionar('id')
        adicionar('destinacao')
        adicionar('id_complemento3')
        adicionar('argumento3')
        adicionar('id_complemento4')
        adicionar('argumento4_logico')
        adicionar('argumento4_real')

    tree.write('edificio1//arquivo.xml')

def modificar_xml():
    # Carregando o arquivo XML 
    tree = ET.parse('edificio1//arquivo.xml') 
    root = tree.getroot()

    elementos_destinacao = root.findall(".//uc/destinacao")
    elementos_complemento3 = root.findall(".//uc/id_complemento3")
    elementos_argumento = root.findall(".//uc/argumento3")
    elementos_complemento4 = root.findall(".//uc/id_complemento4")
    elementos_logico = root.findall(".//uc/argumento4_logico")
    elementos_real = root.findall(".//uc/argumento4_real")
    
    for elemento in elementos_destinacao:
        # Faz algo com o elemento
        elemento.text = 'vai que e sua tafarel'

    for elemento in elementos_complemento3:
        # Faz algo com o elemento
        elemento.text = 'ta indo'                                     

    for elemento in elementos_argumento:
        # Faz algo com o elemento
        elemento.text = 'ixi massa'

    for elemento in elementos_complemento4:
        # Faz algo com o elemento
        elemento.text = 'achei outro'

    for elemento in elementos_logico:
        # Faz algo com o elemento
        elemento.text = '123' 

    for elemento in elementos_real:
        # Faz algo com o elemento
        elemento.text = '321'          
                                                                                         
    tree.write('edificio1//edificio1.xml')
    
    caminho_do_arquivo = os.path.abspath('edificio1//arquivo.xml') 
    #deletar arquivo xml
    try:
        os.remove(caminho_do_arquivo)      
    except FileNotFoundError: 
        print("Arquivo XML não encontrado!") 
    except PermissionError: 
        print("Sem permissão para excluir o arquivo XML!") 
    except Exception as e: 
        print("Erro ao tentar excluir o arquivo XML:", e)
                        

criar_xml()
    
modificar_xml()
