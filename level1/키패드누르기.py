def dist(i, center, hand_row, hand_col):
    center_row = center.index(i)
    center_col = 1
    
    distance = (abs(hand_row-center_row) + abs(hand_col-center_col))
    return distance


def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]
    center = [2, 5, 8, 0]
    left_hand_row = 3; left_hand_col = 0
    right_hand_row = 3; right_hand_col = 0
    
    for i in numbers:
        if i in left:
            answer += 'L'
            left_hand_row = left.index(i)
            left_hand_col = 0
        
        elif i in right:
            answer += 'R'
            right_hand_row = right.index(i)
            right_hand_col = 2
        
        elif i in center:
            left_dist = dist(i, center, left_hand_row, left_hand_col)
            right_dist = dist(i, center, right_hand_row, right_hand_col)
            
            if left_dist > right_dist:
                right_hand_row = center.index(i)
                right_hand_col = 1
                answer += 'R'
            elif left_dist < right_dist:
                left_hand_row = center.index(i)
                left_hand_col = 1
                answer += 'L'
            elif left_dist == right_dist:
                if hand == 'right':
                    right_hand_row = center.index(i)
                    right_hand_col = 1
                    answer += 'R'
                elif hand == 'left':
                    left_hand_row = center.index(i)
                    left_hand_col = 1
                    answer += 'L'
    
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))