count = 0

while True:
    n = int(input())
    count += 1
    if n == 0:
        break
    n1 = n*3
    if n1%2 == 0:
        n2 = n1//2
        n3 = 3*n2
        n4 = n3//9
        print(f'{count}. even {n4}')
    else:
        n2 = (n1+1)//2
        n3 = 3*n2
        n4 = n3//9
        print(f'{count}. odd {n4}')