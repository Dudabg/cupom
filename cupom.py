import os
import re

def verificar_numeracao_repetida(caminho_pasta):
    numeros = []
    repetidos = set()
    
    # Regex para capturar números no nome do arquivo
    padrao = re.compile(r'\d+')
    
    # Iterar pelos arquivos na pasta
    for arquivo in os.listdir(caminho_pasta):
        if os.path.isfile(os.path.join(caminho_pasta, arquivo)):
            # Encontrar números no nome do arquivo
            match = padrao.findall(arquivo)
            if match:
                for numero in match:
                    if numero in numeros:
                        repetidos.add(numero)
                    else:
                        numeros.append(numero)
    
    if repetidos:
        print("Números repetidos encontrados:", ', '.join(repetidos))
    else:
        print("Não foram encontrados números repetidos.")

# Caminho da pasta
caminho = r"C:\Users\newgen\Desktop\Minha NewGen\atualizadores\teste"
verificar_numeracao_repetida(caminho)
