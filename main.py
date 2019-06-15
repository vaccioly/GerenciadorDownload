from gerenciador import *
from Menu import *
import time
#Esse é o programa principal do projeto do gerenciador de downloads
menu()
opcao = int(input('Digite uma opção: '))
while opcao > 0 and opcao <= 6:
	# Testa se a opcao fornecida no input for igual a 1 solicita as informaçoes do computador a ser cadastrado, verifica se ja existe lista de cadastro =[], caso não será efetuado o cadastro e se existente exibira uma mensagem print('pc ja cadastrado')
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
