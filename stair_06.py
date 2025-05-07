def count_ways(n):
    if n == 0 or n == 1:
        return 1

    prev2, prev1 = 1, 1

    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1

n = 5
print(f"Ways to climb {n} stairs: {count_ways(n)}")
