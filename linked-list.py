class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail =self.head
    
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

    def update(self,id):
        current =  self.heap

        while

    def remove(self):
        if self.head is not None:
            self.head = self.head.next


linkedi_list = LinkedList()
    
list_users = [
    ["pedro",21,"TI"],
    ["Ana ",28,"Contabilidade"],
    ["Luiz",40,"Financeiro"],
    ["Claudia",26,"Rh"],
    ]


for data in list_users:
    user =  User(data[0],data[1],data[2])
    linkedi_list.insert(user)

linkedi_list.show()

linkedi_list.remove()

print("-----------------\n")

linkedi_list.show()
