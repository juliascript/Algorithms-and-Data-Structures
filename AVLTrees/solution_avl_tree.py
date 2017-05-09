
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
		return (self.left_child.height if self.left_child else -1) - (self.right_child.height if self.right_child else -1)

	def update_height(self):
		if not self.right_child and not self.left_child:
			self.height = 0
		elif not self.right_child:
			self.height = (self.left_child.height + 1)
		elif not self.left_child:
			self.height = (self.right_child.height + 1)
		else:
			self.height = (max(self.left_child.height, self.right_child.height) + 1)

	# # Recursive calculation of height -- can be removed
	# def calculate_height(self):
	# 	"""Return the number of edges on the longest downward path from this
	# 	node to a descendant leaf node"""
	# 	# TODO: Check if left child has a value and if so calculate its height
	# 	left_height = self.left_child.height if self.left_child is not None else -1
	# 	# TODO: Check if right child has a value and if so calculate its height
	# 	right_height = self.right_child.height if self.right_child is not None else -1
	# 	# Return one more than the greater of the left height and right height
	# 	return 1 + max(left_height, right_height)



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
		return self.root is None

	def find(self, data):
		current = self.root
		while current is not None:
			if current.data == data:
				return current
			elif current.data > data:
				current = current.left_child
				continue
			elif current.data < data:
				current = current.right_child
				continue
		raise ValueError('%s not found in tree.' % (data))

	def insert(self, data):
		# print('')
		# print('Inserting ({}) ...'.format(data))

		n = Node(data)
		if self.root is None:
			self.root = n
			return

		current = self.root
		while current is not None:
			if current.data == data:
				# do nothing? raise error?
				raise ValueError('%s already in tree.' % (data))
			elif current.data > data:
				if not current.left_child:
					current.left_child = n
					n.parent = current
					# update heights of parents and rotate if needed
					self.retrace_loop(n)
					return
				else:
					current = current.left_child
					continue
			elif current.data < data:
				if not current.right_child:
					current.right_child = n
					n.parent = current
					# update heights of parents and rotate if needed
					self.retrace_loop(n)
					return
				else:
					current = current.right_child
					continue

	def retrace_loop(self, node):
		# print('retrace_loop({})'.format(node))

		current = node.parent
		while current is not None:
			# print('current: {}'.format(current))

			current.update_height()

			balance_factor = current.balance_factor()
			# print('balance_factor: {}'.format(balance_factor))
			
			if balance_factor < -1:
				# right heavy
				if current.right_child:
					# check the right child of current to see if it's left heavy
					right_child_balance_factor = current.right_child.balance_factor()
					if right_child_balance_factor >= 1:
						# right left
						self.right_rotation(current.right_child)
					self.left_rotation(current)
					current = current.parent
					continue
				else:
					# left
					self.left_rotation(current)

			elif balance_factor > 1:
				# left heavy
				if current.left_child:
					# check the left child of current to see if it's right heavy
					left_child_balance_factor = current.left_child.balance_factor()
					if left_child_balance_factor <= -1:
						# left right
						self.left_rotation(current.left_child)
					self.right_rotation(current)
					current = current.parent
					continue
				else:
					# right
					self.right_rotation(current)
			else:
				# balanced
				current = current.parent

	def update(self, node, data):
		try:
			n = self.find(node)
			n.data = data
		except ValueError:
			raise ValueError('%s not found in tree.' % (node))

	def left_rotation(self, node):
		# print('left_rotation({})'.format(node))

		# o    // node
		#  \
		#   o  // node.right_child
		#    \
		# 	  o

		# nodes right child becomes parent, node becomes left child
		new_left_child = node
		new_right_child_of_left_child = node.right_child.left_child
		new_parent = node.right_child

		new_parents_parent = node.parent

		if new_parents_parent is None:
			# new_parent is becoming the tree's root
			self.root = new_parent
			new_parent.parent = None
		else:
			# check to see if this is the left or right child of the parent node
			if node.data > new_parents_parent.data:
				new_parents_parent.right_child = new_parent
			else:
				new_parents_parent.left_child = new_parent
			new_parent.parent = new_parents_parent

		new_parent.left_child = new_left_child
		new_left_child.parent = new_parent
		new_left_child.right_child = new_right_child_of_left_child
		if new_right_child_of_left_child:
			new_right_child_of_left_child.parent = new_left_child
		new_left_child.update_height()
		new_parent.update_height()

	def right_rotation(self, node):
		# print('right_rotation({})'.format(node))

		# 	  o // node
		#    /
		#   o   // node.left_child
		#  /
		# o

		# nodes left child becomes parent, node becomes right child
		new_right_child = node
		new_left_child_of_right_child = node.left_child.right_child
		new_parent = node.left_child

		new_parents_parent = node.parent
		if new_parents_parent is None:
			# new_parent is becoming the tree's root
			self.root = new_parent
			new_parent.parent = None
		else:
			# check to see if this is the left or right child of the parent node
			if node.data > new_parents_parent.data:
				new_parents_parent.right_child = new_parent
			else:
				new_parents_parent.left_child = new_parent
			new_parent.parent = new_parents_parent

		new_parent.right_child = new_right_child
		new_right_child.parent = new_parent
		new_right_child.left_child = new_left_child_of_right_child
		if new_left_child_of_right_child:
			new_left_child_of_right_child.parent = new_right_child
		new_right_child.update_height()
		new_parent.update_height()

	def items_level_order(self):
		"""Return a list of all items in this binary search tree found using
		level-order traversal"""
		# Create a queue to store nodes not yet traversed in level-order
		queue = list()
		# Create an items list
		items = list()
		# Enqueue the root node if this tree is not empty
		if not self.is_empty():
			queue.append(self.root)
		# Loop until the queue is empty
		while len(queue) > 0:
			# Avoid infinite loop if tree has duplicate child pointers
			# if len(items) > 10:
			# 	print(items)
			# 	return
			# Dequeue the node at the front of the queue
			node = queue.pop(0)
			# Add this node's data to the items list
			items.append(node.data)
			# Enqueue this node's left child if it exists
			if node.left_child is not None:
				queue.append(node.left_child)
			# Enqueue this node's right child if it exists
			if node.right_child is not None:
				queue.append(node.right_child)
		# Return the items list
		return items



if __name__ == "__main__":

	# # Start with an empty AVL tree
	# avl_tree = AVLTree()
	# max_num = 3
	# for item in range(1, max_num + 1):
	# 	print('Inserting {} into tree...'.format(item))
	# 	avl_tree.insert(item)
	# 	print('items in level-order: {}'.format(avl_tree.items_level_order()))
	# 	print('\n')


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
	data = [20, 10, 40, 30, 50, 55]
	print('Inserting: {}'.format(data))
	avl_tree = AVLTree(data)
	print('items in level-order: {}'.format(avl_tree.items_level_order()))

