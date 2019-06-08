from datetime import date
"""Solicita a opção do Programa Principal"""
"""Funções do Menu!!!"""
while True:
    print("Gerenciador de Downloads", date.today())
    print('-'*35)
    print(''' Opções:
1- Cadastro computadores:
2- Cadastro banda de Internet:
3- Importar computadores e /ou recursos
4- Exportar computadores e /ou recursos
5- Cadastrar / listar recursos
6- Cadastrar / remover jobs
0- Sair''', end='')
    print('-'*35)
    opcao = int(input('Digite uma opção: '))
    while opcao != 0:
        '''Testa se a opcao fornecida no input for igual a 1 solicita as informaçoes do computador a ser cadastrado, verifica se ja existe lista de cadastro =[], caso não será efetuado o cadastro e se existente exibira uma mensagem print('pc ja cadastrado')'''
        # 1 - cadastro
        if opcao == 1:
            print = ('Cadastro Efetuado com sucesso')
            # print("Gerenciador de Downloads",date.today())
            print('-'*35)
            print(''' Opções:
1- Cadastro computadores:
2- Cadastro banda de internet:
3- Importar computadores e /ou recursos
4- Exportar computadores e /ou recursos
5- Cadastrar / listar recursos
6- Cadastrar / remover jobs
0- Sair''', end='')
            print('-'*35)
            opcao = int(input('Digite uma opção: '))
            while opcao != 0:
                # print("Gerenciador de Downloads",date.today())
                print('-'*35)
                print(''' Opções:
1- Cadastro computadores:
2- Cadastro banda de internet:
3- Importar computadores e /ou recursos
4- Exportar computadores e /ou recursos
5- Cadastrar / listar recursos
6- Cadastrar / remover jobs
0- Sair''')
                print('-'*35)
                opcao = int(input('Digite uma opção: '))

  # 2- Cadastrar banda de internet

        elif opcao == 2:
            print("Banda Cadastrada com sucesso!")
            print("Gerenciador de Downloads", date.today())
            print('-'*35)
            print(''' Opções:
1- Cadastro computadores:
2- Cadastro banda de internet:
3- Importar computadores e /ou recursos
4- Exportar computadores e /ou recursos
5- Cadastrar / listar recursos
6- Cadastrar / remover jobs
0- Sair''', end='')
print('-'*35)
opcao = int(input('Digite uma opção: '))
 # 3-Importar computadores e /ou recursos
        elif opcao == 3:
          print('Importacao de dados efetuado com sucesso!')
          print("Gerenciador de Downloads", date.today())
          print('-'*35)
          print(''' Opções:
1- Cadastro computadores:
2- Cadastro banda de internet:
3- Importar computadores e /ou recursos
4- Exportar computadores e /ou recursos
5- Cadastrar / listar recursos
6- Cadastrar / remover jobs
0- Sair''', end='')
print('-'*35)
opcao = int(input('Digite uma opção: '))
 # 4- Exportar computadores e /ou recursos
    elif opcao == 4:
        print('Dados exportados com sucesso!')
        print("Gerenciador de Downloads", date.today())
        print('-'*35)
        print(''' Opções:
1- Cadastro computadores:
2- Cadastro banda de internet:
3- Importar computadores e /ou recursos
4- Exportar computadores e /ou recursos
5- Cadastrar / listar recursos
6- Cadastrar / remover jobs
0- Sair''', end='')
print('-'*35)
opcao = int(input('Digite uma opção: '))
  # 5- Cadastro / listar os recurso
    elif opcao == 5:
        print("Gerenciador de Downloads", date.today())
        print('-'*35)
        print(''' Opções:
1- Cadastro computadores:
2- Cadastro banda de internet:
3- Importar computadores e /ou recursos
4- Exportar computadores e /ou recursos
5- Cadastrar / listar recursos
6- Cadastrar / remover jobs
0- Sair''', end='')
print('-'*35)
opcao = int(input('Digite uma opção: '))
   # 6- Cadastrar / remover jobs
   elif opcao == 6:
        print('Jobs cadastrados / removido com sucesso !')
  # 0 - sair (Encerra o sistema)
    elif opcao ==0:
        print("Programa encerrado com sucesso! ")
