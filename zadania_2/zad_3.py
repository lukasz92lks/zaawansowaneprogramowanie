def is_even(number: int) -> bool:
    return number % 2 == 0

even_check = is_even(5)
print("zadanie 3")
if even_check:
    print("Liczba jest parzysta.")
else:
    print("Liczba nie jest parzysta.")