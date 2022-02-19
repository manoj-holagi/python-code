y = int(input())
def myfucn(y):
    count=0
    for i in range(1,y+1):
        if y%i==0:
          count = count+1
    return count
a = myfucn(y)
if a>2:
    print(y, "is not prime number")
else:
    print(y,"is prime number")