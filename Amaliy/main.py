



# """
# Masala: 1 dan n gacha bo'lgan sonlar yig'indisini hisoblang.
# Kiritish: n = 10
# Natija: 1 + 2 + ... + 10 = 55

# # """
# n = int(input("1 dan n gacha bo'lgan sonlar yig'indisini hisoblang. "))
# k = 0
# for i in range(1,n+1):
#     k = i + k

# print(k)

# """"""

# Masala: 1 dan n gacha bo‘lgan tub sonlarni ekranga chiqaring.
# Kiritish: n = 20
# Natija: 2 3 5 7 9 11 13 15 17 19


# """"""






# n= int(input(" 1 dan n gacha bo'lgan tub sonlarni ekranga chiqaring."))
# k = 0

# for i in range(3,n+1):
#     k=i+ k 
#     print(k)
# if ("n=20"):
# #     print("")
# # else:
#   print("xatolik ")

# Foydalanuvchidan hafta kunini qabul qilishni so'rang agar foydalanuvchi shanba va yakshanba kirisa havo haroratini 
# so'rang agar harorat 35 dan yuqori bo'lsa cho'milgani ketdik agar past bo'lsa uyda dam olamiz degan
# matin chiqsin agar foydalanuvchi shanba yakshanba kundan boshqa kunlarni kiritsa bugun ish kunideb chiqaring!










# kun=input ("bugun nima kun?")
# harorat =float (input("havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba' ) and harorat>=35:
#     print("cho'milgani ketdik!")
# elif(kun.lower()=='shanba' or kun .lower ()=='yakshnba')and harorat<35:
#     print ("uyda dam olamiz!")
# elif (kun .lower ()== 'dushanba' ):

#   print("bugun ish kuni!")
# else:
#    print("siz hato yozdiz?")









# Foydalanuvchidan quyidagi ma'lumotlar olinadi:

# Kun (hafta kuni)

# Yomg‘ir yog‘yaptimi? (ha yoki yo'q)

# Soat nechi bo‘ldi?

# Shartlar:

# Agar yakshanba kuni bo‘lsa va yomg‘ir yog‘mayotgan bo‘lsa va soat 9:00 dan kichik bo‘lsa, "Tezroq avtobusga chiq, sayr qilamiz!" chiqadi.

# Agar yakshanba bo‘lsa, lekin yomg‘ir yog‘ayotgan bo‘lsa, "Bugun uydan chiqma, yomg‘ir yog‘yapti." chiqadi.

# Boshqa kunlarda esa "Bugun avtobus yo'q, ish qilamiz!" deb chiqariladi.










# kun=input("hafta kuni  kiriting ?") 
# if



# l = "admin"
# p = "1234"

# login=input("ism, yoki so'z kiriting:")
# parol= input("harf,yoki son parol qo'ying ")










# if login == l and parol == p:
#     print("salom")
# elif login == l:
#     print("parol xato")
# elif parol == p:
#     print("login xato")
# else:
#     print(" ikkisi ham xato")








# son = float(input("Iltimos, biror son kiriting: "))

# # Kvadratini va kubini hisoblaymiz
# kvadrat = son ** 2
# kub = son ** 3

# # Natijalarni konsolga chiqaramiz
# print(f"{son} ning kvadrati: {kvadrat}")
# print(f"{son} ning kubi: {kub}")








# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))


# yigindi = son1 + son2
# ayirma = son1 - son2
# kopaytma = son1 * son2


# if son2 != 0:
#     bolinma = son1 / son2
#     print(f"{son1} / {son2} = {bolinma}")
# else:
#     print("Bo‘lish mumkin emas: ikkinchi son nol bo‘lishi mumkin emas.")

# print(f"{son1} + {son2} = {yigindi}")
# print(f"{son1} - {son2} = {ayirma}")
# print(f"{son1} * {son2} = {kopaytma}")












# yosh = int(input("Yoshingizni kiriting: "))

# if yosh < 18:
#     qolgan_yil = 18 - yosh
#     print(f"Sizga saytga kirishga {qolgan_yil} yil qoldi.")
# else:
#     print("Xush kelibsiz!")

    













# cars = ['Toyota', 'bmw', 'Mercedes', 'audi', 'Chevrolet', 'Kia']


# sorted_cars = sorted(cars)
# print("Alifbo tartibida (katta-kichik harflar bilan):")
# print(sorted_cars)


