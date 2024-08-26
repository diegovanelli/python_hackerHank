matrix = [
  [112,42,83,119],
  [56,125,56,49],
  [15,78,101,43],
  [62,98,114,108]
]

n = len(matrix) // 2
print(n)
soma = 0
for i in range(n):
  for j in range(n):
    values = [
        matrix[i][j], matrix[i][2*n-j-1], matrix[2*n-i-1][j], matrix[2*n-i-1][2*n-j-1]
    ]
    soma += max(values)
#print(soma)


1,2,3,4,
5,6,7,8,
9,10,11,12,
13,14,15,16,

