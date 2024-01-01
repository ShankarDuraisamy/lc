from typing import List


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
