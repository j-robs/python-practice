import time
import datetime

prompt = "Enter your name: "
prompt2 = "Enter your age: "

name = raw_input(prompt)
age = raw_input(prompt2)
thisyear = datetime.datetime.today().strftime('%Y')

year = (100 - int(age)) + int(thisyear)

print name + " will turn 100 in the year " + str(year) + "!"