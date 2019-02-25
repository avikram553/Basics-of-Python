class area:
  def __init__(self,r=0,l=0,b=0):
    self.r=r
    self.l=l
    self.b=b
  def square(self,l):
     a=l*l
     print("area is ",a)
  def rectangle(self,l,b):
     a=l*b
     print("area is ",a)
  def circle(self,r):
     a=3.14*r*r
     print("area of circle is",a)

a = area()
ip = input("1.Square\n2.Rectangle\n3.Circle")
if(ip=='1'):
  l = int(input("Enter the length ="))
  a.square(l)
elif(ip=='2'):
  l = int(input("Enter the length"))
  b = int(input("Enter the breadth of the rectangle"))
  a.rectangle(l,b)
elif(ip=='3'):
  r = int(input("Enter the radius of the circle"))
  a.circle(r)
else:
  print("Choose the correct option")
