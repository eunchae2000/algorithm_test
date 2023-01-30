time = int(input())

hour = time//3600
minute = (time%3600)//60
second = (time%3600)%60

print(str(hour)+"시간" + str(minute)+"분" + str(second)+"초")