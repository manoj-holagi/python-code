st = input()
s = list(st)
for i in range(0,len(s),2):
  t=s[i]
  s[i]=s[i+1]
  s[i+1]=t

print("".join(s))