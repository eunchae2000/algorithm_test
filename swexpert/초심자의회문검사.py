t = int(input())
for tc in range(1, t+1):
    string = input()
    if string == string[::-1]:
        print(1)
    else:
        print(0)