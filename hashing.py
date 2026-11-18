from hashlib import sha256

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


        
    def __setitem__(self,key,value):
        self.__check_key(key)
        
        index = self.search_index(key)
        
        for element  in self.__internal_table[index]:
            if element.key == key:
                element.value = value 
                return 
            
        new_element = self._Element(key,value)
            
        self.__internal_table[index].append(new_element)
            
        self.__size += 1

chamado = TableHash()

chamado["cod"] ="1234"
chamado["solicitante"] = ["Contabilidade",1]
chamado["solicitado"] = "TI"
chamado["hora"] ="12:20"
chamado["prioridade"] ="baixo"
chamado["problema"] ="sem internet"

print(f"quantdade de elemento : {len(chamado)}")
