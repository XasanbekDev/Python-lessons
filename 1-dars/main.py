# mehmonlar=['Ali','Vali','Hasan','Husan','Olim',] 
# for mehmon in mehmonlar:
#      print( f"Hurmatli {mehmon},sizni 20  dekabr kuni nahorga  oshga taklif qilamiz")
#      print("Hurmat bilan, palonchiyevlar oilasi") 






# sonlar = list(range(1,11)) 
# for son in sonlar: print(f"{son} ning kvadrati {son**2} ga teng")










# narh = 0 # mijoz 15 so'mga ovqat oldi
# choy = True
# somsa = False
# lagmon= True
# shashlik = True
# osh = False

# if choy: 
#    print("Mijoz choy oldi.")
# narh = narh + 3000
# if somsa: 
#    print("Mijoz somsa oldi.")
# narh = narh + 5000
# if lagmon: 
#   print("Mijoz lagmon oldi.")
# narh = narh + 25000
# if shashlik: 
#   print("Mijoz shashlik oldi.")
# narh = narh + 15000
# if osh: 
#   print("Mijoz osh oldi.")
# narh = narh + 20000

# print(f"Jami {narh} so'm")













# from turtle import *
# import colorsys
# import math

# bgcolor("black")
# speed(0)
# hideturtle()

# n = 180
# h = 0

# for i in range(n):
#     color(colorsys.hsv_to_rgb(h, 1, 1))
#     circle(100 - i, 60)
#     left(120)
#     circle(100 - i, 60)
#     left(120)
#     h += 1/n
#     left(5)

# done()











#kamalakli
from turtle import*

bgcolor("black")
speed(0)
for i in range(200):
    color("red")
    circle(i*0.6)
    color("cyan")
    circle(i*0.4)
    right(4)
    forward(3)
done()












# from turtle import *
# import colorsys

# bgcolor("black")
# speed(0)
# hue = 0

# for i in range(150):
#     color(colorsys.hsv_to_rgb(hue, 1, 1))
#     begin_fill()
#     circle(i, 60)
#     left(120)
#     circle(i, 60)
#     left(120)
#     circle(i, 60)
#     end_fill()
#     hue += 0.005
#     left(5)

# done()








# from turtle import *

# # bgcolor("black")
# # color("yellow")
# # speed(0)

# # for i in range(100):
# #     for j in range(5):
# #         forward(i * 2)
# #         right(144)
# #     right(10)

# # done()







# from turtle import *
# import colorsys

# bgcolor("black")
# speed(0)
# pensize(2)
# hue = 0

# for i in range(250):
#     color(colorsys.hsv_to_rgb(hue, 1, 1))
#     forward(i)
#     right(59)
#     hue += 0.004

# done()






# from turtle import *

# bgcolor("black")
# speed(0)
# colors = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta"]

# for i in range(360):
#     color(colors[i % len(colors)])
#     forward(i * 3 / 10 + i)
#     left(59)
#     circle(i * 0.1, 60)

# done()