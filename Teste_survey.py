from pycep_correios import get_address_from_cep, WebService
from openpyxl import load_workbook
from time import sleep
from tqdm import tqdm

wb = load_workbook('coordenada.xlsx')
ws = wb.active
for i in tqdm(range(2,402), desc ="Carregando..."):
    sleep(.5)
    endereco = get_address_from_cep('88066260', webservice=WebService.CORREIOS)    

    '''print(endereco['logradouro'])
        print(endereco['bairro'])
        print(endereco['cidade'])
        print(endereco['uf'])
        print(endereco['cep'])'''