# sorted_lower_cars = sorted(cars, key=lambda x: x.lower())
# print("\nBarcha elementlar kichik harflarda tartiblangan:")
# print(sorted_lower_cars)
# Natija:
# python
# Копировать
# Редактировать
# Alifbo tartibida (katta-kichik harflar bilan):
# ['Chevrolet', 'Kia', 'Mercedes', 'Toyota', 'audi', 'bmw']


# ['audi', 'bmw', 'Chevrolet', 'Kia', 'Mercedes', 'Toyota']




# n=int









# car=("'tayota', bmw', ',audi',cherolet',kia")

# sorted_cars=sorted (cars)
# print ("alifbo tartib bo")















# 📌 Masala 1: Ro'yxatdagi musbat sonlarni ajratish

# Masala:
# Foydalanuvchi kiritgan sonlar ro'yxatidan faqat musbat sonlarni ajratib yangi ro'yxat yarating.

# Namuna: 

# Input: [4, -2, 0, 5, -7, 3]
# Output: [4, 5, 3]










# Masala:
# Ro’yxatdagi eng katta va eng kichik sonni aniqlang.

# Namuna:

# Input: [10, 23, 5, 67, 1, 89]
# Output: Eng kichik: 1, Eng katta: 89












# n = int(input("n sonini kiriting: "))
# juft = list(range(0,n,2))
# toq = list(range(1,n,2))
# print(juft)
# print(toq)












# a = int(input("a sonni kiriting: "))
# b = int(input("b sonni kiriting: "))

# if a > b:
#     print("a son katta")
# elif a<b:
#     print("b son katta")
# else:
#     print("sonlar teng")












# sonlar=[4, -2, 0, 5, -7, 3]
# musbat_sonlar=[]
# for son in sonlar:
#     if son>0:
#         musbat_sonlar.append










# input [10, 23, 5, 67, 1, 89]











# n= int(input[10, 23, 5, 67, 1, 89] )
# k = 0

# for i in range(3,n+1):
#     k=i+ k 
#     print(k)
# if ("n=20"):
#      print("")
# else :  
#       print("xatolik ")











# son1=4
# son2=-2
# son3=0
# son4=5
# son5=-7
# son6=3
# print(f"musbat sonlar",son1,son4,son6)











# ages = [10, 23, 5, 67, 1, 89]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))









# sonlar = [4, -2, 0, 5, -7, 3]
# sonlar.sort(reverse=True)
# print(sonlar)









# .sort() metodi ro'yxatni tartiblaydi. Ba'zida asl 
# ro'yxat ichidagi elementlarning ketma-ketligini buzmagan holda 
# ' ro'yxatni tartiblash talab qilinishi mumkin. Buning uchun sorted() 
# funktsiyasidan foydalanamiz:
# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)















# # musbat_sonlar=4,






# # sonlar=[4, -2, 0, 5, -7, 3]
# # sonlar.sort()
# # print(sonlar,"0 dan  keyingi sonlar musbat")


# const scene = new THREE.Scene();
# const camera = new THREE.PerspectiveCamera(
#     75,
#     window.innerWidth / window.innerHeight,
#     0.1,
#     5000
# );

# camera.position.z = 5000;

# const renderer = new THREE WebGLRenderer();
# renderer.setPixelRatio (window.devicePixelRatio >1 ? 2 : 1);
# renderer.setSize(window.innerwidth, window.innerHeight);
# document.body.appendCHild(renderer.domElement);




# const scene = new THREE.Scene();

# const camera = new THREE.PerspectiveCamera(
#     75,
#     window.innerWidth / window.innerHeight,
#     0.1,
#     5000
# );
# camera.position.z = 5000;

# const renderer = new THREE.WebGLRenderer(); // Fixed syntax
# renderer.setPixelRatio(window.devicePixelRatio > 1 ? 2 : 1);
# renderer.setSize(window.innerWidth, window.innerHeight); // Fixed typo (innerwidth → innerWidth)
# document.body.appendChild(renderer.domElement); 



# 'const' 'Scene' = 'new' 'THREE'.Scene();''

# 'const' 'camera' = 'new' 'THREE'.PerspectiveCamera(
#     75,
#     'window'.innerWidth / 'window'.innerHeight,
#     0.1,
#     5000
# );''
# 'camera'.position.z = 5000;''

# 'const' 'renderer' = 'new' 'THREE'.WebGLRenderer(); 
# 'renderer'.setPixelRatio('window.devicePixelRatio > 1 ? 2 : 1');''
# 'renderer'.setSize('window.innerWidth, window.innerHeight');  
# 'document'.body.appendChild('renderer.domElement');''