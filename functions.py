import string


def is_palindrome(text: str) -> bool:
    text = text.lower().replace(" ", "")
    return text == text[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n nie moze byc ujemne")

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    return sum(1 for char in text.lower() if char in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 1:
        raise ValueError("Discount must be between 0 and 1")
    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


def word_frequencies(text: str) -> dict:
    text = text.lower().translate(
        str.maketrans("", "", string.punctuation)
    )
    words = text.split()
    frequencies = {}

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True