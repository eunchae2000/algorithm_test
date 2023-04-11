import sys
word1, word2 = sys.stdin.readline().strip(), sys.stdin.readline().strip()
len_word1, len_word2 = len(word1), len(word2)
cache = [0]*len_word2

for i in range(len_word1):
    count = 0
    for j in range(len_word2):
        if count < cache[j]:
            count = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = count + 1
print(max(cache))