# Plathanus - Python Test for Jr Role

Welcome!
First of all, [fork](https://docs.github.com/pt/get-started/quickstart/fork-a-repo) This Repository to your Github Account.

After that [git clone](https://git-scm.com/docs/git-clone) it to your machine.

Create a [git branch](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) using the name pattern `test/<your-github-username>`
Do the developing on this branch.

## Installation

Requires python >= 3.8

**Create an virtual environment:**

This tutorial snippets assumes you uses Linux. For installation on other OS check [python documentation on venv](https://docs.python.org/3/library/venv.html).

> python3 -m venv venv

**Activate it:**

> source venv/bin/activate

**Install pytest:**

> pip install pytest

That's it you are done! To run the tests run:

> pytest

## The goal of the test

One of our clients had an series of documents that may depend on others. He wants us to everytime he deletes an document all children documents are deleted as well. You've been designated to do this task. For this example, we're going to call the document as an `Node`.
We're going to implement an `Node` class that will have an `id` and `parent`, and an `NodeManager` that will have an List of instance of the `Node`s. This Manager will have the `remove` method that removes an single `Node` from the `nodes` member, and `remove_cascade` method that will removes all `Node`s that has it as an parent, and all the `Node`s that have been removed, must remove all `Node`s that has it as an parent, and so on.

## Hands ON

The requirements for the test are below. As you code, make sure that you run `pytest` to see your current progress. When all tests are passing, go ahead to the finishing part.

### The Node class

Inside _nodes/node.py_ you must write the `Node` class.
Here are the requirements for an `Node`:

1. The `Node` class must declare the `id` and `parent` members. They Must be [type hinted](https://docs.python.org/3/library/typing.html) as `int`egers.
2. An node `parent` cannot be greater than it's `id`. If this condition is not satisfied you should raise an `ValueError` exception;
3. An node `parent` cannot be the same as it's own `id`. If this condition is not satisfied you should raise an `ValueError` exception;
4. An `Node` should be instanced giving 2 integers like: `Node(2, 1)`; If this condition is not satisfied you should raise an `ValueError` exception;
5. For debugging purposes we'll like that the `Node` representation is equals to the way we instance it. Done in the [`__repr__ method`](https://docs.python.org/3/reference/datamodel.html?highlight=__repr__#object.__repr__);

### The NodeManager class

Inside _nodes/manager.py_ you must write the `NodeManager` class.
Here are the requirements for the `NodeManager`:

1. Each `NodeManager` must declare the `nodes` member. Must be type hinted as an `List` of `Node`.
2. It must receive an `List` of `Node` to be instanced, the `nodes` member should receive this `List`. If this condition is not satisfied you should raise an `ValueError` exception;
3. This object must not mutate the received `List`;
4. We should be able to see the number of nodes in the `nodes` member through the `NodeManager` instance. Done in the [`__len__ method`](https://docs.python.org/3/reference/datamodel.html?highlight=__len__#object.__len__).
5. We should be able to get an `Node` object from the `nodes` member through the `NodeManager` instance like an list. Done in the [`__getitem__ method`](https://docs.python.org/3/reference/datamodel.html?highlight=__len__#object.__getitem__)
6. It must implement two methods `remove` and `remove_cascade`. They both receives an `Node` object to be removed from the `nodes` member and should return `None`.
7. The `remove` and `remove_cascade` method should raise an `ValueError` if the received `Node` does not exist on the `nodes` member.
8. The `remove` method must not remove its childrens.
9. The `remove_cascade` method should remove all `Node` from the `nodes` member that have the parent equal to the received `Node`, this action must be performed again on the granchildren of the removed `Node`. Example:

Given the `List`[`Node`] below:

    [
        Node(1, 0),
        Node(2, 1),
        Node(3, 2),
        Node(4, 2),
        Node(5, 2),
        Node(6, 5),
        Node(7, 6),
        Node(8, 7),
    ]

If you call `remove_cascade` on the manager instance for the `Node(2, 1)` the `nodes` member must look like below:

    [
        Node(1, 0),
    ]

This is expected because when we excluded the `Node` with `id` 2, the `Node`s that has `id`s 3, 4, 5 as `parent` must be excluded, and the same is for the `Node` with `id` 6, that has the `Node` with 5 as `parent` and so on..

## Finishing

After you finish, push your local branch to your github repository and [create a pull request](https://docs.github.com/articles/creating-a-pull-request-from-a-fork) to our `master` branch.
