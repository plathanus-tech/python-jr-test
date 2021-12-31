# Create here the NodeManager Class
from typing import List
from nodes.node import Node

class NodeManager:
    
    nodes: List[Node]

    def __init__(self, nodes: List[Node]):
        self.nodes = nodes        
        
    def remove(self, nodes):
        self.nodes = nodes
        
    def remove_cascade(self, children):
        self.children = children
    
    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, nodes):
        return self.nodes[nodes]
   


    
    