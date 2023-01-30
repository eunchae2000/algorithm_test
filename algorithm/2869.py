A, B, V = map(int, input().split())
days = (V-B)/(A-B)

print(int(days) if days == int(days) else int(days)+1)