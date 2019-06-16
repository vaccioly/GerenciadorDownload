from gerenciador import *
from Menu import *
import time
#Esse é o programa principal do projeto do gerenciador de downloads

while True:
	try:
		menu() #Imprime na tela as opçoes das funções permitidas pelo sistema
		opcao = int(input('Digite uma opção: '))
		# 1 - cadastro
		if opcao == 1:
			print('Cadastro Efetuado com sucesso')
			time.sleep(3)
			clear()
			menu()
			opcao = int(input('Digite uma opção: '))
		# 2- Cadastrar banda de internet
		if opcao == 2:
			link = gerenciador()
			valor = int(input('Velecidade que deseja cadastrar: '))
			link.setLink(valor)
			print(link.getLink())
			print("Banda Cadastrada com sucesso!")
			time.sleep(3)
			clear()
			menu()
			opcao = int(input('Digite uma opção: '))

		# 3-Importar computadores e /ou recursos
		if opcao == 3:
			print('Importacao de dados efetuado com sucesso!')
			time.sleep(3)
			clear()
			menu()
			opcao = int(input('Digite uma opção: '))

		# 4- Exportar computadores e /ou recursos
		if opcao == 4:
			print('Dados exportados com sucesso!')
			time.sleep(3)
			clear()
			menu()
			opcao = int(input('Digite uma opção: '))
		# 5- Cadastro / listar os recurso
		if opcao == 5:
			print("Gerenciador de Downloads", date.today())
			time.sleep(3)
			clear()
			menu()
			opcao = int(input('Digite uma opção: '))
		# 6- Cadastrar / remover jobs
		if opcao == 6:
			print('Jobs cadastrados / removido com sucesso !')
			time.sleep(3)
			clear()
			menu()
			opcao = int(input('Digite uma opção: '))
		# 0 - sair (Encerra o sistema)
		if opcao == 0:
			print("Programa encerrado com sucesso! ")
			break
		else:
			print('Valor fora do intervalo, Apenas opçoes de 0 a 6!!')
			time.sleep(3)
			clear()
	except ValueError:
		print('Letras e caracteres nao permitido, apenas numeros inteiros')
		time.sleep(3)
		clear()
	except TypeError:
		print('Tipo digitado invalido')
		time.sleep(3)
		clear()
	except:
		print('Nossos engenheiro irao analisar o problema!')
		time.sleep(3)
		clear()