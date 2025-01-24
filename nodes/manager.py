"""
This module defines the NodeManager class which manages a collection of Node objects.
"""

from typing import List
from .node import Node

class NodeManager:
    """
    Manages a collection of Node objects, allowing for removal of nodes and their children.
    
    Attributes:
        nodes (List[Node]): A list of Node objects managed by this instance.
    """
    nodes: List[Node]

    def __init__(self, nodes: List[Node]) -> None:
        """
        Initializes the NodeManager with a list of Node objects.
        
        Args:
            nodes (List[Node]): A list of Node objects to be managed.
        
        Raises:
            ValueError: If nodes is not a list.
        """
        if not isinstance(nodes, list):
            raise ValueError("nodes must be a list")
        self.nodes = nodes.copy()

    def __len__(self) -> int:
        """
        Returns the number of nodes managed by this instance.
        
        Returns:
            int: The number of nodes.
        """
        return len(self.nodes)

    def __getitem__(self, index: int) -> Node:
        """
        Returns the Node at the specified index.
        
        Args:
            index (int): The index of the Node to retrieve.
        
        Returns:
            Node: The Node at the specified index.
        """
        return self.nodes[index]

    def remove(self, node: Node) -> None:
        """
        Removes the specified Node from the manager.
        
        Args:
            node (Node): The Node to be removed.
        
        Raises:
            ValueError: If the Node is not found in the manager.
        """
        if node not in self.nodes:
            raise ValueError("Node not found in the manager")
        self.nodes.remove(node)

    def remove_cascade(self, node: Node) -> None:
        """
        Removes the specified Node and all its children from the manager.
        
        Args:
            node (Node): The Node to be removed along with its children.
        
        Raises:
            ValueError: If the Node is not found in the manager.
        """
        if node not in self.nodes:
            raise ValueError("Node not found in the manager")

        to_remove = [node]
        while to_remove:
            current = to_remove.pop()
            children = [n for n in self.nodes if n.parent == current.id]
            to_remove.extend(children)
            self.nodes.remove(current)

        for n in self.nodes[:]:
            if n.parent == node.id:
                self.nodes.remove(n)
                