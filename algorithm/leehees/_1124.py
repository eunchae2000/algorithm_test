s = str(input())

num=s[1:].split("H")

result = 0

for i in range(0, len(s)):
    if (s[i] == 'C'):
        result += int(num[0])*12
    if(s[i] == 'H'):
        result += int(num[1])*1

print(result)
