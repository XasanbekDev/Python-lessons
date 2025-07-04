# # # float(input(iltimos, bir son kiriting:"))
# # # kv=son**2
# # # kb=son**3
# # # print(f"{son}ning kvadirati:{kv}")
# # # print(f"{son}ning kb{kubi}")






# cars=['toyota', 'bmw', 'mercedes', 'audi', 'chevrolet', 'kia']
# cars.sort()
# print(cars)


# n = int(input("n sonini kiriting: "))
# juft = list(range(0,n,2))
# toq = list(range(1,n,2))
# print(juft)
# print(toq)


# n=int(input("n sonini kiriting"))
# juft = list(range(0,n,2))
# print(juft)



# # n= int (input("n soni kiriting: "))
# # fruits=('olma', 'anor', 'banan', 'uzum', 'shaftoli')
# # fruits=('olma', 'gilos', 'banan', 'uzum', 'shaftoli')
# # tuple=list (range(olman,saftol))






# # Foydalanuvchidan ro‘yxatdagi sonlarni kiritishni so‘rang. Kiritilgan ro‘yxatdan faqat musbat sonlarni ajratib olib, 
# yangi ro‘yxatda saqlang va ekranga chiqaring.
# # )









# # # = int (input("n soni kiriting: "))
# # #  juft = list(range(0,n,2))
# # # toq = list(range(1,n,2))
# # # print(juft)
# # # print(toq)








# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>=18: 
#  print('Xush kelibsiz!')
# else: 
#  print ('Kirish mumkin emas!')









# login = "input"("Yangi parol qo'ying:")
# if "len"("parol")<=4: # parol uzunligini tekshiramiz

#  "print"("Login 4 harfdan ko'proq bo'lishi shart!")
# else:
#  print =(" xato qaytadan urining !")

















# login = input("Yangi login tanlang:")
# if len(login)<=5: # login uzunligini tekshir
#    print (" # login 5 harifdan ko'proq bolishi shart!")

# else:
#    print ("buni sayitka qo'yildi.")










# Kichik: a<b
# Kichik yoki teng: a<=b
# Katta: a>b
# Katta yoki teng: a>=b #masala







# login = input("bitta son kiriting:")
# if len(login)<=5: # login uzunligini tekshir      
      
#  print( "10 dan katta yoki 5 dan kichik")







# menu = ['osh','kozonkabob', 'shashlik', 'somsa'] 
# buyurtma =[]
# ovqat = "manti" if ovqat in "menu" 
# print("Buyurtma qabul qilindi.") 
# else: 

# print("Afsuski bizda bunday ovqat yo'q")







# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#   print('Sizga kirish bepul.')
# elif yosh<=12:
#   print('Sizga kirish 5000 so\'m')
# else:
#   print('Sizga kirish 10000 so\'m')









# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#   print("Cho'milgani ketdik!")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#   print("Uyda dam olamiz!")

# else:
#   print("bugun ish kuni")








# #2-dars
# Haftakuni= int(input("hafta kuni kiriting(1-7)"))
# if 1 <= Haftakuni  <=5:
#   print("sizning  ish kuni!")
# elif 6 <= Haftakuni <=7:
#   print ("sizning dam olish kuningiz!")
# else:
#   print("bunaqa kun yo'q!")






# 3-dars

# a = int(input("a sonni kiriting: "))
# b = int(input("b sonni kiriting: "))

# if a > b:
#     print("a son katta")
# elif a<b:
#     print("b son katta")
# else:
#     print("sonlar teng")





# # 4-dars
# fasllar= int(input("fasilarni (1-12)"))
# if 3 <= Fasl  <= 5:
#   print(" bu bahor fasli!")
# elif 6 <= fasl <=8:
#   print ("bu yoz fasli!")
# elif  9 <= fasl <= 11:
#   print("bu kuz fasli!")
# elif 12  or 1 and 2:
#   print("bu fasl qish !")
# else:
#   print("bu hato ! ")

    




# x = int(input("Son kiriting: "))

# if x > 0:
#     print("+ sonlar")
# elif x < 0:
#     print("- sonlar")
# else:                                                                                                                                                                                                                                                                                                                               
#     print("0 son")








# Bosh lugat yarating: kitoblar = {}
# Unga quyidagi elementlarni qoshing:
# "Python" → "Guido van Rossum"
# "Java" → "James Gosling"
# "C++" → "Bjarne Stroustrup"
# Lug'atni ekranga chiqarib, natijani tekshiring.
















