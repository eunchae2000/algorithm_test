n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = []

if max(arr) == 0:
    print("SAD")
else:
    num = sum(arr[0:m])
    value = num
    count = 1
    for i in range(m, n):
        # 슬라이딩 윈도우
        print("+", arr[i-m])  # 슬라이딩 윈도우 앞의 값
        value -= arr[i-m]
        print("-", arr[i])  # 슬라이딩 윈도우 뒤의 값
        value += arr[i]
        # value의 최대 값
        if value > num:
            num = value
            count = 1
        # 최대 값을 몇 일 동안 반복하는지 count
        elif value == num:
            count += 1
    print(num)
    print(count)