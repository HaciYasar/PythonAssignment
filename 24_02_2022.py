# -*- coding: utf-8 -*-
"""24.02.2022.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SUNmLajqesgbTPm5HyOW7ZJHqbuGWGoW
"""

# if else koşul komutları: ifin elsi aynı hizzada olur. Else false veya falsy ise else çalışır.

num = int(input("Enter a number :"))
if num % 2 == 0 :
    print("{} is even".format(num))
else :
    print("{} is odd".format(num))

sayı = int(input("Bir sayı girin :"))
if sayı > 0 :
    print("Bu sayı pozitiftir.")
else :
    print("Bu sayı negatiftir.")

num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))

if num1 > num2 :
    larger = num1

else :
    larger = num2
print("The larger number is ", larger)

bool_value = True

if bool_value :
    print("Yes")
else :
    print("No")

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter the third number :"))

if (num1 >= num2) and (num1 >= num3) :
    largest = num1
elif (num2 >= num1) and (num2 >= num3) :
    largest = num2
else :
    largest = num3
print("The largest number is ", largest)

num = float(input("Enter anumber : "))

if num > 0 :
  print("Pozitive number.")
elif num == 0 :
  print("Zero.")
else :
  print("Negatif number.")

# İç içe geçmiş koşullar

score = int(input('Enter your score :'))

if score >=90:
	if score >=95:
		Score_letter='A+'
	else:
		Score_letter='A'
elif score >=80:
	if score >=85:
		Score_letter = 'B+'
	else:
		Score_letter = 'B'
else:
	Score_letter = 'below B'
print('Your degree: %s' % Score_letter)

left =set("qwertasdfgzxcvb")
left

right =set("yuıophjklnm")
right

word ="clarusway"
word

word = set(word)
word

leftcheck = bool(word.intersection(left))
rightchech = bool(word.intersection(right))

leftcheck

rightchech

sonuç = leftcheck and rightchech
sonuç # Sağ el ve sol el klaevye harfleri kesişim nolktaları.

# Lops

while 0 :
  print("sıfır")

condition = 5

while condition :
  condition -=1
  print(condition)

condition = 5
while True :
  condition -=1
  print(condition)
    if condition == 0 :
      break

