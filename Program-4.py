def count_multiples(nums):
    counts = {i: 0 for i in range(1, 10)}
    for n in nums:
        for d in range(1, 10):
            if n % d == 0:
                counts[d] += 1
    return counts

nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(nums))

