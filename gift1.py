"""
ID: muffinl1
LANG: PYTHON3
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

n = int(fin.readline()[:-1])

account = dict()
for i in range(n):
  account[fin.readline()[:-1]] = 0

for i in range(n):
  giver = fin.readline()[:-1]
  money, cnt = map(int, fin.readline()[:-1].split())
  if cnt==0:
    continue
  remain = money%cnt
  account[giver]=account[giver]-money+remain
  money = money//cnt

  for j in range(cnt):
    name = fin.readline()[:-1]
    account[name]+=money

for I, J in account.items():
  fout.write(I + " " + str(J) + "\n")

fout.close()