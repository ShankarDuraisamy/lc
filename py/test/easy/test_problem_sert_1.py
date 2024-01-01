import pytest
from src.easy.problem_set_1 import ProblemSet1


def test_assign_cookies_455_base_case_01():
	g = [1, 2, 3]
	s = [1, 1]
	assert 1 == ProblemSet1.assign_cookies_455(g, s)


def test_assign_cookies_455_base_case_01():
	g = [1, 2]
	s = [1, 2, 3]
	assert 2 == ProblemSet1.assign_cookies_455(g, s)
