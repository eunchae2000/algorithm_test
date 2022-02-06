number = (list(map(str, input().split())))
number.sort(key=lambda x : x*3, reverse=True)

print(str(int(''.join(number))))