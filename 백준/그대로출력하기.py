while True:
    try:
        print(input())
    # 입력 값이 없을 때
    except EOFError:
        break
