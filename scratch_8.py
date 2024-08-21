summation = 0
averageness = 0
oldman = 0
manname = ""
totmulher20 = 0
from time import sleep
for person in range(1,5):
    print("-----{}° PERSON-----".format(person))
    name = str(input("Name: "))
    age = int(input("Age: "))
    sex = str(input("Sex [M/F]: "))
    somaidade = age + somaidade
    if person == 1 and sex in "Mm":
        oldman = age
        homname = name
    if sex in "Mm" and age > oldman:
        oldman = age
        homname = name
    if sex in "Ff" and age < 20:
        totmulher20 = totmulher20 + 1
mediaity = summation / 4
print("The average age of the group is {} years.".format(averageness))
print("The older man has {} and is called {}". format(oldman, manname))
print("In total there are {} women under 20 years old".format(totmulher20))