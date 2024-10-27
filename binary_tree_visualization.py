import uuid
import networkx as nx
import matplotlib.pyplot as plt
import threading

from heap_draw import close_window


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Store node color
        self.id = str(uuid.uuid4())  # Unique ID for each node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Recursively adds edges and positions to the graph for visualization."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2 ** layer
            pos[node.left.id] = (left_x, y - 1)
            left_x = add_edges(
                graph, node.left, pos,
                x=left_x, y=y - 1, layer=layer + 1,
            )
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2 ** layer
            pos[node.right.id] = (right_x, y - 1)
            right_x = add_edges(graph, node.right, pos,
                                x=right_x, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root: Node) -> None:
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)

    # Додаємо кольори для тексту
    for label in labels.keys():
        x, y = pos[label]
        plt.text(
            x, y, labels[label], ha='center', va='center',
            color='white', fontsize=12,
        )  # Світлий колір тексту

    plt.title("Binary Tree Visualization")
    threading.Thread(
        target=close_window,
        daemon=True,
    ).start()
    plt.show()


def dfs_visualize(node, visited=None):
    """Depth-First Search (DFS) visualization."""
    if visited is None:
        visited = []
    if node is not None:
        visited.append(node)
        node.color = generate_unique_color(len(visited))
        dfs_visualize(node.left, visited)
        dfs_visualize(node.right, visited)


def bfs_visualize(root):
    """Breadth-First Search (BFS) visualization."""
    queue = [root]
    visited = []

    while queue:
        node = queue.pop(0)
        visited.append(node)
        node.color = generate_unique_color(len(visited))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def generate_unique_color(index):
    """Generates a unique color based on the index."""
    return f'#{index * 10 % 256:02x}{
        (index * 20) % 256:02x}{(index * 30) % 256:02x}'


def visualize_traversal(root: Node) -> None:
    """Visualizes the tree with node colors reflecting the order of visits."""
    dfs_visualize(root)
    draw_tree(root)  # Visualize DFS

    bfs_visualize(root)
    draw_tree(root)  # Visualize BFS


# Test the code
if __name__ == "__main__":
    # Create a sample binary tree
    root = Node(0)
    root.left = Node(1)
    root.left.left = Node(2)
    root.left.right = Node(3)
    root.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    # Visualize traversals
    visualize_traversal(root)
