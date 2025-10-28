class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, employee_name, side):
        parent_node = self._find(self.root, parent_name)
        if not parent_node or side not in ("left", "right"):
            return False
        new_node = DoctorNode(employee_name)
        if side == "left":
            parent_node.left = new_node
        else:
            parent_node.right = new_node
        return True

    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        left_search = self._find(node.left, name)
        if left_search:
            return left_search
        return self._find(node.right, name)

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]