# { 'ali':['python','c++'],
# 'vali':['html','css','js'],
# 'hasan':['php','sql'], 
# 'husan':['python','php'],
# 'maryam':['c++','c#']}
# for ism, tillar in "dasturchilar"".items(): print(f" \
# { "ism".title()} (" quyidagi dasturlash tillarini biladi:")\
# for  til in tillar: 
#  "print" ( "til".upper())

























# 🧠 Masala: Talabalar bahosiga qarab baholash
# Vazifa:

# Talabalar ro‘yxatini baholari bilan yarat.

# Har bir talabani tekshirib chiq:

# Agar bahosi 90 va undan yuqori bo‘lsa: "A'lo"

# Agar bahosi 75 dan yuqori va 90 dan kam bo‘lsa: "Yaxshi"

# Agar bahosi 60 dan yuqori va 75 dan kam bo‘lsa: "Qoniqarli"

# Aks holda: "Qoniqarsiz"

# Natijani quyidagicha chiqar:

# "Ali: 91 → A'lo"

# "Laylo: 78 → Yaxshi"

# 🔄 Ishlash ketma-ketligi:
# Talabalar ro‘yxatini tayyorlash (dict formatda: ism → ball).

# for yordamida har bir talabaning ismini va bahosini olish.

# if/elif/else orqali shartlarni tekshirish.

# Har bir talaba uchun natijani print qilish.









# talabalar= ["samandar, kamron,hasan,muhmud"(90-)]
# x=(bal )









# talabalar= int(input("ballar (60-)"))
# if 3 <= Fasl  <= 5:
#   print(" bu bahor fasli!")
# elif 6 <= fasl <=8:
#   print ("bu yoz fasli!")
# elif  9 <= fasl <= 11:
#   print("bu kuz fasli!")
# elif 12  or 1 and 2:
#   print("bu fasl qish !")
# else:
#   print("bu hato ! ")

    



# talabalar= ["samandar", "kamron"]
# n = 1
# for i in talabalar:
#     n = n + 1

















# n = int(input("Nechta talaba bahosini kiritmoqchisiz? "))
# talabalar = []

# for i in range(n):
#     ism = input(f"{i+1}-talabaning ismini kiriting: ")
#     ball = int(input(f"{ism}ning bahosini kiriting (0-100): "))
#     talabalar.append((ism, ball))

# print("\nBaholash natijalari:")


# for ism, ball in talabalar:
#     if 90 <= ball <= 100:
#         baho = "A'lo (5)"
#     elif 75 <= ball < 90:
#         baho = "Yaxshi (4)"
#     elif 60 <= ball < 75:
#         baho = "Qoniqarli (3)"
#     elif 0 <= ball < 60:
#         baho = "Qoniqarsiz (2)"
#     else:
#         baho = "❌ Xato: noto‘g‘ri ball"
    
#     print(f"{ism}: {ball} → {baho}")










# Hurmatli Husan,
# Siz 2025-05-08 sanasida topshirgan imtihondan B baho oldingiz.
# Tabriklaymiz!









# 🎯 Vazifa:
# Foydalanuvchidan quyidagilarni kiriting:

# Ismi

# Balli

# Imtihon sanasi (masalan, 2025-05-08)

# Ballga qarab A, B, C, D, F baho chiqaring.

# Agar ball noto‘g‘ri bo‘lsa (masalan, -5 yoki 150), quyidagi xabarni chiqaring:
# Xatolik: ball 0 dan 100 gacha bo'lishi kerak

# Natijani quyidagicha chiqarilsin:






# from builtins import print


# n= "int"("input"("Nechta o'quvchi bahosini kiritmoqchisiz? "))
# Foydalanuvchi=[] 
# for i in "range"(n):
#   ism = "input"(f"{i+1}-foydalanuvchi ismini kiriting: ")
# ball = "int"("input"(f"{ism}ning bahosini kiriting (0-100): "))
# "talabalar.append"((ism, ball,))

# print("\nBaholash natijalari:")

# for ism, ball in "talabalar":
#     if 90 <= ball <= 100:
#         baho = "A'lo (A)"
#     elif 75 <= ball < 90:
#         baho = "Yaxshi (B)"
#     elif 60 <= ball < 75:
#         baho = "Qoniqarli C)"
#     elif 0 <= ball < 60:
#         baho = "Qoniqarsiz (D)"
# else:
#          baho = "❌ Xato: noto'g'ri ball"
# print(f"{ism}: {ball} → {baho}")





                # Foydalanuvchidan ma'lumotlarni olish
