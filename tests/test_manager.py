import pytest
from typing import get_type_hints, List, Dict, Any
from nodes.manager import NodeManager
from nodes.node import Node


def assert_nodes_type_hint_on_hints(hints: Dict[str, Any]):
    assert "nodes" in hints
    assert hints.get("nodes") is List[Node]


def test_nodemanager_nodes_attr_has_type_hints():
    hints = get_type_hints(NodeManager)
    assert_nodes_type_hint_on_hints(hints)


def test_nodemanager_init_has_type_hints():
    hints = get_type_hints(NodeManager.__init__)
    assert_nodes_type_hint_on_hints(hints)


def test_nodemanager_init_requires_one_arg():
    with pytest.raises(TypeError):
        NodeManager()


def test_nodemanager_raises_given_non_sequence():
    with pytest.raises(ValueError):
        NodeManager(1)


def test_nodemanager_accepts_list(random_nodes):
    node_list = random_nodes
    NodeManager(node_list)


def test_nodemanager_is_subscriptable(one_node_manager: NodeManager):
    node = one_node_manager[0]
    assert isinstance(node, Node)


def test_nodemanager_has_len(one_node_manager: NodeManager):
    assert len(one_node_manager) == 1


def test_nodemanager_remove_removes_only_one_item(one_node_manager: NodeManager):
    node = one_node_manager[0]
    one_node_manager.remove(node)
    assert len(one_node_manager.nodes) == 0


def test_nodemanager_remove_does_not_mutate_received_list():
    nodes = [
        Node(1, 0),
    ]
    manager = NodeManager(nodes)
    manager.remove(nodes[0])
    assert len(nodes) == 1


def test_nodemanager_remove_returns_none(one_node_manager: NodeManager):
    node = one_node_manager[0]
    returned = one_node_manager.remove(node)
    assert returned is None


def test_nodemanager_remove_cascade_removes_all_childrens():
    node_to_remove = Node(1, 0)
    nodes = [
        node_to_remove,
        Node(2, 1),
        Node(3, 2),
        Node(4, 2),
        Node(5, 2),
        Node(6, 5),
        Node(7, 6),
        Node(8, 7),
    ]
    manager = NodeManager(nodes)
    manager.remove_cascade(node_to_remove)
    assert len(manager.nodes) == 0


def test_nodemanager_remove_cascade_removes_only_dependent_childrens():
    node_to_remove = Node(2, 1)
    node_to_keep = Node(1, 0)
    another_node_to_keep = Node(9, 0)
    nodes = [
        node_to_keep,
        node_to_remove,
        Node(3, 2),
        Node(4, 2),
        Node(5, 2),
        Node(6, 5),
        Node(7, 6),
        Node(8, 7),
        another_node_to_keep,
    ]
    manager = NodeManager(nodes)
    manager.remove_cascade(node_to_remove)
    assert len(manager.nodes) == 2
    assert node_to_keep in manager.nodes
    assert another_node_to_keep in manager.nodes
