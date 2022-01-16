# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 길이와 알파벳 순서에 따라 정렬하는 프로그램

# N개의 단어를 입력받기 위해 N을 입력
N = int(input())
# N개의 단어를 입력받고 리스트로 저장
alpha = [input() for _ in range(N)]
# 리스트 요소의 중복을 제거하기 위해 set 사용
alpha = list(set(alpha))
# 리스트의 요소를 먼저 길이와 비교하여 정렬하고 길이가 같으면 알파벳 순서로 정렬
alpha.sort(key=lambda x:(len(x), x))

# 리스트의 요소를 하나씩 출력
for i in alpha:
    for j in i:
        print(j, end="")
    print()