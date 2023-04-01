n = int(input())

for i in range(1, n+1):
    num = sum((map(int, str(i))))  # i의 각 자릿수를 더하기
    total = num + i
    # 생성자가 있을 경우
    if (total == n):
        print(i)
        break
    # 생성자가 없을 경우
    if i == n:
        print(0)