import Node

class User:
    def __init__(self,name,age,departament,cod):
        self.name= name
        self.age = age
        self.departament = departament
        self.id = cod

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail =self.head

class Queue(LinkedList):
    
    def show(self):
        current =  self.head

        while(current is not None):
            print(current.value.__dict__)
            current = current.next
            
    def search(self,key):
        current = self.head
        
        while current is not None:
            if current.value.key == key:
                return current.value
            
            current = current.next
        return None

    def insert(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = self.head
            
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self,cod):
        
        current =  self.head 
        previous = None
        
        if self.head is None:
            return None
            
        while current is not None:
            
            if current.value.id == cod: 
                if previous is None:
                    self.head = current.next
                
                else: 
                    previous.next = current.next
                
                if current == self.tail:
                    self.tail = previous
                
                return current.value
            
            previous = current
            current = current.next
        
        return None

class Stack(LinkedList):
    
    def push(self,value):
        new_node = Node(value)
        current = self.head
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.head = new_node
            self.head.next = current
    
        print(f"{new_node.value.__dict__}\n adicionado")
        
    def pop(self):
        
        if self.head is None:
            return None
        
        current = self.head
        print(f"{current.value.__dict__}\n removido")
        self.head = current.next
        
        if self.head.next is None:
            self.tail = None
    

list_users = [
    ["pedro",21,"TI",22],
    ["Ana ",28,"Contabilidade",32],
    ["Luiz",40,"Financeiro",34],
    ["Claudia",26,"Rh",45],
    ]


queue_list =  Queue()

for data in list_users:
    user =  User(data[0],data[1],data[2],data[3])
    queue_list.insert(user)

queue_list.remove(32)
# queue_list.show()

queue_list.show()
