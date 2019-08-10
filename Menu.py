from datetime import date
"""Solicita a opção do Programa Principal"""
"""Funções do Menu!!!"""

def menu():
  print("Gerenciador de Downloads", date.today())
  print('-'*35)
  print(''' Opções:
1 - Cadastrar banda larga;
2 - Computadores;
3 - Recursos;
4 - Jobs;
5 - Iniciar downlads;
0 - Sair do programa;''')
  print('-'*35)

def menuComputador():
  print(''' Funções para Computadores
  1 - Cadastrar.
  2 - Listar.
  3 - Exportar.
  4 - Importar.
  0 - Voltar para menu principal''')
  print('-'*35) 

def menuRecursos():
  print('''Funções para Recursos/Arquivos.
  1 - Cadastrar.
  2 - Listar.
  3 - Exportar.
  4 - Importar.
  0 - Voltar para menu principal''')
  print('-'*35) 

def menuJobs():
  print('''Funções para Jobs.
  1 - Cadastrar.
  2 - Listar.
  3 - Exportar.
  4 - Importar.
  0 - Voltar para menu principal''')
  print('-'*35)
  
def clear():
  import os
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
