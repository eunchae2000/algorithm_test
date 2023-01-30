x, y = map(int, input().split())

if(x<0):
    if(y<0):
        print("3")
    else:
        print("2")
else:
    if(y>0):
        print("1")
    else:
        print("4")
