from typing import List
from typing import Optional

from src.common.list_node import ListNode


class ProblemSet1:

    @staticmethod
    def assign_cookies_455(g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        pointer_1 = 0
        pointer_2 = 0
        while pointer_1 < len(g) and pointer_2 < len(s):
            if g[pointer_1] <= s[pointer_2]:
                pointer_1 += 1
            pointer_2 += 1
        return pointer_1

    @staticmethod
    def merge_sorted_array_88(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        num1_pointer = m - 1
        num2_pointer = n - 1
        last_pointer = m + n - 1
        while num1_pointer >= 0 and num2_pointer >= 0:
            if nums1[num1_pointer] >= nums2[num2_pointer]:
                nums1[last_pointer] = nums1[num1_pointer]
                num1_pointer -= 1
            else:
                nums1[last_pointer] = nums2[num2_pointer]
                num2_pointer -= 1
            last_pointer -= 1
        while num2_pointer >= 0:
            nums1[last_pointer] = nums2[num2_pointer]
            last_pointer -= 1
            num2_pointer -= 1

    @staticmethod
    def delete_duplicate(head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
                continue
            node = node.next
        return head






