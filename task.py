#
import time
pre_Y=int(time.strftime("%Y"))
bir_Y=int(input("Enter your birth year: "))
age=pre_Y-bir_Y
print("your age is",age)
print("total days is",age*365)

#
import time
day=int(input("Enter your date: "))
month=int(input("Enter your month: "))
year=int(input("Enter your year: "))
print(f"previous date in dd/mm/yr is {day-1}/{month-1}/{year-1}")

#
import random
for i in range(0,4):
    print(random.randrange(1,50),end=" ")