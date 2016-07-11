class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        '''Return the root node.'''
        return self.root

    def iterative_insert(self, item):
        '''Insert an element into the bst.'''
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
        """Remove an element from bst."""
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
        '''Iteratively search an element.'''
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
        '''Recursively search an element.'''
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
        '''Fetch the number of items in the bst.'''
        if node is None:
            return 0
        else:
            return 1 + self.size(node.left) + self.size(node.right)

    def max_depth(self, node):
        '''Find the maximum depth.'''
        if node is None:
            return 0
        else:
            return 1 + max(self.max_depth(node.left), self.max_depth(node.right))

    def inorder(self, node):
        '''Inorder traversal'''
        if node:
            self.inorder(node.left)
            print node.data
            self.inorder(node.right)

    def preorder(self, node):
        '''Pre-order Traversal.'''
        if node:
            print node.data
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        '''Post-order Traversal.'''
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.data

    def get_min(self, node):
        '''Get the minimum value.'''
        if node.left is None:
            return node.data
        else:
            return self.get_min(node.left)

    def get_max(self, node):
        '''Get the maximum value.'''
        if self.root is None:
            return "Tree is empty."
        else:
            if node.right is None:
                return node.data
            else:
                return self.get_max(node.right)


    def level_width(self, node, k):
        """Return the number of nodes in level k."""
        if node is None:
            return 0
        elif k == 1:
            return 1
        elif k > 1:
            return self.level_width(node.left, k-1) + self.level_width(node.right, k-1)


    def max_width(self):
        """Return the maximum width of the tree."""
        if self.root is None:
            return 0
        else:
            nd = self.root
            width = 0
            height = self.max_depth(self.root)
            for x in xrange(1, height+11):
                lwidth = self.level_width(self.root, height-x)
                if lwidth > width:
                    width = lwidth

            return lwidth

    def nodes_at_distance(self, node, k):
        """Print all nodes at distance k from the root."""
        if node is None:
            return

        elif k == 0:
            print "%d " % node.data,

        else:
            self.nodes_at_distance(node.left, k-1)
            self.nodes_at_distance(node.right, k-1)


    def kth_smallest(self, node, k):
        """Kth smallest element of the bst."""
        if k == 0:
            print node.data
            return
        else:
            kth_smallest(node.left)
            kth_smallest(node.right)

    def count_leafs(self, node):
        """Count the number of leaf nodes."""
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return self.count_leafs(node.left) + self.count_leafs(node.right)


