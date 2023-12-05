def fib(n, count):
    count += 1
    if n==1 or n==2:
        return count
    else:
        count += 1
        return (fib(n - 1, count) + fib(n - 2, count))

def fibonacci(n, count):
    fibo = [0, 1]
    for i in range(2,n+1):
        count += 1
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo[n], count+1


n = int(input())
count1, count2 = 0, 0

print(*fibonacci(n, count2-2))