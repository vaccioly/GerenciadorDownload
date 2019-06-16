#import linkedlist
#import computador
class gerenciador:
    """A classe gerenciador de downloads administra a velocidade que cada computador terá disponível""" 

    def __init__(self):
        pass
       # self.__linked_list = linkedlist()
       # self.__link = link


    def cadastrarComputador(self):
        pass

    def cadastrarRecurso(self):
        pass


    def listarComputadores(self):
        pass
    
    def setLink(self,link):
        """Modifica a velocidade do link e retorna uma string dessa atualização"""
        self.__link = link
        return str(self.__link)

    def getLink(self):
        """retorna ao usuário uma string com o valor do link"""
        return f'Velocidade de coneção   {self.__link} Gb/s'



#teste
#gerenciador = gerenciador()

#print(gerenciador.setLink.__doc__)

