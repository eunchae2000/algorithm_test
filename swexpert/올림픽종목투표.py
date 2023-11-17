t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    content = list(map(int, input().split()))
    judge = list(map(int, input().split()))
    answer = [0 for _ in range(n)]
    for i in range(len(judge)):
        for j in range(len(content)):
            if judge[i] >= content[j]:
                answer[j] += 1
                break
    print(f'#{tc} {answer.index(max(answer))+1}')