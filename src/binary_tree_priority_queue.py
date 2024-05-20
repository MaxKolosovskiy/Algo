class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None


class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if not self.root:
            self.root = new_node
            return

        current = self.root
        while True:
            if priority < current.priority:
                if not current.left:
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    break
                else:
                    current = current.right

    def peek(self):
        if not self.root:
            return None
        max_node = self._find_max(self.root)
        return max_node.value

    def pop(self):
        if not self.root:
            return None
        return self._remove_max(self.root)

    def _find_max(self, current):
        if not current:
            return None
        while current.right:
            current = current.right
        return current

    def _remove_max(self, current, parent=None):
        if not current:
            return None
        if not current.right:
            if parent:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            return current.value

        max_node = self._find_max(current.left)
        max_value = max_node.value
        self._remove_max(max_node, current)

        if parent:
            if parent.left == current:
                parent.left = max_node
            else:
                parent.right = max_node
        else:
            self.root = max_node

        max_node.left = current.left
        max_node.right = current.right

        return max_value

    def __repr__(self):
        result = []
        stack = []
        current = self.root

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                result.append(current.value)
                current = current.right
            else:
                break

        return "**<" + ", ".join(map(str, result)) + ">**"