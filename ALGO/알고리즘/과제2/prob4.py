import sys
input = sys.stdin.readline

def ccw(left,mid,right):
  lx,ly = left
  mx, my = mid
  rx,ry = right

  cross = (mx - lx)*(ry - ly) - (rx - lx)*(my - ly)
  return cross > 0

def convex_hull_pos(positions):
  convex = []
  for p3 in positions:
    while len(convex) >= 2:
      p1, p2 = convex[-2], convex[-1]
      if ccw(p1,p2,p3):
        break
      convex.pop()
    convex.append(p3)
  
  return convex

n = int(input())
positions = []
for i in range(n):
  positions.append(list(map(int,input().split())))

positions = sorted(positions, key=lambda x: (x[0],x[1]))
arr = convex_hull_pos(positions)

positions.reverse()
arr.extend(convex_hull_pos(positions))

result = list(set([tuple(p) for p in arr]))
print("-----출력------")
for x,y in result:
  print(x,y)