#!/usr/bin/python3
def element_at(my_lists, idx):
    for num in my_lists:
        index_num = my_lists.index(num)
        if index_num == idx:
            return my_lists[index_num]
    return None
