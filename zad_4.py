def every_other_numbers(numbers):
    return [number for i, number in enumerate(numbers) if i % 2 == 0]


print("Zadanie 4")
ten_numbers = list(range(1, 11))
print("Każda druga liczba:", every_other_numbers(ten_numbers))
