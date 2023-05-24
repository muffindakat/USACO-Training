"""
ID: muffinl1
LANG: PYTHON3
TASK: friday
"""
fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')

n = int(fin.readline()[:-1])
count = [0, 0, 0, 0, 0, 0, 0]
month = [0,31, 28,31,30,31,30,31,31,30,31,30,31]
year = 1900
day = 14

for i in range (1900, 1900 + n):
  leap = False
  if i%4==0 and (i%100!=0 or i%400==0):
    leap = True
  
  if leap == True:
    month[2] = 29
  elif leap == False:
    month[2] = 28
  for k in range (1, 13):
    count[day%7] += 1
    day += month[k]
ans = str(count[0])
for m in range(1, 7):
  ans += " " + str(count[m])

fout.write(ans + "\n")
fout.close()