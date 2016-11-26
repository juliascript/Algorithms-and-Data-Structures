#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        node = Node(item)
        if self.tail is not None:
            currentTailNode = self.tail
            currentTailNode.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # TODO: prepend given item
        node = Node(item)
        if self.head is not None:
            currentHeadNode = self.head
            node.next = currentHeadNode
            self.head = node
        else: 
            self.head = node
            self.tail = node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        current = self.head
        try:
            if current.data == item:
                if current.data == self.tail.data:
                    self.head = None
                    self.tail = None
                    return
                else: 
                    self.head = current.next
                return None

            while current.next is not None: 
                if current.next.data == item:
                    #remove item
                    if current.next == self.tail:
                        self.tail = current
                        current.next = None
                    else:
                        current.next = current.next.next

                    return 
                else: 
                    current = current.next
        except AttributeError:
            raise ValueError

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True
        current = self.head

        try: 
            while current.data is not None:
                if quality(current.data) is True: 
                    return current.data
                else:
                    current = current.next
        except AttributeError:
            return None



def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
