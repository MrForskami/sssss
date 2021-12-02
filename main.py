import time
from turtle import *
from random import randint

qwe = 60 #int(input())
qwerty = 60 #int(input())

print("loding...")
time.sleep(2)

circle(qwe, -qwerty)
circle(qwe, 2*qwerty)

penup()
circle(60, 60)
pendown()
circle(12, 360)
penup()
circle(60, 120)
pendown()
circle(12, 360)