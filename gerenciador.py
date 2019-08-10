from computador import *
from recurso import *
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
        

    def importarComputador(self, arquivo):
        try:
            with open(arquivo + '.csv','r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    print(row)
            return
        except FileNotFoundError:
            raise gerenciadorException (f'Arquivo não encontrado ou não existe, favor verifique o nome!')
        except NameError:
            raise gerenciadorException(f'Arquivo não definido.')
        except:
            raise

    def exportarComputador(self, nome ='Teste'):
        with open(nome + '.csv', 'a', newline='', encoding='utf-8') as csvfile:
            cabecalho = ['Identificação', 'IP', 'Descrição']
            arquivos = csv.DictWriter(csvfile, fieldnames=cabecalho)
            for pc in self.computadores:
                arquivos.writerow({'Identificação': pc.getId(), 'IP': pc.getIp(),'Descrição': pc.getDescricao()})
            #arquivos.writeheader() Linha para adicionar o cabecalho do arquivo
            

    def setLink(self, link):
        """Modifica a velocidade do link e retorna uma string dessa atualização"""
        self.__link = link
        return str(self.__link)

    def getLink(self):
        """retorna ao usuário uma string com o valor do link"""
        return f'Velocidade de coneção   {self.__link} Mb/s'

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
        #return f'Arquivo {self.recurso}, tamanho {self.tamanho} Kbps'
        for c in self.recursos:
            print (c)
    
    def exportarRecurso(self,arquivo):
        with open(arquivo + '.csv', 'a', newline='', encoding='utf-8') as csvfile:
            cabecalho = ['Descrição', 'Tamanho']
            arquivos = csv.DictWriter(csvfile, fieldnames=cabecalho)
            #arquivos.writeheader()
            for rec in self.recurso:
                arquivos.writerow({'Descrição': rec.getRecurso(), 'Tamanho': rec.getTamanho()})
           

    def importarRecurso(self,arquivo):
        try:
            with open(arquivo + '.csv','r' newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            raise gerenciadorException (f'Arquivo não encontrado ou não existe, favor verifique o nome!')
        except NameError:
            raise gerenciadorException(f'Arquivo não definido.')
        except:
            raise

'''
##testes
#adm.cadastrarComputador('ifpb01')
#adm.listarComputadores()
#adm.importarComputador(testw)
#adm.cadastrarRecurso('documento.txt',1500)
#print(adm.listarRecurso())
#adm.exportarComputador('teste')
adm = Gerenciador()
print('Recurso')
adm.cadastrarRecurso('Bola.doc',7800)
adm.cadastrarRecurso('Sinuca.mp3',3309)
adm.listarRecurso()
print('Computador')
adm.cadastrarComputador('ifpb01')
adm.cadastrarComputador('ifpb')
adm.listarComputadores()
'''