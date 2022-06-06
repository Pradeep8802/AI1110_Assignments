from math import *
n=int(input("Number of voter: "))
x=float(input("Enter value of mean: "))
z=float(input("enter z_u: "))
a=float(100*z*sqrt(x*(1-x)/n))
a=round(a,2)
print(f"Margin error is {a}%")
m=input("Enter margin error:")
w=2/(100*sqrt(x*(1-x)/n))
w=round(w,3)

if(w==1.225):
    u=0.89
    print("The cofidence coefficient is:",2*u-1)
