import computador
import csv


class gerenciador:
    """A classe gerenciador de downloads administra a velocidade que cada computador terá disponível"""

    def __init__(self):
        pass

    def cadastrarComputador(self):
        pass

    def listarComputadores(self):
        pass

    def importarComputador(self, arquivo):
        with open(arquivo + '.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
            print('Importado com sucesso!')

    def exportarComputador(self, nome):
        with open(nome + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
            cabecalho = ['Identificação', 'IP', 'Recurso']
            write.writeheader = csv.DictWriter(csvfile, cabecalho=cabecalho)
            write.writeheader()
            write.writerow({'Identificação': self.__class__.__id, 'IP': '192.168.0.' + self.__class__.__ip,
                            'Recurso': self.__recurso})
            print('Exportado com sucesso!!!! ')

    def setLink(self, link):
        """Modifica a velocidade do link e retorna uma string dessa atualização"""
        self.__link = link
        return str(self.__link)

    def getLink(self):
        """retorna ao usuário uma string com o valor do link"""
        return f'Velocidade de coneção   {self.__link} Mb/s'

    def cadastrarRecurso(self):
        pass
