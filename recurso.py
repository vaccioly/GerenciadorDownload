from computador import Computador

class Recurso(Computador):
    def __init__(self, arquivo= None, tamanho= None):
        Computador.__init__(self)
        self.__recurso = arquivo
        self.__tamanho = tamanho
        


    def setRecurso(self, novo_recurso):
        self.__recurso = novo_recurso
        #return f'{self.__recurso}'

    def getRecurso(self):
        return f'{self.__recurso}'

    def setTamanho(self, tamanho):
        self.__tamanho = tamanho
        #return f'{self.__tamanho}'

    def getTamanho(self):
        return f'{self.__tamanho}'

    def __str__(self):
        return f'Arquivo: {self.__recurso}\nTamanho: {self.__tamanho} Kbps'
        #print (f'Descricao{self.__recurso} Tamanho {self.__tamanho} Kbs')



a = Recurso('circulo.jpg',100)

a.setIp('192.168.0.1')

a.setId('0')


print(a)
print(a.getIp())
print(a.getId())