# Create here the Node Class


class Node:
    id     : int
    parent : int

    def __init__(self, id: int, parent: int) -> None:
        if not isinstance(id,int):
            raise ValueError("id must be an integer")
        if not isinstance(parent, int):
            raise ValueError("parent must be an integer")
        if parent >= id:
            raise ValueError("parent must be less than id")
        
        self.id     = id
        self.parent = parent

    def __repr__(self) -> str:
        return f"Node({self.id},{self.parent})"
    