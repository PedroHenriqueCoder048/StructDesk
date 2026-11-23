class TableHash:
    '''Aqui trabalhamos com o hash dos elementos
    '''
    
    class _Element:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            
            
    def __init__(self):
        self.__current_capacity = 5  ## capacidade / tamanho databela interna
        self.__internal_table = [Queue() for _ in range(self.__current_capacity)]
        self.__size = 0 ## quantdade de elementos no salvos na tabela hash

    def __len__(self):
        return self.__size
        
    def search_index(self,key):
        return self.__deterministic_hash(key) % self.__current_capacity
    
    @staticmethod
    def __check_key(key):
        return hash(key)
    
    @staticmethod
    def __deterministic_hash(key):
        certificate = str(key).encode()
        return int(sha256(certificate).hexdigest(),16)


        
    def __setitem__(self, key, value):
    
        index = self.search_index(key)
    
        element = self.__internal_table[index].search(key)
    
        if element is not None:
            element.value = value
            return
    
        new_element = self._Element(key, value)
    
        self.__internal_table[index].insert(new_element)
    
        self.__size += 1
        
    def __getitem__(self, key):
        index = self.search_index(key)
    
        element = self.__internal_table[index].search(key)
    
        if element is None:
            raise KeyError(key)
    
        return element.value
