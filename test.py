def solution(arr):
    answer = [0,0]
    
    def compress(x, y, size):
        initial_value = arr[x][y]
        for i in range(x, x+size):
            for j in range(y, y+size):
                if arr[i][j] != initial_value:
                    halfsize = size//2
                    compress(x, y, halfsize)
                    compress(x, y+halfsize, halfsize)
                    compress(x+halfsize, y, halfsize)
                    compress(x+halfsize, y+halfsize, halfsize)
                    return
        answer[initial_value] += 1
    compress(0, 0, len(arr))
    return answer