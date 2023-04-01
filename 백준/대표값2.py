import sys

score = []

for i in range(5):
    score.append(int(input()))

score.sort()

print(int(sum(score)/5))
print(score[2])