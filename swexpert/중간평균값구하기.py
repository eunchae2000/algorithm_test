t = int(input())
for tc in range(1, t+1):
    nums = list(map(int, input().split()))
    num_list = nums
    num_list.remove(max(num_list))
    num_list.remove(min(num_list))
    answer = round(sum(num_list)/len(num_list))
    print(f'#{tc} {answer}')