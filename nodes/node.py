# Create here the Node Class
class Node:
    id: int
    parent: int

    def __init__(self, id: int, parent:int):
        if not isinstance(id, int):
            raise ValueError("id must be set to an integer")
        elif not isinstance(parent, int):
            raise ValueError("parent must be set to an integer")
        self.id = id 
        self.parent = parent
    
        if parent >= id:
          raise ValueError('parent bigger or equal than id')
    def __repr__(self):
      return "Node(%s, %s)" % (self.id, self.parent)
        

