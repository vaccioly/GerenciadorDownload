

class Node:

    '''Classe que representa um nó na memória
    '''
    def __init__(self,data):
        self.data = data
        self.next = None

    def insertNext(self, data):
        if self.next == None:
            self.next = Node(data)	

    def getNext(self):
        return self.next

    def setData(self,newValue):
        self.data = newValue

    def getData(self):
        return self.data

    def __str__(self):
        return str(self.data)

    def hasNext(self):
        return self.next != None


class PosicaoInvalidaException(Exception):
    """Classe de exceção lançada quando uma violação no acesso aos elementos
       da lista, indicado pelo usuário, é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


class ValorInexistenteException(Exception):
    def __init__(self,msg):
        super().__init__(msg)   


      
	    
'''
Esta classe implementa uma estrutura Lista Simplesmente Encadeada
'''
class LinkedList:
    """elemento atual é o objeto que está no ciclo"""
    ciclo= 0
    index_do_elemento_atual = -1
    # constructor initializes an empty LinkedList of integers
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def estaVazia(self):
        return True if self.__tamanho ==0 else False

    def tamanho(self):
        return self.__tamanho

    def elemento(self, posicao):


        try:
            assert posicao > 0

            if (self.estaVazia()):
                raise PosicaoInvalidaException(f'Lista vazia')

            cursor = self.__head
            contador = 1
            while( (cursor != None) and (contador < posicao) ):
                cursor = cursor.next
                contador += 1

            if ( cursor != None ):
                return cursor.data
        
            raise PosicaoInvalidaException(f'A lista não contém {posicao} elementos. O máximo é {self.__tamanho}')


        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser 0 (zero) ou um número negativo')
        except:
            raise

    
    def busca(self, valor):
        if (self.estaVazia()):
            raise PosicaoInvalidaException(f'Lista vazia')

        cursor = self.__head
        contador = 1

        while( cursor != None ):
            if( cursor.data == valor):
                return contador
            cursor = cursor.next
            contador += 1
            
        raise ValorInexistenteException(f'O valor {valor} não está armazenado na lista')

    def inserir(self, posicao, valor ):

        try:
            assert posicao > 0

            # CONDICAO 1: insercao se a lista estiver vazia
            if (self.estaVazia()):
                print(f'Estou vazia e a posicao eh {posicao}')
                if ( posicao != 1):
                    print('Entrei no posicao = 1')
                    raise PosicaoInvalidaException(f'A lista esta vazia. A posicao correta para insercao é 1.')

                self.__head = Node(valor)
                self.__tamanho += 1
                return
            
            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            if ( posicao == 1):
                novo = Node(valor)
                novo.next = self.__head
                self.__head = novo
                self.__tamanho += 1
                return

            # CONDICAO 3: insercao apos a primeira posicao em lista nao vazia
            cursor = self.__head
            contador = 1
            while ( (contador < posicao-1) and  (cursor != None)):
                cursor = cursor.next
                contador += 1

            if ( cursor == None ):
                raise PosicaoInvalidaException(f'A posicao {posicao} é invalida para a atual lista')

            novo = Node(valor)
            novo.next = cursor.next
            cursor.next = novo
            self.__tamanho += 1

        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo ou 0 (zero)')
        except:
            raise



    def inserirFinal(self,valor):
        posicao = self.tamanho() + 1
        
        self.inserir(posicao,valor)


    def remover(self, posicao):
 
        try:
            assert posicao > 0 

            if( self.estaVazia() ):
                raise PosicaoInvalidaException(f'Não é possível remover de uma lista vazia')

            cursor = self.__head
            contador = 1

            while( (contador <= posicao-1) and (cursor != None) ) :
                anterior = cursor
                cursor = cursor.next
                contador+=1

            if ( cursor == None ):
                raise PosicaoInvalidaException(f'Posicao {posicao} invalida para remoção')

            data = cursor.data

            if( posicao == 1):
                self.__head = cursor.next
            else:
                anterior.next = cursor.next

            self.__tamanho -= 1
            return data
        
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo')
        except:
            raise


    def getCycle(self):
        
        return f"Ciclo atual : {self.ciclo}"


    def imprimir(self):
        print('Lista: ',end='')

        cursor = self.__head

        print('[ ',end='')
        while( cursor != None ):
            print(f'{cursor.data}, ', end='')
            cursor = cursor.next
        print(']')
        

        
    def __str__(self):

        str = 'Lista: [ '

        cursor = self.__head

        while( cursor != None ):
            str += f'{cursor.data}, '
            cursor = cursor.next
        str += ']'
        return str

    def cycle(self):
        if self.estaVazia() == none:
            raise PosicaoInvalidaException("a lista estÀ vazia")
        tamanho = self.tamanho()
        index_do_elemento = self.index_do_elemento_atual

        index_do_elemento + 1
        if index_do_elemento > tamanho:
            index_do_elemento == -1
            self.ciclo == 1
        return LinkedList.elemento(index_do_elemento)



