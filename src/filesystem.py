class Node:
    def __init__(self, name, size=0, children=None):
        self.name = name
        self.size = size
        self.children = children or []


def total_size(node):
    """Return the total size of a folder (postorder sum)."""
    if node is None:
        return 0
    if not node.children:
        return node.size
    total = node.size
    for child in node.children:
        total += total_size(child)
    return total


def folder_sizes(root):
    """Return a dictionary mapping each folder name to its total size."""
    if root is None:
        return {}
    sizes = {}

    def dfs(node):
        total = node.size
        for child in node.children:
            total += dfs(child)
        if node.children:  # Only include folders (nodes with children)
            sizes[node.name] = total
        return total

    dfs(root)
    return sizes


def level_order(root):
    """Return level-order traversal (BFS) as list of lists of names."""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_names = []
        next_level = []
        for node in queue:
            level_names.append(node.name)
            next_level.extend(node.children)
        result.append(level_names)
        queue = next_level

    return result


# Example test
if __name__ == "__main__":
    # Example tree
    root = Node("root", 10, [
        Node("bin", 20, [
            Node("bash", 5),
            Node("ls", 3)
        ]),
        Node("usr", 15, [
            Node("local", 7),
            Node("share", 8)
        ])
    ])

    print("Total size of root:", total_size(root))
    print("Folder sizes:", folder_sizes(root))
    print("Level order:", level_order(root))
