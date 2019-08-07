import computador
import csv


class Gerenciador:
    """A classe gerenciador de downloads administra a velocidade que cada computador terá disponível"""

    def __init__(self):
        self.computadores = []
        self.recursos = []

    def cadastrarComputador(self,nome):
        pc = Computador(nome)
        self.computadores.append(pc)

    def listarComputadores(self):
        for c in self.computadores:
            print (c)

    def importarComputador(self, arquivo):
        with open(arquivo + '.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
            print('Importado com sucesso!')

    def exportarComputador(self, nome ='Teste'):
        with open(nome + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
            cabecalho = ['Identificação', 'IP', 'Descrição']
            arquivos = csv.DictWriter(csvfile, fieldnames=cabecalho)
            arquivos.writeheader()
            #write.writerow({'Identificacao':pc.getId()})
            #arquivos.writerow({'Identificação': Computador.__class__.__id, 'IP': '192.168.0.' + Computador.__class__.__ip,'Recurso': self.__recurso})
            #print('Exportado com sucesso!!!! ')
            for pc in self.computadores:
                #print(i.getIp(),i.getId())
                arquivos.writerow({'Identificação': pc.getId(), 'IP': pc.getIp(),'Descrição': pc.getDescricao()})
            print('Computadores exportado com sucesso!!!!')

    def setLink(self, link):
        """Modifica a velocidade do link e retorna uma string dessa atualização"""
        self.__link = link
        return str(self.__link)

    def getLink(self):
        """retorna ao usuário uma string com o valor do link"""
        return f'Velocidade de coneção   {self.__link} Mb/s'

    def cadastrarRecurso(self, novo_recurso, tamanhoNovo):
        self.recurso = novo_recurso
        self.tamanho = tamanhoNovo
        self.recursos.append(self.recurso)
        self.recursos.append(self.tamanho)

    def listarRecurso(self):
        return f'Arquivo {self.recurso}, tamanho {self.tamanho} Kbps'

"""adm = Gerenciador()
adm.cadastrarComputador('ifpb01')
adm.listarComputadores()
adm.cadastrarRecurso('documento.txt',1500)
print(adm.listarRecurso())
adm.exportarComputador()