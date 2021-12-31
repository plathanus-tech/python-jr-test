# Create here the Node Class

class Node:
    id: int
    parent: int
    def __init__(self, id: int, parent: int):
        self.id = id
        self.parent = parent
        
        if (int(id) == False):
            raise ValueError
        
        if (id < parent):
            raise ValueError

        if (id == parent):
            raise ValueError
        
    def __repr__(self):
        if (Node != "( , )"):
            return f"Node({self.id}, {self.parent})"  
        