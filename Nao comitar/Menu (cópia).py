from datetime import date
"""Solicita a opção do Programa Principal"""
"""Funções do Menu!!!"""
def menu():
  print("Gerenciador de Downloads", date.today())
  print('-'*35)
  print(''' Opções:
1- Cadastro computadores:
2- Cadastro banda de Internet:
3- Importar computadores e /ou recursos
4- Exportar computadores e /ou recursos
5- Cadastrar / listar recursos
6- Cadastrar / remover jobs
0- Sair''')
  print('-'*35)

def clear():
  import os
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')