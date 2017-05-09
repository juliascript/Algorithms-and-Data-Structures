
class Node(object):
	"""Nodes in binary search tree, specifically for AVL tree"""
	def __init__(self, data):
		self.data = data
		self.height = 0
		self.parent = None
		self.left_child = None
		self.right_child = None

	def __repr__(self):
		"""Return a string representation of this node"""
		return 'Node({})'.format(repr(self.data))

	def balance_factor(self):
		pass

	def update_height(self):
		pass


class AVLTree(object):
	"""AVLTree, a self balancing binary search tree where the heights of each child node do not differ by more than 1"""
	def __init__(self, iterable=None):
		self.root = None
		if iterable:
			for item in iterable:
				self.insert(item)

	def __repr__(self):
		"""Return a string representation of this AVL tree"""
		return 'AVLTree({})'.format(self.items_level_order())

	def is_empty(self):
		"""Return True if this AVL tree contains no nodes"""
		pass

	def find(self, data):
		pass

	def insert(self, data):
		# print('')
		# print('Inserting ({}) ...'.format(data))
		pass

	def retrace_loop(self, node):
		# print('retrace_loop({})'.format(node))
		pass

	def update(self, node, data):
		pass

	def left_rotation(self, node):
		# print('left_rotation({})'.format(node))

		# o    // node
		#  \
		#   o  // node.right_child
		#    \
		# 	  o

		pass

	def right_rotation(self, node):
		# print('right_rotation({})'.format(node))

		# 	  o // node
		#    /
		#   o   // node.left_child
		#  /
		# o

		pass

	def items_level_order(self):
		"""Return a list of all items in this binary search tree found using
		level-order traversal"""
		pass



if __name__ == "__main__":

	# # Start with an empty AVL tree
	avl_tree = AVLTree()
	max_num = 3
	for item in range(1, max_num + 1):
		print('Inserting {} into tree...'.format(item))
		avl_tree.insert(item)
		print('items in level-order: {}'.format(avl_tree.items_level_order()))
		print('\n')


	# # Start with a balanced AVL tree with 3 nodes
	# avl_tree = AVLTree([2,1,3])
	# print('items in level-order: {}'.format(avl_tree.items_level_order()))
	# print('Inserting {} into tree...'.format(4))
	# avl_tree.insert(4)
	# print('items in level-order: {}'.format(avl_tree.items_level_order()))
	# print('')
	# print('Inserting {} into tree...'.format(5))
	# avl_tree.insert(5)  # Should trigger rebalance
	# print('items in level-order: {}'.format(avl_tree.items_level_order()))
	# print('')

	# # Start with an empty AVL tree for left-right right_rotation
	# data = [1, 4, 8, 12, 16, 20, 25, 30, 35, 28]
	# data = [20, 10, 40, 30, 50, 55]
	# print('Inserting: {}'.format(data))
	# avl_tree = AVLTree(data)
	# print('items in level-order: {}'.format(avl_tree.items_level_order()))

