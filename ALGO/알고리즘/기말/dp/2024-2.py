def subset_sum(nums, target):
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return True  # 첫 번째 성공한 부분집합만 찾으면 되므로 바로 True 반환
        if total > target:
            return False
        for i in range(start, len(nums)):
            if backtrack(i + 1, path + [nums[i]], total + nums[i]):
                return True
        return False

    found = backtrack(0, [], 0)
    return found, result[0] if found else []

# 파일에서 입력 받기
with open("input3.txt", "r") as f:
    lines = f.read().splitlines()

K = int(lines[0])
index = 1

for _ in range(K):
    N, W = map(int, lines[index].split())
    index += 1
    nums = list(map(int, lines[index].split()))
    index += 1

    found, subset = subset_sum(nums, W)
    if found:
        print("Yes", subset)
    else:
        print("No")