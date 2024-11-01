def solution(arr):
    # 압축된 0과 1의 개수를 저장할 변수
    result = [0, 0]

    def compress(x, y, size):
        initial_value = arr[x][y]
        # 주어진 영역이 모두 같은 값인지 확인
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != initial_value:
                    # 다르면 4개의 하위 영역으로 나누어 압축
                    half_size = size // 2
                    compress(x, y, half_size)         # 왼쪽 위
                    compress(x, y + half_size, half_size)   # 오른쪽 위
                    compress(x + half_size, y, half_size)   # 왼쪽 아래
                    compress(x + half_size, y + half_size, half_size)  # 오른쪽 아래
                    return

        # 모든 값이 같다면 압축 결과에 반영
        result[initial_value] += 1

    # 전체 배열을 하나의 영역으로 시작하여 압축
    compress(0, 0, len(arr))

    return result

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
    