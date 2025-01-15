def solution(cacheSize, cities):
    if cacheSize == 0 :
        return len(cities) * 5

    cache = []  
    total_time = 0

    for city in cities:
        city = city.lower()  # 대소문자 구분하지 않음

        if city in cache :
            total_time += 1
            cache.remove(city)
            cache.append(city)
        else :
            # Cache miss: 실행 시간 +5
            total_time += 5
            # 캐시가 꽉 찼으면 가장 오래된 항목 제거
            if len(cache) >= cacheSize :
                cache.pop(0)
            # 새 도시를 캐시에 추가
            cache.append(city)

    return total_time
