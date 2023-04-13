import xml.etree.ElementTree as ET 
# Carregando o arquivo XML 
tree = ET.parse('arquivo.xml') 
root = tree.getroot() 
result = 3

elementos_filhos = root.findall('caixasEntrada')
for elemento_filho in elementos_filhos:
    for child in elemento_filho:
        for i in child:
            if i.tag =='prumadas':
                for filho in i:
                    for prum in filho:
                        if prum.tag == 'ucs':
                            for lista in range(result):
                                novo_elemento_filho = ET.Element('uc')
                                novo_elemento_filho.text = '\n'
                                prum.insert(1,novo_elemento_filho)
                            
tree.write('edificio1//arquivo.xml')


