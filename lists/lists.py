def size_of_list(list):
    return len(list)

def add_elem_to_list(list, elem):
    list.append(elem)
    return list

def delete_elem_from_list(list, index = -1):
    list.pop(index)
    return list

def count_elements_in_list(list, x):
    return list.count(x)

def sort_list(list):
    list.sort()
    return list

def reverse(list):
    list.reverse()
    return list
