n = int(input())

def check():
    for i in range(len(tel)-1):
        if tel[i] == tel[i+1][0:len(tel[i])]:
            print(len(tel[i]))
            print("NO")
            return
    print("YES")

for i in range(n):
    num = int(input())
    tel = [input() for _ in range(num)]
    tel.sort()
    check()
