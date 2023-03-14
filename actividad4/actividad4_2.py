nums = [3, 4, 8, 5, 5, 22, 13, 33, 5, 47, 23, 32, 70, 71 ]
for i in range(2, 10):
    nums = list(filter(lambda x: x == i or x % i, nums))

print(nums)