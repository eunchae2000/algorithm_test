t = int(input())

def check(num_list):
    num = len(num_list)
    for i in range(num-1):
        if num_list[i+1].startswith(num_list[i]):
            print("NO")
            return 
    print("YES")
    return     

for _ in range(t):
    n = int(input())
    num_list = [input() for _ in range(n)]
    num_list.sort()
    check(num_list)
