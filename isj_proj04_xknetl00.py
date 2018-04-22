#!/usr/bin/env python3

def can_be_a_set_member_or_frozenset(item):
    """ returns item if it is possible to isert it to set(), returns frozenset(item) otherwise """
    emptyset = set() #create new set
    try:
        emptyset.add(item) # makes an attempt to add item to set
        return item # if attempt was succesful

    except TypeError: # if item can't be inserted
        return frozenset(item) # return frozen set

def all_subsets(lst):
    """ returns all subsets of list """
    sublsts = [[]] # new list with empty sublist

    for elem in lst: # for every element of list
        sublsts = sublsts + [last + [elem] for last in sublsts] #append for every sublist new character

    return sublsts #returns complete sublists list


def all_subsets_excl_empty(*args, exclude_empty = True):
    """ returns all subsets of list with or without empty list (depending on parameter 'exclude_empty') """

    if exclude_empty == True:  #return sublists without empty
        return  list(filter(None, all_subsets(args)))# all previous function and filter out empty list
    elif exclude_empty == False:  #return sublists with empty

        return all_subsets(args) #calls previous function

###################### ASSERTS ######################################
assert can_be_a_set_member_or_frozenset(1) == 1
assert can_be_a_set_member_or_frozenset((1,2)) == (1,2)
assert can_be_a_set_member_or_frozenset([1,2]) == frozenset([1,2])

assert all_subsets(['a', 'b', 'c']) == [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]

assert all_subsets_excl_empty('a', 'b', 'c') == [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
assert all_subsets_excl_empty('a', 'b', 'c', exclude_empty = True) == [['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
assert all_subsets_excl_empty('a', 'b', 'c', exclude_empty = False) == [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]
