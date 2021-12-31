import pytest
from nodes.node import Node
from typing import get_type_hints, Dict, Any
from . import conftest


def test_node_class_id_attr_has_type_hint(node_type_hints: Dict[str, Any]):
    assert "id" in node_type_hints
    assert int == node_type_hints.get("id")


def test_node_class_parent_attr_has_type_hint(node_type_hints: Dict[str, Any]):
    assert "parent" in node_type_hints
    assert int == node_type_hints.get("parent")


def test_node_class_init_has_type_hints():
    hints = get_type_hints(Node.__init__)
    assert "id" in hints
    assert int == hints.get("id")
    assert "parent" in hints
    assert int == hints.get("parent")


def test_node_class_init_raises_given_non_integer():
    with pytest.raises(ValueError):
        Node("abc", "Cde")


def test_node_class_init_does_not_accept_no_args():
    with pytest.raises(TypeError):
        Node()


def test_node_class_init_does_not_accept_one_arg_only():
    with pytest.raises(TypeError):
        Node(1)


def test_node_class_init_does_not_accept_more_than_two_args():
    with pytest.raises(TypeError):
        Node(1, 2, 3)


def test_node_init_holds_id_parent_attrs():
    node = Node(2, 1)
    assert getattr(node, "id", 0) == 2
    assert getattr(node, "parent", 0) == 1


def test_node_repr_returns_init_signature():
    node = conftest.generate_random_node()
    assert repr(node) == f"Node({node.id}, {node.parent})"


def test_node_does_not_accept_id_as_parent_of_itself():
    with pytest.raises(ValueError):
        Node(1, 1)


def test_node_does_not_accept_parent_greater_than_children():
    with pytest.raises(ValueError):
        Node(0, 1)
