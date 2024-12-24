#1

def solution(text, ending):
    return text.endswith(ending)


#2

def accum(st):
    return '-'.join((ch.upper() + ch.lower() * i) for i, ch in enumerate(st))


#3

def DNA_strand(dna):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in dna)


#4

def sum_two_smallest_numbers(numbers):
    # Sort the list in ascending order
    numbers.sort()
    # Return the sum of the first two elements
    return numbers[0] + numbers[1]



#5

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))