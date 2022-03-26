class Node:

    def __init__(self, id: int, parent: int):
        self.id = id
        self.parent = parent

    def __repr__(self):
        return f'node_{self.id - 1}'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError('The node id must be an integer.')
        self.__id = value

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        if not isinstance(value, int):
            raise ValueError('The node parent must be an integer.')
        elif value >= self.id:
            raise ValueError('The node parent must be less than node id.')
        self.__parent = value
