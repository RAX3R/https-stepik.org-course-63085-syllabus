nums = list(map(int, input().split()))

for num in nums:
    for _ in range(1, num + 1):
        print('*', end='')
    print()
