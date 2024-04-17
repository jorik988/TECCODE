# функцию возвращает список, содержащий только уникальные элементы из исходного списка
def unique_elements_a(lst):
    unique_set = set(lst)
    unique_list = list(unique_set)
    return unique_list

original_numbers = [1, 2, 2, 3, 4, 5, 3, 6, 4]
print(unique_elements_a(original_numbers))


def unique_elements_b(lst):
    unique_list = []
    for i in lst:
        if not isinstance(i, int):
            continue 
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


mylist = [1, 2, 3, 4, 5, 3, 6, 4]
print(unique_elements_b(mylist))
