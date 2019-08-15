from gerenciador import *
from Menu import *
from listacircular import *
import time
#Esse é o programa principal do projeto do gerenciador de downloads
computadores = []
recursos = []
jobs_lista = []
adm = Gerenciador()
while True:
	try:
		menu() #Imprime na tela as opçoes das funções permitidas pelo sistema
		opcao = int(input('Digite uma opção: '))
		# 1- Cadastrar banda larga
		if opcao == 1:
			menuBandaLarga()
			larga = int(input('Digite uma opção: '))
			# Cadastrar banda larga
			if larga == 1:
				valor = float(input('Velocidade que deseja cadastrar em Mbps: '))
				adm.setLink(valor)
				print("Banda larga cadastrada com sucesso!")
				time.sleep(3)
				clear()
				continue
			# Listar banda larga cadastrada
			if larga == 2:
				print(adm.getLink())
				time.sleep(3)
				clear()
				continue
			# Voltar ao menu anterior
			if larga == 0:
				print('Voltando ao menu anterior!')
				time.sleep(3)
				clear()
				continue
		# 2 - Computadores
		if opcao == 2:
			menuComputador()
			computer = int(input('Digite uma opção: '))
			# 1 - Cadastrar computador;
			if computer == 1:
				nome = input('Nome do computador: ')
				adm.cadastrarComputador(nome)
				adm.listarComputadores()
				print('Cadastro Efetuado com sucesso')
				time.sleep(3)
				clear()
				continue
			
			# 2 - Listar Computadores
			if computer == 2:
				adm.listarComputadores()
				time.sleep(3)
				clear()
				continue

			# 3 - Exportar computadores
			if computer == 3:
				arq = input('Qual nome do arquivo(sem extensao)? ')
				adm.exportarComputador(arq)
				print('Computadores exportados com sucesso!')
				time.sleep(3)
				clear()
				continue

			# 4 - Importar computadores
			if computer == 4:
				arq = input('Arquivo que deseja importar? ')
				adm.importarComputador(arq)
				print('Importacao de dados efetuado com sucesso!')
				time.sleep(3)
				clear()
				continue 

			# 0 - Voltar para menu principal
			if opcao == 0:
				print('Voltando ao menu Principal')
				time.sleep(3)
				clear()
				continue
		
			
		#Cadastro de RECURSOS
		if opcao == 3:
			menuRecursos()
			arquivo = int(input('Digite uma opção: '))
			#1 - Cadastrar recursos
			if arquivo == 1:
				nome = input('Informe o nome do arquivo que deseja cadastrar: ')
				tamanho = float(input('Tamanho do arquivo em Mbps: '))
				adm.cadastrarRecurso(nome, tamanho)
				print('Arquivo cadastrado com sucesso!')
				time.sleep(3)
				clear()
				continue
			#2 - Listar recursos
			if arquivo == 2:
				adm.listarRecurso()
				time.sleep(3)
				clear()
				continue
			#3 - Exportar recursos
			if arquivo == 3:
				nome = input('Nome que deseja salvar a lista de Recursos: ')
				adm.exportarRecurso(nome)
				print('Arquivo exportado com sucesso!!')
				time.sleep(3)
				clear()
				continue
			#4 - Importar recursos
			if arquivo == 4:
				nome = input('Nome da lista de Recursos a ser importada: ')
				adm.importarRecurso(nome)
				print('Recursos importados com sucesso!!')
				time.sleep(3)
				clear()
				continue

			#0 - Voltar para menu principal
			if arquivo ==0:
				print('Voltando ao menu Principal')
				time.sleep(3)
				clear()
				continue

		
	#Cadastro de Jobs
		if opcao == 4:
			menuJobs()
			trabalho = int(input('Digite uma opção: '))
			#1 - Cadastrar Jobs
<<<<<<< HEAD
			if opcao == 1:
				print(adm.listarRecurso())
				opcao = input('digite qual recurso quer (1,2,3...): ')
				for i in recursos:
					if opcao == i:
						computador = computadores[i]

				print(adm.listarComputadores())

				opcao = input('digite qual pc quer (1,2,3...): ')
				for i in recursos:
					if opcao == i:
						recurso = recursos[i]


				

				

				
				novo_job = adm.cadastrarJobs(recurso, pc)
				jobs_lista.append(novo_job)
=======
			if trabalho == 1:
				idComputador = int(input('Id do computador: '))
				idRecurso = int(input('Id Recurso: '))
				adm.cadastrarJobs(idComputador, idRecurso)
>>>>>>> 32394c9583b120df1866ce2364d1c7d9172a100b
				print('Jobs cadastrado com sucesso!')
				time.sleep(3)
				clear()
				continue
			#2 - Listar Jobs
			if trabalho == 2:
				adm.listarJobs()
				time.sleep(5)
				clear()
				continue
			#3 - Exportar Jobs
			if trabalho == 3:
				nome = input('Nome que deseja salvar a lista de Recursos: ')
				adm.exportarJobs(nome)
				print('Arquivo exportado com sucesso!!')
				time.sleep(3)
				clear()
				continue
			#4 - Importar Jobs
			if trabalho == 4:
				nome = input('Nome da lista de Recursos a ser importada: ')
				adm.importarJobs(nome)
				print('Recursos importados com sucesso!!')
				time.sleep(3)
				clear()
				continue

			#0 - Voltar para menu principal
			if trabalho ==0:
				print('Voltando ao menu Principal')
				time.sleep(3)
				clear()
				continue

		#5 - Iniciar downloads
		if opcao == 5:
<<<<<<< HEAD
			banda = adm.getLink()
			jobs_simulacao = listacircular

			adm.iniciarDownloads(jobs_simulacao,banda,jobs_lista)

			

=======
			print('Downloads iniciados')
			time.sleep(3)
			clear()
			continue
>>>>>>> 32394c9583b120df1866ce2364d1c7d9172a100b

		# 0 - sair (Encerra o sistema)
		if opcao == 0:
			print("Programa encerrado com sucesso! ")
			break
		if opcao < 0:
			print("Números negativos não permitido!")
			time.sleep(4)
			clear()
			continue
		else:
			print('Opção não disponivel, Tente novamente!!')
			time.sleep(4)
			clear()
	except ValueError:
		print('Letras e caracteres nao permitido, apenas numeros inteiros')
		time.sleep(3)
		clear()
	except TypeError:
		print('Tipo digitado invalido')
		time.sleep(3)
		clear()
	except NameError:
		print('Nome não definido, favor verifique a ortografia e tente novamente!')
		time.sleep(3)
		clear()
	except KeyboardInterrupt:
		print('Voltar ao menu Principal!')
		menu()
		time.sleep(3)
		clear()
	except:
		print('Nossos engenheiros irão analisar o problema!')
		time.sleep(3)
		clear()