# ism = input("Ismingizni kiriting: ")
# sana = input("Imtihon sanasini kiriting (YYYY-MM-DD): ")
# ball_kiritildi = input("Ballingizni kiriting (0-100): ")

# Ball raqam ekanligini tekshirish
# if ball_kiritildi.isdigit():
#     ball = int(ball_kiritildi)

#     if 0 <= ball <= 100:
#         if ball >= 90:
#             baho = "A"
#         elif ball >= 80:
#             baho = "B"
#         elif ball >= 70:
#             baho = "C"
#         elif ball >= 60:
#             baho = "D"
#         else:
#             baho = "F"

#         print(f"\nHurmatli {ism},")
#         print(f"Siz {sana} sanasida topshirgan imtihondan {baho} baho oldingiz.")
#         print("Tabriklaymiz!")
#     else:
#         print("Xatolik: ball 0 dan 100 gacha bo'lishi kerak.")
# else:
#     print("Xatolik: Ball raqam bo'lishi kerak.")















# Foydalanuvchi avtomobilida muammo borligini aytadi. Tizim esa unga turli savollar beradi (yurganda g‘alati tovush chiqyaptimi, dvigatel ishga tushyaptimi, faralar ishlayaptimi va h.k.), shunga qarab muammo taxmini chiqariladi.

# ✅ Ishlash ketma-ketligi (algoritm):
# Foydalanuvchidan bir nechta "ha"/"yo'q" (yoki "1"/"0") ko'rinishidagi savollarni qabul qilamiz:

# Dvigatel umuman ishlamayaptimi?

# Starter tovushi chiqadimi?

# Akkumulyator lampasi yonayaptimi?

# Faralar ishlayaptimi?

# Tovushlar yoki g‘alati hidlar bormi?

# if-elif-else orqali holatlarga qarab xulosa chiqaramiz.

# Har_bir_holatga_aniq_tashxisyozamiz.






# def aftomobil_tashhisi ():
#  "print"("iltimos savolarimizga ha/ yo'q  deb javob bering.")

# dvigatel_ishlamaydi = "input"("Dvigatel umuman ishlamayaptimi? ").lower()
# starter_tovushi = "input"("Starter tovushi chiqadimi? ").lower()
# akkumulyator_lampasi = "input"("Akkumulyator lampasi yonayaptimi? ").lower()
# faralar_ishlaydi = "input"("Faralar ishlayaptimi? ").lower()
# galati_tovush_yoki_hid = "input"("Tovushlar yoki g'alati hidlar bormi? ").lower()


# if dvigatel_ishlamaydi=="ha yoki yo'q":
#  if starter_tovushi=="yo'q yoki ha ":
#   if faralar_ishlaydi=="yo'q yoki ha":
#    "pirint"("tashhis: akkumlyator bo'sh yoki butinla")
# elif starter_tovushi == "ha":
#   "print"(" Tashxis: Yonilg'i tizimida yoki dvigatelning boshqa ichki qismlarida muammo bo'lishi mumkin.")
# elif galati_tovush_yoki_hid == "ha":
#  "print"(" Tashxis: Ehtimol, kamarlar, tormozlar yoki simlarda nosozlik bor. Tekshiruv zarur.")
# elif akkumulyator_lampasi == "ha" and faralar_ishlaydi == "yo'q":
#    " print"(" Tashxis: Akkumulyator zaryadi past yoki generator ishlamayapti.")
# else:
#   "print"(" Tashxis: Dastlabki tekshiruvda jiddiy muammo aniqlanmadi. Batafsil diagnostika tavsiya qilinadi.")









# aftomabil_tashxisi "int"(input("moshinada nima hatolik bor."))




# kun = input("Kun (hafta kuni): ").lower()
# yomgir = input("Yomg'ir yog'yaptimi? (ha/yo'q): ").lower()
# soat = int(input("Soat nechi bo'ldi? (24 soat formatida): "))

# # Shartlarni tekshirish va natijani chiqarish
# if kun == "yakshanba" and yomgir == "yo'q" and soat < 9:
#     print("Tezroq avtobusga chiq, sayr qilamiz!")
# elif kun == "yakshanba" and yomgir == "ha":
#     print("Bugun uydan chiqma, yomg'ir yog'yapti.")
# else:
#     print("Bugun avtobus yo'q, ish qilamiz!")














































