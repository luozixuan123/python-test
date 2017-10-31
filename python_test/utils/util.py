# -*- coding: utf-8 -*-


class MyUtil():

    @staticmethod
    def get_years_list(start_year, end_year):
        return list(xrange(int(start_year), int(end_year) + 1))
