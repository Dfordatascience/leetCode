def maximum_subarray():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    max_sum = 0
    count = 0
    for i in nums:
        count += i
        if count > 0 and  count > max_sum:
            max_sum = count
        if  count < 0 :
            count = 0

    return max_sum




if __name__ == '__main__':
    print(maximum_subarray())