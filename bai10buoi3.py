def tinh(R):
    import math
    if R>=0:
        s=math.pi*R*R
        v=2*math.pi*R
        print(s,v)
    else:
        print(" ban kinh k hop le")
R=int(input("nhap R: "))
tinh(R)
        

