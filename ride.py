"""
ID: muffinl1
LANG: PYTHON3
TASK: ride
"""
def m(s):
  n = 1
  for c in s:
    n *= ord(c)-64

  return n%47

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
a = m(fin.readline()[:-1])
b = m(fin.readline()[:-1])


if a == b:
  fout.write("GO\n")
else:
  fout.write("STAY\n")


fout.close()