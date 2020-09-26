

b=1.6
print(b)
print(type(b))

from decimal import*
getcontext().prec=30
print(Decimal(10)/Decimal(3))
#Fraction là số hữu tỷ
from fractions import*
frac = Fraction(6,9)
print(frac)
print(type(frac)) 
#complex là số phức
c=complex(6,8)
print(c.real)
print(c.imag)

#thư viện math 
import math 
#lấy số nguyên
d=math.trunc(6.5) 
print(d)
#làm tròn nhỏ hơn
e=math.floor(6.54)
print(e)
#làm tròn lớn
k=math.ceil(6.551)
print(k)
#giá trị tuyệt đối
q=math.fabs(-5.51)
print(q)
#căn bậc 2
i=math.sqrt(5)
print(i)
#ước chung lớn nhất
j=math.gcd(12,32)
print(j)
#chia lấy số nguyên thôi
v=6//5
print(v)
#
