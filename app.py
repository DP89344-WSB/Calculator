def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def concatenate(str1, str2):
    return str1 + str2

def reverse_string(s):
    return s[::-1]

def get_max(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)

def get_average(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)

def count_occurrences(lst, value):
    return lst.count(value)