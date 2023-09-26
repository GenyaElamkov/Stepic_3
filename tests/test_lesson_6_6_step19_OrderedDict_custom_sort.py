from collections import OrderedDict

import pytest

from Module_6.lesson_6_6_step19_OrderedDict_custom_sort import custom_sort


@pytest.mark.parametrize("ordered_dict, by_values, result",
                         [(OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16),
                           False,
                           OrderedDict([('Anabel', 17), ('Brian', 40),
                                        ('Carol', 16), ('Dustin', 29)])),
                          (OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2),
                           True,
                           OrderedDict([('Earth', 3), ('Mars', 4), ('Mercury', 1),('Venus', 2)]))
                          ])

def test_custom_sort(ordered_dict, by_values, result):
    assert custom_sort(ordered_dict, by_values=False) == result
