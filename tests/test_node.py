import pytest
from nodes.node import Node
from typing import get_type_hints, Dict, Any


def test_node_class_id_attr_has_type_hint(node_type_hints: Dict[str, Any]):
    assert "id" in node_type_hints
    assert node_type_hints.get("id") is int


def test_node_class_parent_attr_has_type_hint(node_type_hints: Dict[str, Any]):
    assert "parent" in node_type_hints
    assert node_type_hints.get("parent") is int


def test_node_class_init_has_type_hints():
    hints = get_type_hints(Node.__init__)
    assert "id" in hints
    assert hints.get("id") is int
    assert "parent" in hints
    assert hints.get("parent") is int


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


def test_node_repr_can_be_instanced_and_is_equals_to_node(generate_random_node):
    node: Node = generate_random_node
    node_repr = repr(node)
    node_from_repr = eval(node_repr)
    assert node_from_repr.id == node.id
    assert node_from_repr.parent == node.parent


def test_node_does_not_accept_id_as_parent_of_itself():
    with pytest.raises(ValueError):
        Node(1, 1)


def test_node_does_not_accept_parent_greater_than_children():
    with pytest.raises(ValueError):
        Node(0, 1)
