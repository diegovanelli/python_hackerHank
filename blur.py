m = [
  [10, 40 ,70],
  [110, 120, 130],
  [200, 220, 240]
]

for i in range(3):
  for j in range(3):
    a = []
    
    a.append(m[i][j])
    if (i < 2):
      a.append(m[i+1][j])
      if (j < 2):
        a.append(m[i+1][j+1])
      if (j > 0):
        a.append(m[i+1][j-1])
    if (i > 0):
      a.append(m[i-1][j])
      if (j > 0):
        a.append(m[i-1][j-1])
      if (j < 2):
        a.append(m[i-1][j+1])
    if (j < 2):
      a.append(m[i][j+1])
    if (j > 0):
      a.append(m[i][j-1])
    print(sum(a)/len(a))

    # 0,0 0,1 0,2
    # 1,0 1,1 1,2
    # 2,0 2,1 2,2
    print(a)
    
#print(soma



