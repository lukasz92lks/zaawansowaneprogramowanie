def compare_element(target: list, searched: int) -> bool:
    return searched in target


print("zadanie 5")
my_list = [1, 2, 3, 4, 5]
print("Czy liczba 3 znajduje się w liście?", compare_element(my_list, 6))
