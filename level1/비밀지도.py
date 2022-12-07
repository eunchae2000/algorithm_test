def solution(n, arr1, arr2):
    graph1 = []
    for i in arr1:
        binary_value = bin(i)[2:].rjust(n,'0')
        graph1.append(list(binary_value))

    graph2 = []
    for i in arr2:
        binary_value = bin(i)[2:].rjust(n,'0')
        graph2.append(list(binary_value))

    for i in range(n):
        for j in range(n):
            graph1[i][j] = int(graph1[i][j]) + int(graph2[i][j])

    answer = []
    for i in graph1:
        tmp = ''
        for j in i:
            if j == 0:
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer