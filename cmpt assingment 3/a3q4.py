# Navaneeth Krishna Anilkumar
# NSID: nka629
# Student number: 11306665
# DR. Mark Keil

import string
import random

input_name = input("Please input a student’s first name :")
first_name = input_name[0].upper() + input_name[1:]

print(first_name)

pick = random.choice(string.ascii_uppercase)
print("A student with the following first initial will be in the Background Research group :",pick)

if first_name[0] == pick:
    print(first_name,"is in background research group !")
elif "A" <= first_name[0] <= "D":
    print(first_name,"is in task group one !")
elif "E" <= first_name[0] <= "I":
    print(first_name,"is in task group two!")
elif "J" <= first_name[0] <= "R":
    print(first_name,"is in task group three !")
else:
    print(first_name, "is in task group four !")