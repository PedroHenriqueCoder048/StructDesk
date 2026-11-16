class TableHash:
    '''Aqui trabalhamos com o hash dos elementos
    '''
    
    class _Element:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            
            
    def __init__(self):
        self.__current_capacity = 5  ## capacidade / tamanho databela interna
        self.__internal_table = [[] for _ in range(self.__current_capacity)]
        self.__size =0 ## quantdade de elementos no salvos na tabela hash

    def __len__(self):
        return self.__size
        
    def search_index(self,key):
        return hash(key) % self.__current_capacity
        
    def __setitem__(self,key,value):
        pass
        

chamado = TableHash()

chamado["cod"] ="1234"
chamado["solicitante"] = "Contabilidade"
chamado["solicitado"] = "TI"
chamado["prioridade"] ="baixo"

print(chamado)
