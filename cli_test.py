import os
import argparse
import pathlib

print('Corretor de provas')
print('O usuario deve passar os paths referentes as pastas das imagens dos gabaritos e depois o arquivo da prova a ser corrigida')
# print('Dê o endereço da pasta onde os gabaritos estão contidos')
imagesPaths = input('Pasta dos gabaritos: ') # pasta que tem todas as provas
# os gabaritos precisam ter um nome específico nelas
lista_files = os.listdir(imagesPaths);
tiposGabaritos = {}
for gabaritoPath in lista_files:
    tipo = gabaritoPath.split('.')[0][-1]
    # print(tipo)
    tiposGabaritos[tipo] = gabaritoPath

pathProvaRespondida = input('path para a prova: ')
tipoRespondido = input('Tipo da prova respondida: ')
# path certinho para imagem da prova
pathProvaRespondida = os.path.abspath(pathProvaRespondida)
pathGabaritoEscolhido = os.path.abspath(tiposGabaritos[tipoRespondido])

print('path da prova: ', pathProvaRespondida)
print('path gabarito escolhido: ', pathGabaritoEscolhido)
# print(type(tipoRespondido))

# print(tiposGabaritos)
