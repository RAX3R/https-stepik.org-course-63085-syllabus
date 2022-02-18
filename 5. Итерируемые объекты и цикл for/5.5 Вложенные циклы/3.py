n, m = list(map(int, input().split()))

count = 0

for a in range(0, 1001):
    for b in range(0, 1001):
        if (a * a + b) == n and (a + b * b) == m:
            count += 1

print(count)
