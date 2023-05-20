def solution(cacheSize, cities):
    answer = 0
    arr = []
    for city in cities:
        city = city.lower()
        if cacheSize:
            if city not in arr:
                if len(arr) == cacheSize:
                    arr.pop(0)
                arr.append(city)
                answer += 5
            else:
                arr.pop(arr.index(city))
                arr.append(city)
                answer += 1
        else:
            answer += 5

    return answer