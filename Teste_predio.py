import xml.etree.ElementTree as et 
import shutil
import random
import os

caminho_origem = f'arquivo.xml'
caminho_destino = f'edificio1//edificio//edificio1.xml'

shutil.copy(caminho_origem,caminho_destino)

tree_apartamento = et.parse('apartamento.xml') 
root_apartamento = tree_apartamento.getroot()
final = 9
for i in range(1, (final + 1)):
    tree_apartamento.write(f'edificio1//apartamentos//apartamento{i}.xml')
    xml_inserir = et.parse(f'edificio1//apartamentos//apartamento{i}.xml')
    elemento_pai_inserir = xml_inserir.getroot()
    xml_principal = et.parse(f'edificio1//edificio//edificio{i}.xml')  
    elemento_pai_princial = xml_principal.find('.//ucs')
    elemento_pai_princial.append(elemento_pai_inserir)
    fim = final - 1
    xml_principal.write(f'edificio1//edificio//edificio{i+1}.xml')

    caminho_origem = f'edificio1//edificio//edificio{fim}.xml'
    caminho_destino = f'edificio1//edificio.xml'

shutil.move(caminho_origem,caminho_destino)

def modificar_xml():
    # Carregando o arquivo XML 
    tree = et.parse('edificio1//edificio.xml') 
    root = tree.getroot()

    elementos_id = root.findall(".//uc/id")
    elementos_destinacao = root.findall(".//uc/destinacao")
    elementos_complemento3 = root.findall(".//uc/id_complemento3")
    elementos_argumento = root.findall(".//uc/argumento3")
    elementos_complemento4 = root.findall(".//uc/id_complemento4")
    elementos_logico = root.findall(".//uc/argumento4_logico")
    elementos_real = root.findall(".//uc/argumento4_real")
    contador = 0
    
    for i, elemento in enumerate(elementos_id):
        elemento.text = f'27385916{79+i}'
        
    for i, elemento in enumerate(elementos_destinacao):
        elemento.text = f'RESIDENCIA'
        
    for i, elemento in enumerate(elementos_complemento3):
        elemento.text = str(i)
        
    for i, elemento in enumerate(elementos_argumento):
        if (i+1) % 4 == 1:
            contador += 1
        elemento.text = f'{contador}0{i}'
    
    for i, elemento in enumerate(elementos_complemento4):
        if (i+1) % 4 == 1:
            contador += 1
        elemento.text = str(contador)
    
    for i, elemento in enumerate(elementos_logico):
        elemento.text = 'T'
        
    for i, elemento in enumerate(elementos_real):
        elemento.text = 'T'
          
                                                                                         
    tree.write('edificio1//edificio1.xml')
    
modificar_xml()
minha_lista = []
for linha in range (6):
                    minha_lista.append(random.randint(1,9))
                    num = int(''.join(map(str,minha_lista)))
                    novo_numero = '20200824091321' + str(num)
                    
for linha in range(0,(final+2)):                    
    #deletar arquivo xml
    try:
        caminho_do_arquivo_apartamentos = os.path.abspath(f'edificio1//apartamentos//apartamento{linha}.xml')  
        os.remove(caminho_do_arquivo_apartamentos)
    except:
        pass
    try:
        caminho_do_arquivo_edificio = os.path.abspath(f'edificio1//edificio//edificio{linha}.xml')
        os.remove(caminho_do_arquivo_edificio)
    except:
        pass
        
try:
    caminho_do_arquivo_edificio = os.path.abspath(f'edificio1//edificio.xml')
    os.remove(caminho_do_arquivo_edificio)
except:
    pass


