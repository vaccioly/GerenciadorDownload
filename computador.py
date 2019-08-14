class Computador:
    """esta classe contem um id único para cada objeto instanciado imutável, e as propriedades ip e recurso que podem ser modificadas """
    __id = 0
    __ip = 0
    def __init__(self, descricao = None):

        self.__class__.__id += 1
        self.__class__.__ip += 1
        self.__descricao = descricao
        self.__ip = f'192.168.168.0.' + str(self.__class__.__ip)
        self.__id = self.__class__.__id

    def setIp(self,novo_ip):
        self.__ip = novo_ip
        #return f'{self.__ip}'


    def setId(self,novo_id):
        self.__id = novo_id

        return f'{self.__id}'
            

    def getIp(self):
        return self.__ip
        #return f'192.168.168.0.' + str(self.__class__.__ip)

    def getId(self):
        return self.__id

    def getDescricao(self):
        return f'{self.__descricao }'

    def setDescricao(self, novaDescricao):
        self.__descricao = novaDescricao

    def __str__(self):
        #return f'Id: {self.__id} \nIP: {self.__ip} \nDescrição: {self.__descricao}'
        #return f'Identificação: {self.__id}\nIp: {self.__ip}\nDescrição: {self.__descricao}'
        return f'{self.__descricao}; {self.__ip}'


"""#teste
c= computador()
print(c.getIp())
print(c.getId())
print(c.getRecurso())"""
