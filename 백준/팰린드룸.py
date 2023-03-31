string = input()
result = ''
for i in string:
    result = i + result

if(string == result):
    print(1)
else:
    print(0)