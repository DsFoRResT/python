# a="dastur"
# print(a)

# a="assalomu"
# b="alaykum"
# c=a+" "+b
# print(c)

# #1 xil yozuvni bir necha marotaba chiqarish
# a="space "
# print(a*8)

# gap="bugun string toifasi bilan shug`ullaniyapmiz"
# print(len(gap))

# s="inqilobchilar"
# print(s[9:1:-1])

# s="s\np\ta\nbbbbbbbbbbbbbbb\ta"
# print(s)

# #parametrlarsiz ishga tushishi
# s=r'"C:\temp\new"'
# print((s))

# yozgan string malumotimiz faqat sonlardan ibotligini tekshiradi 
# s="12345"
# print(s.isdigit())

# berilgan string ma'lumot faqat katta va kichik harflardan iboratligini tekshiradi
# s="smkKdvmvmmv"
# print(s.isalpha())

#berilgan string ma'lumotda raqam qatnashganligini tekshiradi
# s="bgbgLbg8"
# print(s.isalnum())

#faqatgina katta harflardagina yolg'on qiymat qabul qiladi
# s="g7l"
# print(s.islower())

# probeldan keyingi harf kattami yoki yoqmi aniqlaydi hamda son qatnashmasligi kerak
# s="Sfghghdog Ajdigjdxxco fzfsfsfs"
# print(s.istitle())

# s="yozuvlar gaplar"
# print(s.startswith("zuv",2,6))

# s="hdfggyrtyerg yer"
# print(s.endswith("er",9,11))

#har bir string ma'lumotdan keyin salom so'zini qo'shadi
# s="salom"
# print(s.join([' fff ',' hhh ',' ttt ', ' ggg']))


# print(ord("a"))
# print(chr(65))

# #satr boshi
# s="dffgfgfjg gufggu gugu"
# print(s.capitalize())

# #har bir so'zning 1-harfini bosh harf bn boshlaydi
# a="assalomu aleykum"
# print(a.title())

# #matn boshidagi bo'shliqni olib tashlaydi
# meva="      olmalar"
# print(meva.lstrip())

# #matn oxiridagi bo'shliqni olib tashlaydi
# meva="olma     "
# print(meva.rstrip())

# #matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
# meva="      olma        "
# print(meva.strip())

# #matnning har bir harfini bosh harf qilish
ism_familya="asqar axtamov"
print(ism_familya.upper())

# #har bir harfni kichik harf qilish
# ism_familya="ASQAR AXTAMOV"
# print(ism_familya.lower())