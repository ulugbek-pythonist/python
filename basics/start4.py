# 5-7 min

# user input


# ism = input("Ismingiz: ")

# print(type(ism))

# print("Assalomu alaykum, " + ism)

import datetime


son = input("Son kiriting: ")
son = int(son)
print(son * 2)
# "dev" + "eloper" = "developer"
# 3 + 4 = 7  
# "3" + "40" = "340"
# "3"+"3"

# Foydalanuvchidan yoshini kiritishini so'rang 
# va qachon tug'ilganini aytib bering

yosh = input("Yoshingizni kiriting: ")

yosh = int(yosh)
yil = datetime.date.today().year
print(f"{yil - yosh} - yil")
