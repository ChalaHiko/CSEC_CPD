n = int(input())
ni = [int(i) for i in input().split()]
m = int(input())
shots = []
for i in range(m):
  shot = [int(i) for i in input().split()]
  shots.append(shot)
for x,y in shots:
  l = y -1
  r = ni[x-1] -y
  if x > 1 and x<n:
    ni[x-2] += l
    ni[x] += r
  elif x == 1:
    ni[x] += r
  elif x== n:
    ni[x-2] += l
  ni[x-1] = 0
for i in ni:
  print(i)