# 나이 순으 로 정렬한 후 나이가 같다면 먼저 가입한 회원이 앞으로 오는 순서로 정렬하는 프로그램을 작성.

# 입력받을 정보의 개수를 입력
N = int(input())
# 나이와 이름을 문자열 형태로 입력받아 리스트에 저장
info = [list(map(str, input().split())) for _ in range(N)]

# 나이순으로 정렬하기 위해서 리스트의 나이를 비교 // 이름은 입력받은 순서대로 정렬하기 때문에 따로 정렬과정 필요x
info.sort(key=lambda x:int(x[0]))

# 리스트 요소를 하나씩 출력
for i in info:
    for j in i:
        print(j, end=" ")
    print()