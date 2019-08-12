class Job:
    def __init__(self, pc,recurso, banda):
        self.__job = pc
        self.__arquivo = recurso
        self.__banda = banda

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

    def __str__(self):
        return f'Jobs: {self.__job}\nRecursos: {self.__arquivo}\nBanda: {self.__banda} Kbs'
    
    

