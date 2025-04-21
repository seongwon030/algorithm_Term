def can_partition(nums):
    total = sum(nums)
    if total % 3 != 0:
        return False  # 전체 합이 홀수면 절대 나눌 수 없음

    target = total // 3
    used = [False] * len(nums)

    def backtrack(k, start, current_sum):
        if k == 1:
            return True
        if current_sum == target:
            return backtrack(k-1,0,0)

        for i in range(start, len(nums)):
            if not used[i] and current_sum + nums[i] <= target:
                used[i] = True
                if backtrack(k, i+1, current_sum + nums[i]):
                    return True
                used[i] = False

        return False

    return backtrack(3,0,0)

n = int(input())
nums = list(map(int, input().split()))
print("Can partition:", can_partition(nums))  # True
