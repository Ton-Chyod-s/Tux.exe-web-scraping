import xml.etree.ElementTree as ET 

def criar_xml():
    # Carregando o arquivo XML 
    tree = ET.parse('arquivo.xml') 
    root = tree.getroot()                                   

    def adicionar(text):   
        pessoa_nome = ET.SubElement(elemento, text)
        pessoa_nome.text = "exemplo\t"  

    elementos = root.findall(".//ucs")

    for elemento in elementos:
        pessoa_nome = ET.SubElement(elemento, 'uc')
        pessoa_nome.text = "\t"


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
    result = 3 

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
                                        
                                                                
    tree.write('edificio1//arquivo1.xml')

result = 3
for i in range(1,3):
    criar_xml()
    
modificar_xml()
