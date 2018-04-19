class Node:
    def __init__(self, v, children=None):
        self.value = v
        self.children = children or []
        self.count = 0

    def insert(self, ui, vi):
        if self.value == vi:
            self.children.append(Node(ui))
            self.count += 1
            return True
        elif not len(self.children):
            return False
        else:
            for c in self.children:
                inserted = c.insert(ui, vi)
                if inserted:
                    self.count += 1
                    return True
            return False

    def edges_to_remove(self):
        total = 0
        for child in self.children:
            if child.count % 2:
                total += 1
            total += child.edges_to_remove()
        return total

n, m = map(int, input().split(" "))
tree = None
for i in range(m):
    ui, vi = map(int, input().split(" "))
    if not tree:
        tree = Node(vi)
    tree.insert(ui, vi)

print(tree.edges_to_remove())
