a, b = map(int, input().split())

def gen(number):
    generator = []
    for i in range(1, number):
        count=0
        for n in str(i):
            count += int(n)
        count += i
        if count == number:
            generator.append(i)
    return generator
selfnumber = []
for i in range(a,b+1):
    generator = gen(i)
    if not generator:
        selfnumber.append(i)

print(sum(selfnumber))
