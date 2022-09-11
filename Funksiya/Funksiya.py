# import math

# def ekranga_chiqar(a):
#     print(a)

# ekranga_chiqar("Hello world")


# def summa(a,b):
#     print(a+b)

# summa(2,7)

# def summa(a: int,b: int)->int:
#     print(a+b)

# print(type(summa))

# def summa(a: int,b: int)->int:
#     return a+b

# print(summa(a=2,b=3))


# def user(ism,yoshi=22):
#     return f"ismi: {ism} , yoshi: {yoshi}"

# print(user("Sanjarbek",23))

# a=int(22)

# b=int(3)

# def summa():
#     global a
#     a = 2
#     b = 3
#     return a+b
# print(summa())

# print(a,b)

# def summa(var1,var2,*args):
#     print(var1,var2,end="\n")
#     return var1+var2+sum(args)

# print(summa(2,3,4,5)) # parametr nomi yozilmaydi

# def MIN(a,b):
#     min=a
#     if a>b:
#         min=b
#     else:
#         min=a

#     return min

# def MAX(a,b):
#     max=a
#     if a<b:
#         max=b
#     else:
#         max=a

#     return max

# print(MAX(2,4))

# def genarator(a):
#     for i in range(1,a+1):
#         yield i

# for x in genarator(10):
#     print(x)

# def func(var):
    
#     try:
#         kvadrat=math.pow(2,var)
#         return kvadrat
#     except:
#         raise "Argument int  yoki float turida bo'lishi kerak"

# print(func(2))

# func=lambda x: x+2

# print(func(2))

# def daraja(x):
#     return lambda n: n**x

# kv=daraja(2)

# kub=daraja(3)

# print(f"3 kvadrati: {kv(3)}\n3ni kubi : {kub(3)}")

# sonlar=[i for i in range(1,11)]

# def juft(a: int)->bool:
#     return a%2==0

# juft_sonlar=list(filter(lambda x: x%2==0,sonlar))

# print(juft_sonlar)


def func(a,b,c,*args):
    result=[]
    result.append(a)
    result.append(b)
    result.append(c)
    for i in args:
        result.append(i)

    return result

print(func(2,3,4,7,8,2,8,1))