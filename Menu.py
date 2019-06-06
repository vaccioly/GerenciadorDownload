from datetime import date
"""Solicita a opção do Programa Principal"""
'''Funções do Menu!!!'''


#Complementar as opçoes solicitadas no print do menu

while True:

  print("Gerenciador de Downloads",date.today())
  print('-'*35)
  print('''        Opções: 
          1- Cadastro computadores: 
          2- Cadastro Banda (Velocidade):
          3- Importar
          4- Exportar
          5- 
          0- Sair
  ''',end='')
  print('-'*35)
  opcao=int(input('Digite uma opção: '))

"""FALTA Implementar apartir daqui"""


  while opcao !=0:
      '''Testa se a opcao fornecida no input for igual a 1 solicita as informaçoes do computador a ser cadastrado, verifica se ja existe lista de cadastro =[], caso não será efetuado o cadastro e se existente exibira uma mensagem print('pc ja cadastrado')
  #1 - cadastro
      if opcao==1:
          cadastro
          nome=str(input("Digite o nome: "))
          cadastro.append(nome.title())
          print = ('Cadastro Efetuado com sucesso')
          break
          '''numeroconta=input('Digite numero da conta 3 a 7 digitos: ')
          while verifica_conta(digitoVerificador(numeroconta))==1 or len(numeroconta)<3 or len(numeroconta)>7:
              print('Numero da conta fora dos parametros')
              numeroconta = input('Diite numero da conta 3 a 7 digitos: ')
          deposito.append(digitoVerificador(numeroconta))
          lista.append(digitoVerificador(numeroconta))
          senha=input("Digite senha de 8 digitos: ")
          while len(senha)!=8:
              print("Senha não contem 8 digitos")
              senha = input("Digite senha de 8 digitos: ")
          else:
              lista.append(senha)
          depositar=str(input('Deseja executar um deposito? s/n: '))
          if depositar=='s':
              valor=float(input("Valor a ser depositado? "))
              deposito.append(valor)
              lista.append(valor)
              lista.append('True')
          else:
              lista.append(0.0)
              lista.append('True')
              deposito.append(0.0)
          clientes.append(lista)
          saldo_lista.append(deposito)
          print('\n')
          print('-'*35)
          print("Conta criada com sucesso!")
          print('Titular: ', get_nome(digitoVerificador(numeroconta)))
          print('O numero da conta é: ',digitoVerificador(numeroconta))
          print('Saldo Atual: ',get_saldo(digitoVerificador(numeroconta)))
          print('-' *35)
          print('\n')
          print('Banco da Programação!  ', date.today())
          print('-' * 35)
          print('''    '''Opções:
                        1- Cadastro: 
                        2- Saque: 
                        3- Deposito: 
                        4- Tev: 
                        5- Extrato
                        0- Sair, end='')
         # print('-' * 35)
          #opcao = int(input('Digite uma opção: '))'''

  #2- saque

      elif opcao==2:
          numeroconta=input('Digite numero da conta 3 a 7 digitos: ')
          while verifica_conta(numeroconta)==0 or ativo(numeroconta)==2:
              print("Numero conta Invalida")
              numeroconta = input('Digite numero da conta 3 a 7 digitos: ')
          senha = input("Digite senha de 8 digitos: ")
          while verifica_senha(numeroconta,senha)==0:
              print("Senha Invalida")
              senha = input("Digite senha de 8 digitos: ")
          valor=float(input("Valor do saque: "))
          while get_saldo(numeroconta)<valor:
              print("saldo insuficiente!", get_saldo(numeroconta))
              valor=float(input('Valor do saque: '))
          else:
              for i in range (len(clientes)):
                  if clientes[i][1]==numeroconta:
                      x=i
              clientes[x][3]-=valor
              texto = 'D - Saque'+str(valor)+'  '+str(get_saldo(numeroconta))
              extrato(numeroconta,texto)
              print("Saque efetuado com sucesso!")
              print('Novo Saldo = ',clientes[x][3])
              print('Banco da Programação!  ', date.today())
              print('-' * 35)
              print('''        Opções: 
                      1- Cadastro: 
                      2- Saque: 
                      3- Deposito: 
                      4- Tev: 
                      5- Extrato
                      0- Sair
              ''', end='')
              print('-' * 35)
              opcao=int(input('Digite uma opção: '))

  # 3- deposito
      elif opcao==3:
          numeroconta = input('Digite numero da conta 3 a 7 digitos: ')
          while verifica_conta(numeroconta)==0 or ativo(numeroconta)==2:
              print("Conta invalida ou inativa")
              numeroconta = input('Digite numero da conta 3 a 7 digitos: ')
          senha = input("Digite senha de 8 digitos: ")
          while  verifica_senha(numeroconta,senha)==0:
              print("Senha incorreta")
          valor=float(input("Valor a ser depositado"))
          for i in range (len(clientes)):
              if clientes[i][1]==numeroconta:
                  x=i
          clientes[x][3]+=valor
          texto='C - deposito '+str(valor)+' '+str(get_saldo(numeroconta))
          extrato(numeroconta,texto)
          print('Deposito efetuado com sucesso!')
          print("Novo saldo =", clientes[x][3])
          print('Banco da Programação!  ', date.today())
          print('-' * 35)
          print('''        Opções: 
                  1- Cadastro: 
                  2- Saque: 
                  3- Deposito: 
                  4- Tev: 
                  5- Extrato
                  0- Sair
          ''', end='')
          print('-' * 35)
          opcao = int(input('Digite uma opção: '))

  #4- tev
      elif opcao==4:
          numeroconta=input('Digite numero da conta origem: ')
          while verifica_conta(numeroconta)==0 or ativo(numeroconta)==2:
              print('Conta invalida ou inativa.')
              numeroconta=input('Digite numero da conta origem: ')
          senha=input("Digite senha de 8 digitos: ")
          while verifica_senha(numeroconta,senha)==0:
              print("Senha Invalida")
              senha = input("Digite senha de 8 digitos: ")
          valor=float(input("Valor da transferencia: "))
          destino = input('Digite numero da conta destino: ')
          while verifica_conta(destino) == 0 or ativo(destino) == 2:
              print('Conta invalida ou inativa.')
              destino = input('Digite numero da conta destino: ')
          while get_saldo(destino) < valor:
              print("saldo insuficiente!","Saldo disponivel", get_saldo(numeroconta))
              valor=float(input("Valor a ser transferido? "))
          else:
              for i in range (len(clientes)):
                  if clientes[i][1]==numeroconta:
                      x=i
              clientes[x][3]-=valor
              texto = 'D - TEV'+str(valor)+'  '+str(get_saldo(numeroconta))
              extrato(numeroconta,texto)
              for i in range (len(clientes)):
                  if clientes[i][1]==destino:
                      x=i
              clientes[x][3]+=valor
              texto='C - TEV '+str(valor)+' '+str(get_saldo(numeroconta))
              extrato(destino,texto)
              print('Transferencia efetuada com sucesso!')
              print('''
              Opções: 
              1- Cadastro: 
              2- Saque: 
              3- Deposito: 
              4- Tev: 
              5- Extrato
              0- Sair
  ''', end='')
              print('-' * 20)
              opcao = int(input('Digite uma opção: '))
  #5- extrato
      elif opcao==5:
          numeroconta = input('Digite numero da conta 3 a 7 digitos: ')
          while verifica_conta(numeroconta)==0 or ativo(numeroconta)==2:
              print("Conta invalida ou inativa ")
              numeroconta = input('Digite numero da conta 3 a 7 digitos: ')
          senha = input("Digite senha de 8 digitos: ")

          while verifica_senha(numeroconta, senha) == 0:
              print('senha incorreta')
              senha = input("Digite senha de 8 digitos: ")
          print('\n')
          print('Banco da Programação!  ',date.today())
          print('-' * 20)
          print(numeroconta, '     ', get_nome(numeroconta))
          print(' ' * 20, 'saldo=', get_saldoInicial(numeroconta))
          for i in range(len(saldo_lista)):
              if saldo_lista[i][0] == numeroconta:
                  x = i
          while len(saldo_lista[x]) < 3:
              print('\n')
              print('       não há transaçoes')
              print('\n')
              break
          print('\n')
          for i in range(len(saldo_lista)):
              for j in range(len(saldo_lista[i])):
                  d = saldo_lista[x][2:]
          for i in range(len(d)):
              print(d[i])
          print('\n')
          print(' ' * 20, 'saldo=', get_saldo(num))
          print('-' * 20)
          opcao = int(input('Digite uma opção: '))
  #0 - sair
      elif opcao==0:
          print("Programa encerrado com sucesso! ")
