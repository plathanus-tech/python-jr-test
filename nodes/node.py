# Create here the Node Class


class Node:
    id: int
    parent: int
    def __init__(self, id: int, parent: int):
        if not isinstance(id, int):
            raise ValueError("id must be a integer.")

        if not isinstance(parent, int):
            raise ValueError("parent must be a integer.")

        if parent >= id:
            raise ValueError("A Node parent cannot be greater or equal to it's id.")

        self.id = id
        self.parent = parent

        
    def __repr__(self):
        return f"Node({self.id}, {self.parent})"
