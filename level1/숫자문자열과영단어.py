def solution(s):
    # 인덱스와 문자열을 동시에 저장하여 사용하고 싶은 경우에는 딕셔너리나 배열을 사용
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for index, alpha in enumerate(number):
        s = s.replace(alpha, str(index))
    return s
print(solution("one4seveneight"))

# def solution(s):
#     number = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
#     for alpha in number.items():
#         s = s.replace(alpha[0], str(alpha[1]))
#     return int(s)