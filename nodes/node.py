def is_valid_node_params(id, parent) -> bool:
    is_params_int = isinstance(id, int) or isinstance(parent, int)
    is_id_greater = id > parent

    if is_params_int and is_id_greater:
        return True
    else:
        raise ValueError


class Node:
    id: int
    parent: int

    def __init__(self, id: int, parent: int):
        if is_valid_node_params(id, parent):
            self.id = id
            self.parent = parent

    def __repr__(self):
        return f"Node({self.id}, {self.parent})"
