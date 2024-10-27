import threading
import time
import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

from typing import List


class Node:
    def __init__(self, key: int):
        """
        Initializes a new node in the binary heap.

        Args:
            key (int): The value of the node.
        """
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  # Unique identifier for each node


def add_edges(
        graph: nx.DiGraph, node: Node, pos: dict,
        x: float = 0, y: float = 0, layer: int = 1) -> nx.DiGraph:
    """
    Adds edges and positions to the graph for visualization.

    Args:
        graph (nx.DiGraph): The directed graph to which edges will be added.
        node (Node): The current node being processed.
        pos (dict): A dictionary to store positions of nodes.
        x (float): The x-coordinate for the current node.
        y (float): The y-coordinate for the current node.
        layer (int): The current layer of the tree.

    Returns:
        nx.DiGraph: The updated graph with edges added.
    """
    if node is not None:
        graph.add_node(node.id, label=node.val)  # Using id to identify node
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left = x - 1 / 2 ** layer
            pos[node.left.id] = (left, y - 1)
            add_edges(graph, node.left, pos, x=left, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right = x + 1 / 2 ** layer
            pos[node.right.id] = (right, y - 1)
            add_edges(
                graph, node.right, pos, x=right,
                y=y - 1, layer=layer + 1
            )
    return graph


def close_window():
    """Closes the matplotlib window."""
    time.sleep(5)
    plt.close()


def draw_heap(
        heap_root: Node, timeout: int = 5) -> None:
    """
    Visualizes the binary heap using a directed graph
and closes the window after a timeout.

    Args:
        heap_root (Node): The root node of the binary heap.
        timeout (int): Time in seconds before the window closes automatically.
    """
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color="skyblue")
    plt.title("Binary Heap Visualization")

    threading.Thread(
        target=close_window,
        daemon=True,
    ).start()

    plt.show(block=True)  # Show the plot without blocking
    # Set a timer to close the window after the specified timeout


def create_heap_from_list(values: List[int]) -> Node:
    """
    Creates a binary heap from a list of values using heapify.

    Args:
        values (List[int]): List of values to create the heap.

    Returns:
        Node: The root node of the created binary heap.
    """
    # Create a min-heap from the list
    heapq.heapify(values)

    def build_tree(index: int) -> Node:
        if index < len(values):
            node = Node(values[index])
            node.left = build_tree(2 * index + 1)  # Left child
            node.right = build_tree(2 * index + 2)  # Right child
            return node
        return None

    return build_tree(0)


def create_heap() -> Node:
    """
    Creates a simple binary heap.

    Returns:
        Node: The root node of the created binary heap.
    """
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    return root


if __name__ == "__main__":
    heap_root = create_heap()
    draw_heap(heap_root)
