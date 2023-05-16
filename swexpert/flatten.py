for i in range(10):
    dump = int(input())
    arr = list(map(int, input().split()))
    while dump:
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
        dump -= 1
    print("#{} {}".format(i+1, max(arr)-min(arr)))