"""
ID: muffinl1
LANG: PYTHON3
TASK: beads
"""
fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')

n = int(fin.readline()[:-1])
line = fin.readline()[:-1]
countfirst = 0
countlast = 0
#check beginning for a block of same
firstletter = ''
for i in range(0, n):
  if(line[i] != 'w'):
    firstletter = line[i]
for i in range(0, n):
  if line[i] == firstletter:
    countfirst+=1
  elif line[i] == 'w':
    countfirst += 1
  elif line[i] != firstletter and line[i] != 'w':
    break
#check very end to see if its the same as first block
letter = ""
b = 0
for i in range(n-1, -1, -1):
  if line[i] == firstletter:
    countfirst+=1
  elif line[i] != firstletter and line != 'w':
    letter = line[i]
    break
  elif line[i] == 'w':
    countfirst += 1
  b = i
for i in range(b-1, -1, -1):
  if line[i] == letter:
    countlast += 1
  elif line[i] == 'w':
    countlast += 1
  elif line[i] != letter and line[i] != 'w':
    break

ans = str(countfirst + countlast)
fout.write(ans + "\n")
fout.close()
#if so skip those and add to count
#and then count another block from there
#goodo lucko imma sleep now bye