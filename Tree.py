class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class BinaryTree(Node):
    
    def __init__(self, root):
        self.value = root
        self.root = self.value
        self.node_rigth = None
        self.node_left = None
        
    def insert(self, value):  # <-- Recuado para alinhar com __init__
        new_value = BinaryTree(value)
        current = self
        cond = True
        
        while cond:
            if value < current.value:
                if current.node_left is None:
                    current.node_left = new_value
                    cond = False
                else: 
                    current = current.node_left 
            else:
                if current.node_rigth is None:
                    current.node_rigth = new_value
                    cond = False
                else: 
                    current = current.node_rigth
                    
    def pre_order(self):
        
        print(self.value)
        
        if self.node_left is not None:
            self.node_left.pre_order()
            
        
        if self.node_rigth is not None:
            self.node_rigth.pre_order()
            
    def in_order(self):
    
        if self.node_left is not None:
            self.node_left.in_order()
    
        print(self.value)
    
        if self.node_rigth is not None:
            self.node_rigth.in_order()

    def post_order(self):
        if self.node_left is not None:
            self.node_left.post_order()
            
        if self.node_rigth is not None:
            self.node_rigth.post_order()
        
        print(self.value)

    def root_node(self):
        return self.root
        
tree = BinaryTree(20)
tree.insert(10)
tree.insert(8)
tree.insert(7)
tree.insert(9)
tree.insert(30)


tree.post_order()
