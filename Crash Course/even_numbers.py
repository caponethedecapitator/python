numbers = list(range(2, 11, 2))
print(numbers)

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

odd_numbers = [i for i in range(1, 11) if i % 2 != 0]
print(odd_numbers)