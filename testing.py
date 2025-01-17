
if __name__ == '__main__':
    # import heapq
    # arr = [1,8,4,3,]
    # for i in range(len(arr)):
    #     arr[i] = arr[i] * -1
    # heapq.heapify(arr)
    # poped = arr.pop(0) * -1
    # print(poped)
    # print(arr)
    number = 11
    l = []
    while number:

        reminder = number % 2
        l.append(reminder)
        number = number//2
    count =0
    for i in l:
        if i == 1:
            count +=1
    print(count)