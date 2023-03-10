import math
print(" Nhap hai canh ke của mot tam giac vuong: ")
r1=int(input())
r2=int(input())
c=r1*r1+r2*r2
print('Canh ke thu nhat la: ',r1,', canh ke thu hai: ',r2,', co canh huyen = ',round(math.sqrt(c),2),sep='')