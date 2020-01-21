import os
import sys


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class SingleLinkedList:
	def __init__(self):
		self.head = None


	def add_at_beginning(self, node):
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head = node


	def add_at_end(self, node):
		temp = self.head
		while temp.next is not None:
			print(temp.next.data)
			temp = temp.next
		temp.next = node


	def search(self, data):
		temp = self.head
		if temp.data == data:
			return f"{data} is present"
		else:
			while temp.next is not None:
				if temp.next.data == data:
					return f"{data} is present"
				else:
					temp = temp.next
			return f"{data} is NOT present"


	def reverse(self):
		previous = None
		next = None
		current = self.head
		while current is not None: 
			next = current.next
			current.next = previous 
			previous = current 
			current = next
		self.head = previous


	def is_empty(self):
		return 0 if self.head == None else 1


	def print_list(self):
		temp = self.head
		print(temp.data)
		while temp.next is not None:
			print(temp.next.data)
			temp = temp.next


	def is_looped(self):
		pass

	
def find_intersection(l1, l2):
	pass


def main():
	v1 =  10
	v2 = 20
	v3 = 30

	n1 = Node(v1)
	n2 = Node(v2)
	n3 = Node(v3)
	l1 = SingleLinkedList()
	print(f'-- inserting {v1} at beginning --')
	l1.add_at_beginning(n1)
	print(f'-- inserting {v2} at end --')
	l1.add_at_end(n2)
	print(f'-- inserting {v3} at beginning --')
	l1.add_at_beginning(n3)
	print('-- printing list --')
	l1.print_list()
	print('-- searching 10 --')
	print(l1.search(10))
	print('-- searching 100 --')
	print(l1.search(100))
	print('-- reversing list --')
	l1.reverse()
	l1.print_list()

if __name__ == '__main__':
	main()
