from rich.console import Console
print("For This Exercise You Will Be Asked Four Numbers Of Your Choice  " + Style.RESET_ALL)
a=int (input("1:"))
b=int (input("2:"))
c=int (input("3:"))
d=int (input("4:"))
if a % 2 == 0:
    print("this number is EVEN!")
else:
    print("this number is ODD!")
    if b % 2 == 0:
        print("this number is EVEN!")
    else:
          print("this number is ODD!")   
if c % 2 == 0:
        print("this number is EVEN!")
else:
    print("this number is ODD!") 
if d % 2 == 0:
        print("this number is EVEN!")
else:
    print("this number is ODD!") 
    X=a+b+c+d
    print("the sum X is :", X)
    Y=a*b*c*d
    print("the multiplication Y is :", Y)
if a % 2 & b % 2 == 0:
      T=a/b
      print("the quotient T is :", T)
else:
      if a % 2 == 0:
          print("this number is EVEN!")
      else:
              print("this number is ODD!")
      if b % 2 == 0:
            print("this number is EVEN!")
      else:
            print("this number is ODD! //n ")
            print("INCOMPATIBLE!!!")

