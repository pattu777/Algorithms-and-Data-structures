#!/usr/bin/env python

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def iterative_insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            nd = self.root
            while nd is not None:
                if item < nd.data:
                    if nd.left is None:
                        nd.left = Node(item)
                        return
                    else:
                        nd = nd.left
                else:
                    if nd.right is None:
                        nd.right = Node(item)
                        return
                    else:
                        nd = nd.right


    def remove(self, node, item):
        if node is None:
            return
        if item < node.data:
            self.remove(node.left, item)
        elif item > node.data:
            self.remove(node.right, item)
        else:
            if node.left is None:
                tmp = node.right
                node = None

            elif node.right is None:
                tmp = node.left
                node = None

            else:
                tmp = self.get_min(node.right)
                node.data = tmp.data
                node.right = self.remove(node.right, tmp.data)

    def iterative_search(self, item):
        if self.root is None:
            return False
        else:
            nd = self.root
            while nd is not None:
                if nd.data == item:
                    return True
                elif nd.data < item:
                    nd = nd.right
                else:
                    nd = nd.left
            return False

    def recursive_search(self, node, item):
        if node is None:
            return False
        else:
            if node.data == item:
                return True
            elif node.data < item:
                return self.recursive_search(node.right, item)
            else:
                return self.recursive_search(node.left, item)

    def size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.size(node.left) + self.size(node.right)

    def depth(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.depth(node.left), self.depth(node.right))

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print node.data
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print node.data
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.data

    def get_min(self, node):
        if node.left is None:
            return node.data
        else:
            return self.get_min(node.left)

    def get_max(self, node):
        if self.root is None:
            return "Tree is empty."
        else:
            if node.right is None:
                return node.data
            else:
                return self.get_max(node.right)


