from typing import List
import copy
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from nodes.node import Node

class NodeManager:
    nodes: List[Node]   # Adding the type hint for the 'nodes' attribute
    
    # Initializes the NodeManager with a list of Node objects.
    # Ensures that the input is a list of Node instances.
    def __init__(self, nodes: List[Node]):
        if not isinstance(nodes, list):
            raise ValueError("The nodes must be a list of Node objects.")

        if not all(isinstance(node, Node) for node in nodes):
            raise ValueError("The nodes must be a list of Node objects.")
		
        #This object must not mutate the received List
        self.nodes: List[Node] = copy.deepcopy(nodes)
		
    # Returns the number of nodes in the NodeManager.
    def __len__(self) -> int:
        return len(self.nodes)
    
	# Retrieves a Node object by index from the nodes list.	
    def __getitem__(self, index: int) -> Node:
        return self.nodes[index]
    
	
    # Removes a Node from the manager.
    # Raises a ValueError if the node is not in the list of nodes.
    def remove(self, node: Node) -> None:
        if node not in self.nodes:
            raise ValueError("The node does not exist in the nodes member.")
            
        self.nodes.remove(node)	
        
			
    # Removes a Node and all its children (cascade removal).
    # If the node has children, they are recursively removed as well.
    def remove_cascade(self, node: Node) -> None:
        #Check if the node exists in the list
        if node not in self.nodes:
            raise ValueError("The node does not exist in the nodes member.")
			
		# First remove the node itself
        self.remove(node)
        
        # Cascade removal of nodes where the parent is the removed node
        to_remove = [n for n in self.nodes if n.parent == node.id]
        for child in to_remove:
            self.remove_cascade(child)