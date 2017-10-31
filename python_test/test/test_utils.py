# -*- coding: utf-8 -*-

from unittest import TestCase
from python_test.python_test.utils.util import MyUtil


class TestMyUtil(TestCase):

    def test_get_years_list(self):
        result = MyUtil.get_years_list(1995, 1997)
        test_result = [1995, 1996, 1997]
        self.assertEqual(result, test_result)

    def test_get_years_list2(self):
        result = MyUtil.get_years_list(1995, 1997)
        test_result = [1995, 1996, 19971]
        self.assertEqual(result, test_result)