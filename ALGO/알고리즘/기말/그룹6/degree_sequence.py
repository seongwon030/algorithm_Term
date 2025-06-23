from heapq import heapify, heappop, heappush

def is_graphical_sequence(degrees):
    """
    Havel-Hakimi 알고리즘을 이용해 주어진 수열이 degree sequence인지 판별
    """
    # 0보다 큰 차수만 남기고, 최대 힙을 만들기 위해 부호 반전
    degrees = [-d for d in degrees if d > 0]
    heapify(degrees)

    while degrees:
        # 가장 큰 차수 꺼냄
        d = -heappop(degrees)

        # 남은 정점 수보다 차수가 크면 불가능
        if d > len(degrees):
            return False

        temp = []
        for _ in range(d):
            if not degrees:
                return False
            x = -heappop(degrees) - 1
            if x < 0:
                return False
            if x > 0:
                temp.append(-x)

        for x in temp:
            heappush(degrees, x)

    return True

seq = list(map(int, input().split()))
print(is_graphical_sequence(seq))  # 출력: True