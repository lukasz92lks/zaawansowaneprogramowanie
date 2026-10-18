def show_name(names):
    for name in names:
        print(name)

print ("zadanie 1")
list_of_names = ["Jan", "Anna", "Piotr", "Katarzyna"]
show_name(list_of_names)

def multiply_numbers(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result

    def multiply_with_comprehension(numbers):
    return [number * 2 for number in numbers]

print("zadanie 2")
five_numbers = [1, 2, 3, 4, 5]
print("Pętla for:", multiply_numbers(five_numbers))
print("Lista składana:", multiply_with_comprehension(five_numbers))

def even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]
print("Zadanie 3")
ten_numbers = list(range(1, 11))
print("Liczby parzyste:", even_numbers(ten_numbers))

def every_other_numbers(numbers):
    return [number for i, number in enumerate(numbers) if i % 2 == 0]

print("Zadanie 4")
print("Każda druga liczba:", every_other_numbers(five_numbers))