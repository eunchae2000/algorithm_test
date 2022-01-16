N = int(input())
card = [i for i in range(1, N+1)]
card_list = []

while len(card) != 1:
    # 제일 위에 있는 카드를 pop
    card_list.append(card.pop(0))
    # 그 다음으로 위에 있는 카드를 맨 끝으로 보냄
    card.append(card.pop(0))
    
print(card[0])