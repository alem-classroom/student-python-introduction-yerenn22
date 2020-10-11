def size_of_list(list):
    return len(list)

def add_elem_to_list(list, elem):
    list.append(elem)
    return list

def delete_elem_from_list(list, index = -1):
    list.pop(index)
    return list

def count_elements_in_list(list, x):
    counter = 0
    for i in range(len(list)):
        if list[i] == x:
            counter += 1
    return counter

def sort_list(list):
    return list.sort()

def reverse(list):
    return list.reverse()
