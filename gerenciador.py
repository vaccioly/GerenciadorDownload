from computador import *
from recurso import *
from jobs import *
import csv

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
                print('')
      
    def exportarComputador(self, nome ='Teste'):
        with open(r"~/GerenciadorDownload/Exportados/"+ nome + '.csv', 'a', newline='', encoding='utf-8') as csvfile:
            cabecalho = ['Identificação', 'IP', 'Descrição']
            arquivos = csv.DictWriter(csvfile, fieldnames=cabecalho)
            for pc in self.computadores:
                arquivos.writerow({'Identificação': pc.getId(), 'IP': pc.getIp(),'Descrição': pc.getDescricao()})
            #arquivos.writeheader() Linha para adicionar o cabecalho do arquivo    

    def importarComputador(self, arquivo):
        try:
            matriz = []
            with open(r"~/GerenciadorDownload/Exportados/"+arquivo + '.csv','r') as csvfile:
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
        with open(r"~/GerenciadorDownload/Exportados/"+arquivo + '.csv', 'a', newline='', encoding='utf-8') as csvfile:
            cabecalho = ['Descrição', 'Tamanho']
            arquivos = csv.DictWriter(csvfile, fieldnames=cabecalho)
            #arquivos.writeheader()
            for rec in self.recursos:
                arquivos.writerow({'Descrição': rec.getRecurso(), 'Tamanho': rec.getTamanho()})
           
    def importarRecurso(self,arquivo):
        try:
            documentos = []
            with open(r"~/GerenciadorDownload/Exportados/"+arquivo + '.csv','r', newline='') as csvfile:
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

# JOBS
    def povoamento(self):
        if len(self.jobs) == 0:
            print ('Jobs não associados, ou vazia')
        else:
            pv = self.__link / len(self.jobs)
            print(pv)
            return float(pv)

    def cadastrarJobs(self, pc, arquivo):
        try:
            pv = self.__link / len(self.jobs)
            job = Job(self.computadores[pc],self.recursos[arquivo],pv)
            self.jobs.append(job)
            return self.jobs
        except IndexError:
            raise gerenciadorException (f'Tipo de cadastro inválido!')
        except:
            raise
    
    def listarJobs(self):
        if len(self.jobs)==0:
            print('Jobs não cadastrados')
        for j in self.jobs:
            print (j)
            print('')

    def exportarJobs(self,arquivo):
        with open(r"~/GerenciadorDownload/Exportados/"+arquivo + '.csv', 'a', newline='', encoding='utf-8') as csvfile:
            cabecalho = ['Trabalhos', 'Arquivo','Banda']
            arquivos = csv.DictWriter(csvfile, fieldnames=cabecalho)
            #arquivos.writeheader()
            for job in self.jobs:
                arquivos.writerow({'Trabalhos': job.getJob(),'Arquivo': job.getArquivo(),'Banda': job.getBanda()})
                #Jobs: {self.__job}\nRecursos: {self.__arquivo}\nBanda: {self.__banda}
    
    def importarJobs(self,arquivo):
        try:
            trabalhos =[]
            with open(r"~/GerenciadorDownload/Exportados/"+arquivo + '.csv','r', newline='') as csvfile:
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