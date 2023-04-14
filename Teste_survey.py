import xml.etree.ElementTree as ET 
# Carregando o arquivo XML 
tree = ET.parse('arquivo.xml') 
root = tree.getroot()
result = 3

'''elementos_filhos = root.findall('caixasEntrada')
for elemento_filho in elementos_filhos:
    for child in elemento_filho:
        for i in child:
            if i.tag =='prumadas':
                for filho in i:
                    for prum in filho:
                        if prum.tag == 'ucs':
                            for lin in prum:
                                for i in range(1,result):
                                    print(i)
                                    for linha in lin:
                                        print(linha.text)'''
                                        

elementos = root.findall(".//uc")
elementos_destinacao = root.findall(".//uc/destinacao")
elementos_complemento3 = root.findall(".//uc/id_complemento3")
elementos_argumento = root.findall(".//uc/argumento3")
elementos_complemento4 = root.findall(".//uc/id_complemento4")
elementos_logico = root.findall(".//uc/argumento4_logico")
elementos_real = root.findall(".//uc/argumento4_real")


def adicionar(text):   
    pessoa_nome = ET.SubElement(elemento, text)
    pessoa_nome.text = "\t"  
    
    
for elemento in elementos:
    adicionar('id')
    adicionar('destinacao')
    adicionar('id_complemento3')
    adicionar('argumento3')
    adicionar('id_complemento4')
    adicionar('argumento4_logico')
    adicionar('argumento4_real')
    
    
'''
for elemento in elementos_destinacao:
    # Faz algo com o elemento
    elemento.text = 'vai que é sua tafarel'

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
    elemento.text = '321'    '''                      
                                    
                                                             
tree.write('edificio1//arquivo.xml')

#transformar em string
#print(ET.tostring(root))
#mostra o atributo do xml
#print(root.attrib)

