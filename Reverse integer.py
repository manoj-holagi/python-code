n = int(input())
s = str(n)
rs = ""
for i in range (len(s)-1,-1,-1):
  rs = rs+s[i]
a = int(rs)
print(a)