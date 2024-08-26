arr = [[11,2,4], [4,5,6], [10,8,-12]]

max = len(arr)-1
min = 0
count1 = 0
count2 = 0
for i in arr:
  count1 += i[min]
  min += 1
  count2 += i[max]
  print(count2)
  max -= 1
print(abs(count1 - count2))