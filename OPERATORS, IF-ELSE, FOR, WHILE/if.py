"""
+
-
*
/
=
a % b  a ni b ga bo'lgandagi qoldiqbi topadi
a**b   a ning b inchi darajasi
a//b   a ni b ga bo'lgandagi butun qism
"""

"""
a = 10
b = 6
c = a % b  # qoldiqli bo'lish
print( c )
"""
"""
a = 10
b = 6
c = a ** b # a ning b inchi darajasi
print( c )
"""
"""
a = 10
b = 6
c = a // b # a ni b ga butun bo'lish
print( c )
"""
"""
a = 5
a += 3 # a ning qiymatiga 3 ni qo'shadi
print(a)

# a X= b X ning o'rnida qanday amal turgan bo'lsa a = a X b ifodasi bajariladi
a -= 3
a *= 3
a /= 3
a %= 3
a **= 3
a //= 3
 """
"""
 >  
 <
 ==  teng 
 >=
 <=
 !=  teng emas
 """
"""
a = 0
if a > 0:
    print("musbat")
elif a < 0:
    print("manfiy")
else :
    print("nol")
"""
"""
a = 10
b = 10
if a == b:  # a soni b soniga tengmiiiii
    print("TENG")
else :
    print("TENG EMAS")
"""
"""
a = 10
b = 20
if a != b:  # a soni b soniga teng emasmiiiii
    print("ha")
else :
    print("yoq")
"""
"""
# son 10 dan katta yoki teng va 99 dan kichik yoki teng bo'lsa ikki xonali son xisoblanadi
a = 154
if a >= 10 and a <= 99:
    print("ikki xonali")
else :
    print("unamas")
"""
"""
a = 155
# sonning oxirgi xonasi a%10 qilib topiladi!!!
if a % 10 == 5 or a % 10 == 0:
    print("5 ga bo'linadi")
else :
    print("unamas")
"""