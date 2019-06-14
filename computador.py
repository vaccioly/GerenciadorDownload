class computador:
    """esta classe contem um id único para cada objeto instanciado imutável, e as propriedades ip e recurso que podem ser modificadas """
    id = -1



    def __init__(self, ip, recurso):
        cls.id += 1
        self.__id = cls.id
        self.__recurso = recurso
    def setRecurso(self,novo_recurso):
        self.__recurso = novo_recurso
        return f'{self.__recurso}'
    
    def getRecurso(self):
        
        return f'{self.__recurso}'

    def setIp(self,novo_ip):
        self.__ip = novo_ip
        return f'{self.__ip}'

    def getIp(self):
        
        return f'{self.ip}'
          

#teste

