def num():
    n = int(input())
    nm = list(map(int, input().split()))
    a, b = map(int, input().split())

    max=nm[a-1] #최대값 확인
    index=a-1 #최대값의 인덱스 확인
    for i in range(a-1, b):
        if max < nm[i]: #최대값의 비교
            max = nm[i] #최대값보다 크면 최대값 갱신
            index=i #인덱스 갱신
    return index+1 #인덱스 보다 1 크게 반환

print(num())