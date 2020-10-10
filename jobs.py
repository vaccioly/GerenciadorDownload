from computador import Computador

class JobException(Exception):

    """Classe de exceção generica"""





    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)
    
class BandaInexistenteException(Exception):
    """Classe de exceção lançada qu
    ando uma banda não existe
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


class RecursoInexistenteException(Exception):
    """Classe de exceção lançada quando uma recurso não existe
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)

class Job(Computador):
    def __init__(self,recurso, pc,banda=None):
        super.__init__()
        """O atributo "__concluido" indica que o job foi finalizado.""" 
        
        
        
        self.__banda = banda
        self.__concluido = False
        self.__pc = pc
        self.__recurso = recurso
       # self.__ip = Computado
       # r().getIp()
        #self.__id = Computador().getId()
        #self.__tamanho = self.Recurso.__tamanho 
       # self.__tipo_do_recurso = self.Recurso
    def setJob(self, novo_job):
        self.__job = novo_job
        #return f'{self.__recurso}'

    def getJob(self):
        return self.__job

    def setBanda(self, nova_banda):

        self.__banda = nova_banda
        #return f'{self.__tamanho}'

    def getBanda(self):
        return self.__banda
    
    def setArquivo(self, novo_arq):
        self.__arquivo = novo_arq
        #return f'{self.__tamanho}'

    def getArquivo(self):

        return self.__arquivo


    def decrementa(self):
        """esse método decrementa o tamanho do arquivoe retorna tamanho em str"""


       # if self.recurso.getArquivo
        
        if self.getBanda() == None:
            raise BandaInexistenteException('Banda inexistente cadastre alguma Banda')


        if self.recurso.__tamanho == 0:
            self.__concluido == True

        else:
            self.recurso.__tamanho = self.recurso.__tamanho - self.__banda

            return f'{self.recurso.__tamanho}'
        
    def __str__(self):
        # return f'Jobs: {self.__job}\nRecursos: {self.__arquivo}\nBanda: {self.__banda} Kbs'
        return f'{self.__job}; {self.__arquivo}'






