"""
myList = ["olma", "banan", "taroq", "paypoq"]
yourList = [1 , 8 , 15 , -9]
print(myList)
print(yourList)
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non"]
yourList = [1 , 8 , 15 , -9]
n = len(myList) # myListda nechta element borligini xisoblaydi
print(n)
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non"]
print(type(myList))
"""
"""
myList = ["olma", 15, 4.5, False]
print(myList)
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non"]
print(myList[2])
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non"]
print(myList[-2])
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
print(myList[2:6])
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
print(myList[2:])
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
print(myList[:5])
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
if "qolqop" in myList:
    print("YES")
else :
    print("NO")
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
myList[4] = "pamidor"
print(myList)
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
myList[3:6] = ["sardor" , "aziz", "maftuna"]
print(myList)
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
myList[3:6] = ["sardor" , "aziz", "maftuna", "laziz", "salima"]
print(myList)
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
myList.insert(2, "apelsin")
print(myList)
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
myList.append("xayr")
print(myList)
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
myList.remove("taroq")
print(myList)
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
myList.pop(3)
print(myList)
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
myList.pop()
print(myList)
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
del myList[5]
print(myList)
"""
"""
myList = ["olma", "banan", "taroq", "paypoq", "non", "atirgul", "sharf", "salom"]
myList.clear()
print(myList)
"""

"""
myList = [5, 6, 8, 7, 12, 85, 1, -5, 8, 75]
myList.sort()
print(myList)
"""
"""
myList = [5, 6, 8, 7, 12, 85, 1, -5, 8, 75]
myList.sort(reverse = True)
print(myList)
"""