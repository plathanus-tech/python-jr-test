# Create here the Node Class


class Node:

    id: int = 0
    parent: int = 0

    def __init__(self, id: int, parent: int) -> None:

        if parent >= id:
            raise ValueError('parent can not to be greater than its id')

        if not type(id) == int or not type(parent) == int:
            raise ValueError('id and parent must have integer values')

        self.id = id
        self.parent = parent

    def __repr__(self) -> str:
        return 'Node(' + str(self.id) + ', ' + str(self.parent) + ')'

