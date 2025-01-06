def contains_duplicate():
    nums = [7,10,5,5,6,6,4,10,5,4]
    h = {}
    for i in nums:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1

    for i in h:
        if h[i] == 2:
            return True
    return False

if __name__ == '__main__':
    print(contains_duplicate())