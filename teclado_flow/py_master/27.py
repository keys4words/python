def remove_from_list(lst, item):
    """
    Removes an item from a list
    :param lst:
    :param item:
    :return:
    """
    while(item in lst):
        lst.remove(item)

list1 = [1, 2, 1, 1, 1, 1, 3]
remove_from_list(list1, 1)
print(list1)