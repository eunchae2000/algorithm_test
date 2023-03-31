n = int(input())
cnt = 0
subject = 666
while True:
    if '666' in str(subject):
        cnt += 1
    if cnt == n:
        print(subject)
        break
    subject += 1