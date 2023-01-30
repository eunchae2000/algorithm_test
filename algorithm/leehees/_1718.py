s = str(input())

num=s[1:].split("H")

result = 0

for i in range(0, len(s)):
    if (s[i] == 'C'):
        if (s[i+1]=='H'):
            result+=12
        else:
            result += int(num[0])*12
    if(s[i] == 'H'):
        if(i==len(s)-1):
            result+=1
        else:
            result += int(num[1])*1

print(result)
