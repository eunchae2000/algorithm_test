baseString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
base = {i:ord(i)-65 for i in baseString}
for a in baseString.lower():
    base[a] = ord(a)-71

for b in range(0, 10):
    base[str(b)] = ord(str(b))+4

base["+"] = 62
base["-"] = 63

t = int(input())
for i in range(1, t+1):
    string = input()
    answer = ""
    for j in range(0, len(string), 4):
        temp = ""
        for k in string[j:j+4]:
            temp += format(base[k], 'b').zfill(6)
        for m in range(0, len(temp), 8):
            answer += chr(int(temp[m:m+8], 2))
    print("#{} {}".format(i, answer))