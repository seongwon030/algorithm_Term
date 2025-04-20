import sys
input = sys.stdin.readline

def ccw(p1 ,p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])

def convexhull(points):
    convex = []
    for p3 in points:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3) > 0:
                break
            convex.pop()
        convex.append(p3)

    return convex

n = int(input())
positions = []
for _ in range(n):
    positions.append(list(map(int, input().split())))

positions = sorted(positions, key=lambda pos: (pos[0], pos[1]))
arr = convexhull(positions)

positions.reverse()
arr.extend(convexhull(positions))

result = list(set(tuple(p) for p in arr))
for x,y in result:
    print(x,y)