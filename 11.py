lines=[]
while True:
  line=input()
  if line=='00000':
    break
  else:
    lines.append(list(map(int,line.split())))

numCols=len(lines[0])
numRows=len(lines)
# print(numCols, numRows)

prods=[]

for i in range(numRows):
  for j in range(numCols-3):
    prod=1
    for k in range(4):
      prod*=lines[i][j+k]
    prods.append(prod)

for i in range(numRows-3):
  for j in range(numCols-3):
    prod=1
    for k in range(4):
      prod*=lines[i+k][j+k]
      # print(lines[i+k][j+k])
    # print(prod)
    prods.append(prod)
    
for i in range(numRows-3):
  for j in range(numCols-1, 3, -1):
    prod=1
    for k in range(4):
      # print(i+k, j-k)
      prod*=lines[i+k][j-k]
      # print(lines[i+k][j-k])
    # print(prod)
    prods.append(prod)
    

print(max(prods))


