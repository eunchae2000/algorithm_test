# 과제 1번 가장 많이 나온 문자열을 출력(대소문자 상관x)

# 입력받은 문자열을 모두 대문자로 바꿈
alpha = input().upper()  
count = []
# 입력받은 문자열을 배열로 바꾸고 중복된 문자열을 제거
result = list(set(alpha))

for i in result:
    # result의 i번째 문자가 alpha에 몇번나오는지 카운트하여 숫자를 count에 추가
    count.append(alpha.count(i))

# count 배열에서 제일 높은 숫자가 2개 이상인 경우
if count.count(max(count)) > 1:
    print("?")
else:
    # count에서 제일 높은 숫자의 인덱스를 구해서 result의 인덱스로 결과를 출력 
    print(result[count.index(max(count))])