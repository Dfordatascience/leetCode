def twoSum( nums, target):
    h = {}

    for i, num in enumerate(nums):
        h[num] = i

    for i in range(len(nums)):
        val = target - nums[i]
        if val in h and i != h[val]:
            return [i,  h[val]]
    return

if __name__ =="__main__":
    nums =  [3,3]
    target = 6
    print( twoSum( nums, target))