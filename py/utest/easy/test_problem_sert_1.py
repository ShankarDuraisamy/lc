import pytest
from src.easy.problem_set_1 import ProblemSet1
from src.common.list_node import ListNode
from utest.common.linked_list_util import LinkedListUtil


def test_assign_cookies_455_base_case_01():
	g = [1, 2, 3]
	s = [1, 1]
	assert 1 == ProblemSet1.assign_cookies_455(g, s)


def test_assign_cookies_455_base_case_01():
	g = [1, 2]
	s = [1, 2, 3]
	assert 2 == ProblemSet1.assign_cookies_455(g, s)


def test_merge_sorted_array_88_case_01():
	nums1 = [1, 2, 3, 0, 0, 0]
	m = 3
	nums2 = [2, 5, 6]
	n = 3
	ProblemSet1.merge_sorted_array_88(nums1, m, nums2, n)
	assert nums1 == [1, 2, 2, 3, 5, 6]
	assert len(nums1) == m + n


def test_merge_sorted_array_88_case_02():
	nums1 = [1, 2, 3, 0, 0, 0]
	m = 3
	nums2 = [4, 5, 6]
	n = 3
	ProblemSet1.merge_sorted_array_88(nums1, m, nums2, n)
	assert nums1 == [1, 2, 3, 4, 5, 6]
	assert len(nums1) == m + n


def test_merge_sorted_array_88_case_03():
	nums1 = [0]
	m = 0
	nums2 = [1]
	n = 1
	ProblemSet1.merge_sorted_array_88(nums1, m, nums2, n)
	assert nums1 == [1]
	assert len(nums1) == m + n


def test_remove_duplicate_83_case_01():
	node3 = ListNode(2)
	node2 = ListNode(1, node3)
	node1 = ListNode(1, node2)
	result = ProblemSet1.delete_duplicate(node1)
	assert True == LinkedListUtil.check_unique(result)
	assert 2 == LinkedListUtil.length(result)


def test_remove_duplicate_83_case_02():
	node5 = ListNode(3)
	node4 = ListNode(3, node5)
	node3 = ListNode(2, node4)
	node2 = ListNode(1, node3)
	node1 = ListNode(1, node2)
	result = ProblemSet1.delete_duplicate(node1)
	assert True == LinkedListUtil.check_unique(result)
	assert 3 == LinkedListUtil.length(result)

def test_remove_duplicate_83_case_03():
	result = ProblemSet1.delete_duplicate(None)
	assert True == LinkedListUtil.check_unique(result)
	assert 0 == LinkedListUtil.length(result)
