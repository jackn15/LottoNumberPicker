import random


def random_number(z):
    x = random.randint(1, z)
    return x


def winner():
    nums = []

    while len(nums) < 6:
        num = random_number(59)
        if num not in nums:
            nums.append(num)

    print(sorted(nums))


winner()
