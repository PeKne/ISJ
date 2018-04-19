#!/usr/bin/env python3
import itertools

def combine4(numbers, result):
    """
    Find all mathematical expressions represented by numbers (first argument) which are equal to result (second argument)
    """

    string_forms = [None] * 11
    matched_expressions = []
    ops = ["+", "-", "*", "/"]

    for o1 in ops:
        for o2 in ops:
            for o3 in ops:
                for variant in itertools.permutations(numbers): # loop through all permutatins
                    string_forms[0] = "%d%s(%d%s(%d%s%d))" % ( variant[0], o1, variant[1], o2, variant[2], o3, variant[3])
                    string_forms[1] = "(%d%s%d)%s%d%s%d" % ( variant[0], o1, variant[1], o2, variant[2], o3, variant[3])
                    string_forms[2] = "%d%s(%d%s%d)%s%d" % ( variant[0], o1, variant[1], o2, variant[2], o3, variant[3])
                    string_forms[3] = "%d%s%d%s(%d%s%d)" % ( variant[0], o1, variant[1], o2, variant[2], o3, variant[3])
                    string_forms[4] = "%d%s%d%s%d%s%d" % ( variant[0], o1, variant[1], o2, variant[2], o3, variant[3])
                    string_forms[5] = "(%d%s%d)%s(%d%s%d)" % ( variant[0], o1, variant[1], o2, variant[2], o3, variant[3])
                    string_forms[6] = "(%d%s%d%s%d)%s%d" % ( variant[0], o1, variant[1], o2, variant[2], o3, variant[3])
                    string_forms[7] = "%d%s(%d%s%d%s%d)" % ( variant[0], o1, variant[1], o2, variant[2], o3, variant[3])
                    string_forms[8] = "((%d%s%d)%s%d)%s%d" % ( variant[0], o1, variant[1], o2, variant[2], o3, variant[3])
                    string_forms[9] = "(%d%s(%d%s%d))%s%d" % ( variant[0], o1, variant[1], o2, variant[2], o3, variant[3])
                    string_forms[10] = "%d%s((%d%s%d)%s%d)" % ( variant[0], o1, variant[1], o2, variant[2], o3, variant[3])

                    for form in string_forms:
                        try:
                            if eval(form) == result:
                                matched_expressions.append(form)
                        except ZeroDivisionError:
                            pass

    matched_expressions = set(matched_expressions)
    matched_expressions = list(matched_expressions)
    return matched_expressions


def first_nonrepeating(string):
    """
    Return first letter from string which is there only once
    """
    for letter in string: #go letter by letter
        if string.count(letter) == 1: #letter is in string just once
            return letter

    return None #if thre is not such letter





combine4([6,6,5,2], 36)
