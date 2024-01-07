# def solution(n, k, cmd):
#     result = ''
#     arr = [i for i in range(n)]
#     trash = []
    
#     index = k
#     for c in cmd:
#         if len(c) == 3:
#             num1, num2 = c[0], c[2]
#             if index > len(arr):
#                 index = arr[-1]
#             if num1 == 'D':
#                 index += int(num2)
#                 if len(arr) < index:
#                     index = n-1
#                     if index not in arr:
#                         index -= 1
#             elif num1 == 'U':
#                 index -= int(num2)
#                 if index < 0:
#                     index = 0
#                     if index not in  arr:
#                         index -= 1
#         else:
#             num1 = c[0]
#             if num1 == 'C':
#                 print("index", index)
#                 trash.append(arr[index])
#                 arr.remove(arr[index])
#                 index += 1
#                 print(trash)
#             elif num1 == 'Z':
#                 if len(trash) != 0:
#                     arr.append(trash.pop())
#     arr.sort()
#     for i in range(n):
#         if i in arr:
#             result += 'O'
#         else:
#             result += 'X'
#     return result

def solution(n, k, cmd):
    answer = ["O"]*n
    trash = []
    up = [i-1 for i in range(n+2)]
    down = [i+1 for i in range(n+1)]
    
    k += 1
    
    for c in cmd:
        if c.startswith('C'):
            trash.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n<down[k] else down[k]
        elif c.startswith('Z'):
            restore = trash.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
        else:
            action, num = c.split()
            if action == 'U':
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]
    for i in trash:
        answer[i-1] = 'X'
    return ''.join(answer)

print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))