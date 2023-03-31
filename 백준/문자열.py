num = int(input())
result = []
for i in range(num):
    string = input()
    result.append(string[0]+string[-1])

for _ in range(num):
    print(result[_])
