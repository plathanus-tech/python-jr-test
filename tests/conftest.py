import pytest, random
from nodes.node import Node
from nodes.manager import NodeManager
from typing import get_type_hints, Dict, Any, Tuple, List


@pytest.fixture
def node_type_hints() -> Dict[str, Any]:
    return get_type_hints(Node)


def random_integers() -> Tuple[int, int]:
    return random.randint(25000, 50000), random.randint(0, 25000)


@pytest.fixture
def generate_random_node() -> Node:
    id, parent = random_integers()
    return Node(id, parent)


@pytest.fixture
def random_nodes(generate_random_node) -> List[Node]:
    return [generate_random_node for _ in range(100)]


@pytest.fixture
def one_node_manager() -> NodeManager:
    node = Node(-1, -2)
    return NodeManager([node])
