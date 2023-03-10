a=int(input("Nhap so a: "))
b=float(input("Nhap so b: "))
c=float(input("Nhap so c: "))
min=max=a
if b>max:
    max=b
if c>max:
    max=c
if b<min:
    min=b
if c<min:
    min=c
print("SLN=",max)
print("SBN=",min)