def sum_lists(list1: list, list2: list) -> list:
    unique_elements = list(set(list1 + list2))
    return [element**3 for element in unique_elements]


print("zadanie 6")
listA = [1, 2, 3]
listB = [3, 4, 5]
print("Suma sześcianów unikalnych elementów:", sum_lists(listA, listB))
