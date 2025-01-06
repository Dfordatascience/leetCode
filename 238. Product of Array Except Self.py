def product_arrays(nums):
    n = len(nums)
    result = [0]* n
    for i in range(n):
        count = 1
        for j in range(i+1,n):
            count *= nums[j]
        result[i] = count
    return result

if __name__ == '__main__':
    print(product_arrays([1,2,3,4]))