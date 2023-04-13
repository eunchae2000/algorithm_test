n = int(input())
city = [map(int, input().split())]
budget = int(input())
if sum(city) < budget:
    print(max(city))
else:
    result = budget//len(city)
    count = 0
    num = 0
    for i in range(len(city)):
        if city[i]<result:
            num += 1
            count += (result-city[i])
    answer = (count//(len(city)-num))+result
print(answer)