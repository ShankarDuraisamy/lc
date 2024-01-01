from src.common.list_node import ListNode


class LinkedListUtil:
	@staticmethod
	def compare(list1: ListNode, list2: ListNode) -> bool:
		node1 = list1
		node2 = list2
		while node1 and node2:
			if node1.val != node2.val:
				return False

	@staticmethod
	def length(lst: ListNode) -> int:
		count = 0
		node = lst
		while node:
			count += 1
			node = node.next
		return count

	@staticmethod
	def check_unique(lst: ListNode) -> bool:
		count = 0
		node = lst
		while node and node.next:
			if node.val == node.next.val:
				return False
			node = node.next
		return True
