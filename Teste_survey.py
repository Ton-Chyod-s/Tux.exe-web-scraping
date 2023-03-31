import xml.etree.ElementTree as et

linha1 = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>"
linha2 = '<edificio xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" versao="7.8.1" autorizacao="3b33825972febe49591b48a9e8e6abb" tipo="M">'
linha3 = '<gravado>false</gravado>'
linha4 = '<idCEMobile>1</idCEMobile>'
linha5 = '<coordX>-54.5741187</coordX>'
linha6 = '<coordY>-16.4700428</coordY>'
linha7 = '<codigoZona>CPCE-30</codigoZona>'
linha8 = '<nomeZona>CPCE-30</nomeZona>'
linha9 = '<localidade>CAMPO GRANDE</localidade>'
linha10 = '<enderecoEdificio>'
linha11 = '<logradouro>RUA TAPAJOS</logradouro>'
linha12 = '<numero_fachada>5</numero_fachada>'
linha13 = '<cep>79022210</cep>'
linha14 = '<bairro>VILA RICA</bairro>'
linha15 = '<id_roteiro>6712779</id_roteiro>'
linha16 = '<id_localidade>1853370</id_localidade>'
linha17 = '<cod_lograd>2500055300</cod_lograd>'
linha18 = '</enderecoEdificio>'
linha19 = '<tecnico>'
linha20 = '<id>876764089</id>'
linha21 = '<nome>NATALIA GUARIPUNA FERREIRA</nome>'
linha22 = '</tecnico>'
linha23 = '<empresa>'
linha24 = '<id>42541126</id>'
linha25 = '<nome>TELEMONT</nome>'
linha26 = '</empresa>'
linha27 = '<data>20200824091252</data>'
linha28 = '<totalUCs>1</totalUCs>'
linha29 = '<ocupacao>EDIFICACAOCOMPLETA</ocupacao>'
linha30 = '<numPisos>1</numPisos>'
linha31 = '<destinacao>RESIDENCIA</destinacao>'
linha32 = '</edificio>'

moradia = f'{linha1}\n{linha2}\n{linha3}\n{linha4}\n{linha5}\n{linha6}\n{linha7}\n{linha8}\n{linha9}\n{linha10}\n{linha11}\n{linha12}\n{linha13}\n{linha14}\n{linha15}\n{linha16}\n{linha17}\n{linha18}\n{linha19}\n{linha20}\n{linha21}\n{linha22}\n{linha23}\n{linha24}\n{linha15}\n{linha26}\n{linha27}\n{linha28}\n{linha29}\n{linha30}\n{linha31}\n{linha32}'
           
#with open("moradia1.txt","w") as arquivo:
    #arquivo.write(moradia)

#ler arquivo
arquivo = et.parse('moradia1.xml')
raiz = arquivo.getroot()
'''
for linha in raiz.findall('coordX'):
    print(linha.text)

for linha in raiz.findall('coordY'):
    print(linha.text)
'''
raiz[2].clear()
print(raiz[2].attrib)

#print(et.tostring(raiz, encoding='utf8').decode('utf8'))

for movie in raiz.iter('coordX'):
    print(movie.text)

#for filhas in raiz:
    #print(filhas.tag, filhas.attrib )

#escrever xml
#arquivo.write('new_livros.xml')


