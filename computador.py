class Computador:
    """esta classe contem um id único para cada objeto instanciado imutável, e as propriedades ip e recurso que podem ser modificadas """
    __id = 0
    __ip = 0
    def __init__(self, descricao = None):

        self.__class__.__id += 1
        self.__class__.__ip += 1
        self.descricao = descricao
        self.ip = self.getIp()
        self.id = self.getId()


    def setRecurso(self, novo_recurso):
        self.__recurso = novo_recurso
        return f'{self.__recurso}'

    def getRecurso(self):
        return f'{self.__recurso}'

    def setIp(self,novo_ip):
        self.__ip = novo_ip
        return f'{self.__ip}'

    def getIp(self):
        return f'192.168.168.0.' + str(self.__class__.__ip)

    def getId(self):
        return f'{self.__class__.__id}'

    def getDescricao(self):
        return f'{self.descricao}'

    def setDescricao(self, novaDescricao):
        self.descricao = novaDescricao

    def __str__(self):
        return f'{self.id}, {self.ip}, {self.descricao}'
"""#teste
c= computador()
print(c.getIp())
print(c.getId())
print(c.getRecurso())"""
