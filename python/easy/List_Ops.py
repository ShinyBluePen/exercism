"""List Ops

https://exercism.org/tracks/python/exercises/list-ops
"""

def append(list1: list, list2: list) -> list:
    "Add contents of list2 to the end of list1"
    for i in list2:
        list1 += [i]
    return list1

def concat(lists: list) -> list:
    "Return a flattened list of arbitrary depth excluding Null values."
    flatter_list = []
    for list in lists:
        append(flatter_list, list)
    return flatter_list
    
    # # Apparently the below code is /too/ flat.
    # flat_list = []
    # for item in lists:
    #     if item != None:
    #         if isinstance(item, list):
    #             flat_list += concat(item)
    #         else:
    #             flat_list.append(item) # the local append only works for adding lists together...
    # return flat_list

def filter(function, list: list) -> list:
    "Return the list of all items for which function(item) applied to a list is True."
    return [i for i in list if function(i)]

def length(list: list) -> int:
    "Return the total number of items in a list."
    return sum([1 for c in list])

def map(function, list: list) -> list:
    "Return a list of results of applying a function to all items in a list."
    return [function(i) for i in list]

def foldl(function, list: list, initial) -> list:
    "Fold (reduce) each item into an accumulator from the left."
    acc = initial
    for i in list:
        acc = function(acc, i)
    return acc

def foldr(function, list: list, initial) -> list:
    "Fold (reduce) each item into an accumulator from the right."
    acc = initial
    for i in list[::-1]:
        acc = function(i, acc)
    return acc

def reverse(list: list) -> list:
    "Return a list with all the original items reversed."
    return list[::-1]
