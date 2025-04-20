def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False  # 전체 합이 홀수면 절대 나눌 수 없음

    target = total // 2

    def backtrack(index, current_sum):
        # 종료 조건
        if current_sum == target:
            return True
        if current_sum > target or index == len(nums):
            return False

        # 현재 원소를 포함하거나, 포함하지 않음
        include = backtrack(index + 1, current_sum + nums[index])
        exclude = backtrack(index + 1, current_sum)

        return include or exclude

    return backtrack(0, 0)


# 예시 실행
nums = [1, 5, 11, 5]
print("Can partition:", can_partition(nums))  # True
