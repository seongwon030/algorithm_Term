def perm(k):
    if k == n:
        print(data)
        return

    for i in range(k, n): # k ~ n-1까지 위치와 바꾸기
        data[k], data[i] = data[i], data[k] # 스왑
        perm(k+1) # 다음 자리 호출
        data[k], data[i] = data[i], data[k] # 백트래킹


data = [1,2,3]
n = len(data)
perm(0)