def solution(phone_book):
    # 해시맵 생성
    hash_map = {}
    for i in phone_book:
        hash_map[i] = 1
    
    # 접두어가 해시맵에 존재하는지 확인
    for j in phone_book:
        same = ""
        print(j)
        for num in j:
            print(num)
            same += num
            # 본인 자체일 경우 제외
            if same in hash_map and same != j:
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))