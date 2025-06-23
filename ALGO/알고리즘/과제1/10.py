def max_value(n, items, w):
    max_profit = float('-inf')

    def dfs(index, current_volume, current_value, disposal_cost):
        nonlocal max_profit

        if current_volume > w:
            return

        if index == n:
            max_profit = max(max_profit, current_value - disposal_cost)
            return

        dfs(index+1, current_volume + items[index][0], current_value + items[index][1], disposal_cost)
        dfs(index+1, current_volume, current_value, disposal_cost + items[index][2])

    dfs(0, 0, 0, 0)
    return max_profit

n = int(input())
items = [tuple(map(int, input().split())) for _ in range(n)]
w = int(input())

print(max_value(n, items, w))