# Create here the Node Class


class Node:
    id: int
    parent: int

    def __init__(self, id: int, parent: int):

        if not isinstance(id, int):
            raise ValueError("The node's id must to be an interger")
        else:
            self.id = id

        if not isinstance(parent, int):
            raise ValueError("The node's parent must to be an interger")
        elif parent >= id:
            raise ValueError("An Node parent can't be greater or equal to the node's id")
        else:
            self.parent = parent

    def __repr__(self) -> str:
        return f'Node({self.id}, {self.parent})'

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.id == other.id and self.parent == other.parent
