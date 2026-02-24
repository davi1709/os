import os

diretorio_atual = os.getcwd()
itens = os.listdir(diretorio_atual)

for item in itens:
    print(item)