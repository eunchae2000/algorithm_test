x = int(input())
line = 1

# 1. 입력받은 수가 line보다 클 경우 반복
# 2. 해당되는 경우 x는 x - line
# 3. line은 1증가 된다
while x>line:
    x -= line
    line += 1

if line%2==0:
    a = x
    b = line - x + 1
else:
    a = line - x + 1
    b = x

print(str(a) + '/' + str(b))