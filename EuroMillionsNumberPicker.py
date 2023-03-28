
import random


def random_number(z):
    x = random.randint(1, z)
    return x


def winner():
    nums = []
    lucky = []

    while len(nums) < 5:
        num = random_number(50)
        if num not in nums:
            nums.append(num)
    while len(lucky) < 2:
        ls = random_number(12)
        if ls not in lucky:
            lucky.append(ls)

    print(sorted(nums))
    print(sorted(lucky))


winner()


