#this passed the tests!!

from __future__ import annotations
from beginnercodes.challenges import test


def make_text_list(k):

    a = str(k)          #converts number entered as parameter to text

    i = 0
    l = []

    for i in a:             #splits digits in input number into text digit list
        l.append(i)

    return l

def make_num_list(m):

    a = str(m)          #converts number entered as parameter to text

    i = 0
    l = []
    l_num = []

    for i in a:             #splits digits in input number into text digit list
        l.append(i)

    for i in l:             #converts digits in list into numbers
        digit_as_num = l_num.append(int(i))

    return l_num

def r_d(n):

    s = sum(make_num_list(n))
    length = len(make_num_list(n))

    while length > 1:
        return r_d(s)

    return s

test(587, r_d)