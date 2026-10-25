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
