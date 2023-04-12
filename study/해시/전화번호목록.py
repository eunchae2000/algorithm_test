# def solution(phone_book):
#     dict = {}
#     for phone in phone_book:
#         dict[phone] = 1
    
#     for phone in phone_book:
#         check = ""
#         for same in phone:
#             check += same
#             if check in phone_book and check != phone:
#                 return False
#     return True

def solution(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p2):
            return False
    return True