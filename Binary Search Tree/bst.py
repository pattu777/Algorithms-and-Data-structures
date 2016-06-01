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


    def remove(self, item):
        pass

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
                node = node.right
            else:
                node = node.left

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

    def inorder(self, nd):
        if nd is None:
            return
        else:
            self.inorder(nd.left)
            print nd.data
            self.inorder(nd.right)

    def preorder(self, nd):
        if nd is None:
            return
        else:
            print nd.data
            self.preorder(nd.left)
            self.preorder(nd.right)

    def postorder(self, nd):
        if nd is None:
            return
        else:
            self.postorder(nd.left)
            self.postorder(nd.right)
            print nd.data

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

