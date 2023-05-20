import random
import os

for i in range(362880):
    def criar_arquivo(caminho, nome_arquivo):
        arquivo = os.path.join(caminho, nome_arquivo)

        # Verificar se o arquivo já existe
        if os.path.exists(arquivo):
            return

        # Criar o arquivo
        with open(arquivo, 'w') as f:
            f.write('')  # Escrever conteúdo inicial se necessário

    caminho = os.path.abspath('Arquivos xml')
    nome_arquivo = 'numeros_gerados.txt'
    criar_arquivo(caminho, nome_arquivo)

    # Nome do arquivo para armazenar os números gerados
    nome_arquivo = os.path.join(caminho, 'numeros_gerados.txt')

    # Função para verificar se um número já foi gerado anteriormente
    def numero_existe(numero, numeros_existentes):
        return numero in numeros_existentes

    numeros_existentes = set()

    # Abrir o arquivo em modo de leitura para obter os números já gerados
    with open(nome_arquivo, 'r') as f:
        numeros_existentes = set(f.read().split())

    nova_lista = []

    # Gerar números até ter 6 números diferentes
    while len(nova_lista) < 6:
        novo_numero = random.randint(0, 9)
        nova_lista.append(str(novo_numero))

    # Gerar número com 20 dígitos
    num = ''.join(nova_lista)
    if len(num) == 5:
        num += str(random.randint(0, 9))

    novo_num = '20200824091322' + num

    # Verificar se o número já existe na lista atual ou no arquivo
    while num in numeros_existentes:
        nova_lista = []
        while len(nova_lista) < 6:
            novo_numero = random.randint(0, 9)
            nova_lista.append(str(novo_numero))

        num = ''.join(nova_lista)
        if len(num) == 5:
            num += str(random.randint(0, 9))

        novo_num = '20200824091322' + num

    # Atualizar o arquivo com o número gerado
    with open(nome_arquivo, 'a') as f:
        f.write(num + '\n')

    print(novo_num)