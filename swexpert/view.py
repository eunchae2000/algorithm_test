def solution(arr):
    count = 0
    for i in range(2, len(arr)-2):
        current = arr[i]
        left = max(arr[i-2:i])
        if current < left:
            continue
        right = map(arr[i+1:i+3])
        if current < right:
            continue
        around_current = max(left, right)
        count += (current-around_current)
    return count

if __name__ == "__main__":
    for i in range(10):
        n = int(input())
        building = list(map(int, input().split()))
        print("#{} {}".format(i+1, solution(building)))