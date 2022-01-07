# Create here the NodeManager Class
from nodes.node import Node
from typing import List

class NodeManager:
    nodes: List[Node]
    def __init__(self, nodes:List[Node]):
          if not isinstance(nodes, list):
            raise ValueError("nodes must be set to a list")
          self.nodes = tuple(nodes)

    def __len__(self):
      return len(self.nodes)
         
    def __getitem__(self, node_number):
          return self.nodes[node_number]
    def remove(self, node):
      if not(node in self.nodes):
            raise ValueError("node is not in the list")
      for i in range (len(self.nodes)):
        if self.nodes[i] == node:
          lista = list(self.nodes)
          lista.remove(self.nodes[i])
          self.nodes = lista
          break

      return None
    
    def remove_cascade(self, node:Node):
        if not(node in self.nodes):
            raise ValueError("node is not in the list")        

        filtered_nodes = []
        for i in range (len(self.nodes)):
            if not(self.nodes[i].parent >= node.id):
                filtered_nodes.append(self.nodes[i])
        if node in filtered_nodes:
            filtered_nodes.remove(node)
        
        self.nodes = filtered_nodes
    

        return self.nodes


