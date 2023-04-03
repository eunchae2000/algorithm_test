def solution(phone_book):
    dict = {}
    for phone in phone_book:
        dict[phone] = 1
    
    for phone in phone_book:
        check = ""
        for same in phone:
            check += same
            if check in phone_book and check != phone:
                return False
    return True