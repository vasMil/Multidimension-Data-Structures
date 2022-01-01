import unittest
from avlTree.AVLTree import AVLTree

class TestNode(unittest.TestCase):

    def setUp(self):
        self.node_values = [31, 18, 47, 7, 25, 34, 62, 28, 59, 88, 95, 33]
        self.avl = AVLTree()

        self.avl_ready = AVLTree()
        for value in self.node_values:
            self.avl_ready.insert(value)

    def test_insert(self):
        for value in self.node_values:
            self.avl.insert(value)
        self.assertEqual(self.avl.root.data, 31)
        self.assertEqual(self.avl.root.leftChild.data, 18)
        self.assertEqual(self.avl.root.leftChild.leftChild.data, 7)
        self.assertEqual(self.avl.root.leftChild.rightChild.data, 25)
        self.assertEqual(self.avl.root.leftChild.rightChild.rightChild.data, 28)
        self.assertEqual(self.avl.root.rightChild.data, 62)
        self.assertEqual(self.avl.root.rightChild.leftChild.data, 47)
        self.assertEqual(self.avl.root.rightChild.leftChild.leftChild.data, 34)
        self.assertEqual(self.avl.root.rightChild.leftChild.leftChild.leftChild.data, 33)
        self.assertEqual(self.avl.root.rightChild.leftChild.rightChild.data, 59)
        self.assertEqual(self.avl.root.rightChild.rightChild.data, 88)
        self.assertEqual(self.avl.root.rightChild.rightChild.rightChild.data, 95)

    def test_delete(self):
        self.avl_ready.delete(18)
        self.assertEqual(self.avl_ready.root.data, 47)
        self.assertEqual(self.avl_ready.root.leftChild.data, 31)
        self.assertEqual(self.avl_ready.root.leftChild.leftChild.data, 25)
        self.assertEqual(self.avl_ready.root.leftChild.leftChild.leftChild.data, 7)
        self.assertEqual(self.avl_ready.root.leftChild.leftChild.rightChild.data, 28)
        self.assertEqual(self.avl_ready.root.leftChild.rightChild.data, 34)
        self.assertEqual(self.avl_ready.root.leftChild.rightChild.leftChild.data, 33)
        self.assertEqual(self.avl_ready.root.rightChild.data, 62)
        self.assertEqual(self.avl_ready.root.rightChild.leftChild.data, 59)
        self.assertEqual(self.avl_ready.root.rightChild.rightChild.data, 88)
        self.assertEqual(self.avl_ready.root.rightChild.rightChild.rightChild.data, 95)

    def test_inOrder(self):
        self.node_values.sort()
        self.assertListEqual(self.avl_ready.inOrder(), self.node_values)


if __name__ == '__main__':
    unittest.main()