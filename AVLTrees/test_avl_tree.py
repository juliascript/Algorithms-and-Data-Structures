
# from solution_avl_tree import AVLTree, Node
from starter_avl_tree import AVLTree, Node
import unittest 

class NodeTest(unittest.TestCase):

	def test_init(self):
		data = 'a'
		n = Node(data)
		assert n.data == 'a'
		assert n.left_child is None
		assert n.right_child is None

class AVLTreeTest(unittest.TestCase):

	def test_init(self):
		avl_tree = AVLTree()
		assert avl_tree.root is None 
	
	def test_init_with_iterable(self):
		data = [1, 2]
		avl_tree = AVLTree(data)
		assert avl_tree.root.data == 1
		assert avl_tree.root.right_child.data == 2

	def test_node_balance_factor(self):
		data = [1, 2]
		avl_tree = AVLTree(data)
		assert avl_tree.root.balance_factor() == -1
		data = [2, 1]
		avl_tree = AVLTree(data)
		assert avl_tree.root.balance_factor() == 1

	def test_node_update_height(self):
		data = [1, 2]
		avl_tree = AVLTree(data)
		assert avl_tree.root.data == 1
		assert avl_tree.root.height == 1
		assert avl_tree.root.left_child == None
		assert avl_tree.root.right_child.height == 0
		avl_tree.insert(3)
		assert avl_tree.root.data == 2
		assert avl_tree.root.height == 1
		assert avl_tree.root.left_child.data == 1
		assert avl_tree.root.left_child.height == 0
		assert avl_tree.root.right_child.data == 3
		assert avl_tree.root.right_child.height == 0

	def test_tree_level_order_traversal(self):
		data = [20, 10, 40, 30, 50]
		avl_tree = AVLTree(data)
		assert avl_tree.items_level_order() == [20, 10, 40, 30, 50]

	def test_single_left_rotation_1(self):
		data = [1, 2, 3]
		avl_tree = AVLTree(data)
		assert avl_tree.root.data == 2
		assert avl_tree.root.left_child.data == 1
		assert avl_tree.root.right_child.data == 3
		assert avl_tree.items_level_order() == [2, 1, 3]

	def test_single_left_rotation_2(self):
		data = [20, 10, 40, 30, 50, 55]
		avl_tree = AVLTree(data)
		assert avl_tree.root.data == 40
		assert avl_tree.items_level_order() == [40, 20, 50, 10, 30, 55]

	def test_single_right_rotation_1(self):
		data = [3, 2, 1]
		avl_tree = AVLTree(data)
		assert avl_tree.root.data == 2
		assert avl_tree.root.left_child.data == 1
		assert avl_tree.root.right_child.data == 3
		assert avl_tree.items_level_order() == [2, 1, 3]

	def test_single_right_rotation_2(self):
		data = [40, 50, 30, 10, 5]
		avl_tree = AVLTree(data)
		assert avl_tree.root.data == 40
		assert avl_tree.items_level_order() == [40, 10, 50, 5, 30]

	# def test_left_right_rotation_1(self):
	# 	data = [8, 1, 4]
	# 	avl_tree = AVLTree(data)
	# 	assert avl_tree.root.data == 4
	# 	assert avl_tree.items_level_order() == [4, 1, 8]

	# def test_left_right_rotation_2(self):
	# 	data = [1, 4, 8, 12, 16, 20, 25, 30, 35, 28]
	# 	avl_tree = AVLTree(data)
	# 	assert avl_tree.root.data == 12
	# 	assert avl_tree.items_level_order() == [12, 4, 25, 1, 8, 20, 30, 16, 28, 35]

	# def test_right_left_rotation_1(self):
	# 	data = [1, 8, 4]
	# 	avl_tree = AVLTree(data)
	# 	assert avl_tree.root.data == 4
	# 	assert avl_tree.items_level_order() == [4, 1, 8]

	# def test_right_left_rotation_2(self):
	# 	data = [20, 10, 40, 30, 50, 35]
	# 	avl_tree = AVLTree(data)
	# 	assert avl_tree.root.data == 30
	# 	assert avl_tree.items_level_order() == [30, 20, 40, 10, 35, 50]
