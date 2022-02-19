number = int(input())

print([i for i in range(number, number * number + 1) if i % 2 == 1])
