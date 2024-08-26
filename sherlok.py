

if __name__ == '__main__':


  was = dict()
  s = "kkkk"

  n = len(s)
  for i in range(n):
      for j in range(i, n):
          cur = s[i:j + 1]
          cur = ''.join(sorted(cur))
          print(cur)
          was[cur] = was.get(cur, 0) + 1

  print(was)
  ans = 0
  tem = 0
  for x in was:
      v = was[x]
      tem += v
      print("v: " + str(v))
      print("(v * (v - 1)): " + str(v * (v - 1)))
      print("(v * (v - 1)) // 2: " + str((v * (v - 1)) // 2))
      ans += (v * (v - 1)) // 2

  print(ans)
  print(tem // 2)
  