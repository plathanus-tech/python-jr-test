"""
This module defines the Node class which represents a node with an id and a parent id.
"""

class Node:
    """
    Represents a node with an id and a parent id.
    
    Attributes:
        id (int): The unique identifier of the node.
        parent (int): The identifier of the parent node.
    """
    id: int
    parent: int

    def __init__(self, id: int, parent: int):
        if not isinstance(id, int):
            raise ValueError("id must be an integer")
        if not isinstance(parent, int):
            raise ValueError("parent must be an integer")
        if parent >= id:
            raise ValueError("Parent cannot be greater than or equal to id.")
        if parent == id:
            raise ValueError("Parent cannot be the same as id.")
        self.id = id
        self.parent = parent

    def __repr__(self):
        return f"Node({self.id}, {self.parent})"
    