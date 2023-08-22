numbers = []
for i in range(1, 11):
    numbers.append(i ** 2)

print(numbers)

# squares = [i ** 2 for i in range(1, 101)]
# print(squares)

cubes = [i ** 3 for i in range(1, 11)]
print(cubes)

three_cubes = [i for i in range(3, 31, 3)]
print(three_cubes)