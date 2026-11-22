class User:
    def __init__(self,name,age,departament):
        self.name= name
        self.age = age
        self.departament = departament


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

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

    def insert(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = self.head
            
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self):
        if self.head is not None:
            self.head = self.head.next

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
        current = self.head
        print(f"{current.value.__dict__}\n removido")
        self.head = current.next
    

list_users = [
    ["pedro",21,"TI"],
    ["Ana ",28,"Contabilidade"],
    ["Luiz",40,"Financeiro"],
    ["Claudia",26,"Rh"],
    ]

stack_list = Stack()

for data in list_users:
    user =  User(data[0],data[1],data[2])
    stack_list.push(user)

stack_list.pop()
# queue_list.show()
