class Recurso:
    def __init__(self, arquivo= None, tamanho= None):
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
        return f'Descricao{self.__recurso} Tamanho {self.__tamanho} Kbs'
        #print (f'Descricao{self.__recurso} Tamanho {self.__tamanho} Kbs')


'''rc = Recurso()
rc.setRecurso('bola.mp4')
print(rc.getRecurso())
rc.setTamanho(7480)
print(rc.getTamanho())'''