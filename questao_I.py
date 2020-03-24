nums = [2, 7, 11, 15]

def main():
    for n in nums:
        for m in nums:
            if nums.index(n) == nums.index(m):
                pass
            elif m + n == 9:
                return nums.index(n), nums.index(m)

print(main()) 