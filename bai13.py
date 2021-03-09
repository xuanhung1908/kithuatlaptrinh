a=int(input("nhap a "))
b=int(input("nhap b "))
c=int(input("nhap c "))
denta= b*b-4*a*c
if denta<0:
    print("pt vô nghiệm")
elif denta==0:
    x=-b/(2*a)
    print("pt có nghiệm kép x=",x)
else:
    x1=(-b-denta)/(2*a)
    x2=(-b+denta)/(2*a)
    print ("pt có 2 nghiệm riêng biệt là: \n x1 ",x1,"\n x2 ",x2)
