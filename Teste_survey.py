import zipfile
import shutil
import os
from random import randint

'''def gravar_arquivo_zip():
    with zipfile.ZipFile(os.path.abspath(f'KLAYTON_202304{randint(9,999999)}.zip'), 'w') as arquivo_zip: 
        arquivo_zip.write('moradia1.xml') 


# Exemplo de uso: 
gravar_arquivo_zip()'''

shutil.make_archive(f'KLAYTON_2020082409132155{randint(4,999999)}','zip','./','moradia1.xml',)