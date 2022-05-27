from random import randint
from collections import Counter

def generate_numbers():
    draws = []
    while len(draws) < 8:
        draws.append(randint(1, 20))
    is_duplicates = check_duplicates(draws)
    return draws, is_duplicates

def check_duplicates(draws):
    counters = Counter(draws)
    numbers_with_duplicates = 0
    for row in counters.values():
        if row > 1:
            numbers_with_duplicates += 1
    return True if numbers_with_duplicates > 2 and len(draws) == 8 else False



print(generate_numbers())

