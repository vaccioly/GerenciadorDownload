from recurso import *
from computador import *
from jobs import *
from listacircular import *
import csv
import time

listacircular =LinkedList()

class gerenciadorException(Exception):
        """Classe de exceção lançada quando uma violação de acesso aos elementos
        do gerenciador é identificado.
        """
        def __init__(self, msg):
            """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
            """
            super().__init__(msg)

class Gerenciador:
    """A classe gerenciador de downloads administra a velocidade que cada computador terá disponível"""

    def __init__(self):
        self.computadores = []
        self.recursos = []
        self.jobs =[]
        self.__link = 100
            
#BANDA LARGA
    def setLink(self, link):
        """Modifica a velocidade do link e retorna uma string dessa atualização"""
        self.__link = link
        #return str(self.__link)

    def getLink(self):
        """retorna ao usuário uma string com o valor do link"""
        return f'Velocidade de conexão {self.__link} Mb/s'

# COMPUTADORES
    def cadastrarComputador(self,nome):
        try:
            pc = Computador(nome)
            self.computadores.append(pc)
        except IndexError:
            raise gerenciadorException (f'Tipo de cadastro inválido!')
        except:
            raise
    
    def listarComputadores(self):
        if len(self.computadores) == 0:
            print('Lista de computadores vazia')
        else:
            for c in self.computadores:
                print (c)
      
    def exportarComputador(self, nome ='Teste'):
        with open(nome + '.csv', 'a', newline='', encoding='utf-8') as csvfile:
            cabecalho = ['Identificação', 'IP', 'Descrição']
            arquivos = csv.DictWriter(csvfile, fieldnames=cabecalho)
            for pc in self.computadores:
                arquivos.writerow({'Identificação': pc.getId(), 'IP': pc.getIp(),'Descrição': pc.getDescricao()})
            #arquivos.writeheader() Linha para adicionar o cabecalho do arquivo    

    def importarComputador(self, arquivo):
        try:
            matriz = []
            with open(arquivo + '.csv','r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    matriz.append(row)
                for i in range (len(matriz)):
                    self.computadores.append(Computador(matriz[i][2]))
                    print(row)
            return
        except FileNotFoundError:
            raise gerenciadorException (f'Arquivo não encontrado ou não existe, favor verifique o nome!')
        except NameError:
            raise gerenciadorException(f'Arquivo não definido.')
        except:
            raise            

# RECURSOS
    def cadastrarRecurso(self, novo, tamanho):
        rec = Recurso(novo, tamanho)
        self.recursos.append(rec)
        '''self.recurso = novo_recurso
        self.tamanho = tamanhoNovo
        self.recursos.append(self.recurso)
        self.recursos.append(self.tamanho)
        pc = Computador(nome)
        self.computadores.append(pc)'''
        
    def listarRecurso(self):
        if len(self.recursos) ==0:
            print ('Lista recursos vazia, favor efetuar o cadstro')
        else:
            for c in self.recursos:
                print (c)
    
    def exportarRecurso(self,arquivo):
        with open(arquivo + '.csv', 'a', newline='', encoding='utf-8') as csvfile:
            cabecalho = ['Descrição', 'Tamanho']
            arquivos = csv.DictWriter(csvfile, fieldnames=cabecalho)
            #arquivos.writeheader()
            for rec in self.recursos:
                arquivos.writerow({'Descrição': rec.getRecurso(), 'Tamanho': rec.getTamanho()})
           
    def importarRecurso(self,arquivo):
        try:
            documentos = []
            with open(arquivo + '.csv','r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    documentos.append(row)
                for i in range (len(documentos)):
                    self.recursos.append(Recurso(documentos[i][2]))
                    print(row)
            return        
        except FileNotFoundError:
            raise gerenciadorException (f'Arquivo não encontrado ou não existe, favor verifique o nome!')
        except NameError:
            raise gerenciadorException(f'Arquivo não definido.')
        except:
            raise

   # def povoamento(self):
    def divideBanda(self):

        if (len(self.jobs)) == 0:
            print ('Jobs não associados, ou vazia')
        else:
            pv = (self.__link * 1024) / (len(self.jobs))
            return float(pv)
# JOBS


    def cadastrarJobsv1(self, pc, arquivo):
        try:
            temp1 = 1- pc
            temp2 = 1 - arquivo
            job = Job(self.computadores[temp1],self.recursos[temp2])
            self.jobs(job)
            return self.jobs
        except IndexError:
            raise gerenciadorException (f'Tipo de cadastro inválido!')
        except:
            raise

    def cadastrarJobs(recurso,pc):
        try:
            novo_job = jobs(recurso,pc)
            return novo_job
        except IndexError:
            raise gerenciadorException (f'Tipo de cadastro inválido!')
        except:
            raise

        


    
    def listarJobs(self):
        if len(self.jobs)==0:
            print('Jobs não cadastrados')
        for j in self.jobs:
            print (j)

    def exportarJobs(self,arquivo):
        with open(arquivo + '.csv', 'a', newline='', encoding='utf-8') as csvfile:
            cabecalho = ['Trabalhos', 'Arquivo','Banda']
            arquivos = csv.DictWriter(csvfile, fieldnames=cabecalho)
            #arquivos.writeheader()
            for job in self.jobs:
                arquivos.writerow({'Trabalhos': job.getJob(),'Arquivo': job.getArquivo(),'Banda': job.getBanda()})
                #Jobs: {self.__job}\nRecursos: {self.__arquivo}\nBanda: {self.__banda}
    
    def importarJobs(self,arquivo):
        try:
            trabalhos =[]
            with open(arquivo + '.csv','r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    trabalhos.append(row)
                for i in range (len(trabalhos)):
                    self.jobs.append(Jobs(trabalhos[i][2]))
                    print(row)
            return
        except FileNotFoundError:
            raise gerenciadorException (f'Arquivo não encontrado ou não existe, favor verifique o nome!')
        except NameError:
            raise gerenciadorException(f'Arquivo não definido.')
        except:
            raise

    def iniciarDownloads(jobs_simulacao,banda,jobs_lista):
        
        banda_dividida = self.divideBanda()

        

        while len(jobs_lista) != 0:
            job = jobs.pop()
            job.setLink(banda_dividida)
            jobs_simulacao.inserirFinal(job)
            jobs_em_execucao = jobs_simulacao()

        print(f'banda para cada pc é : {banda_dividida}')
        
       
        job_da_rodada = jobs_simulacao.cycle()
        print(f'falta ser baixado: {job_da_rodada.decrementa} do HOST : {self.job_da_rodada.__pc}')
        while jobs_em_execucao != True:

            clear()
            print('pressione qualquer tecla pra continuar...')
            input()


            job_da_rodada = listacircular.cycle()
            if job_da_rodada.__concluido == True:
                index_da_rodada = listacircula.getIndexDoElemento()
                listacircular.remover(index_da_rodada)
            else:
                print(f'falta ser baixado: {job_da_rodada.decrementa} do HOST : {self.job_da_rodada.__pc}')

            



        





        
    
   
                

'''
adm= Gerenciador()
adm.cadastrarComputador('ifpb01')
adm.listarComputadores()
#adm.importarComputador(testw)
adm.cadastrarRecurso('documento.txt',1500)
print(adm.listarRecurso())
adm.exportarComputador('teste')
#adm = Gerenciador()
print('Recurso')
adm.cadastrarRecurso('Bola.doc',7800)
adm.cadastrarRecurso('Sinuca.mp3',3309)
adm.listarRecurso()
print('Computador')
adm.cadastrarComputador('ifpb01')
adm.cadastrarComputador('ifpb')
adm.listarComputadores()
print(adm.getLink())
adm.setLink(50)
print(adm.getLink())
adm = Gerenciador()
adm.cadastrarComputador('vinicius')
adm.cadastrarRecurso('libreoffice.tar',3500)
adm.cadastrarJobs(0,0)
#adm.listarJobs()
adm.cadastrarComputador('ggrr')
adm.cadastrarRecurso('doc.doc',4000)
adm.cadastrarJobs(1,1)
adm.listarJobs()
'''
