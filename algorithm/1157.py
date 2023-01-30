s = input().upper()
ss = list(set(s))
count = 0

for i in range(len(ss)):
    for j in range(len(s)):
        if ss[i] == s[j]:
            count += 1
