def even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]
print("Zadanie 3")
ten_numbers = list(range(1, 11))
print("Liczby parzyste:", even_numbers(ten_numbers))
