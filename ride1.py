"""
ID: muffinl1
LANG: PYTHON3
TASK: ride
"""
def m(s):
  n = 1
  for c in s:
    n *= ord(c)

  return n%47

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

if m(fin.readline()) == m(fin.readline()):
  fout.write("GO\n")
else:
  fout.write("STAY\n")


fout.close()