# Navaneeth Krishna Anilkumar
# NSID: nka629
# Student number: 11306665
# DR. Mark Keil

# importing random module and creating random int with randint()
import random
random_number = random.randint(-100,100)

print("The random integer generated is :", random_number)

# determining if the random integer is positive, negative or 0.
if random_number > 0:
    neg_pos_zero = "positive"
elif random_number < 0:
    neg_pos_zero = "negetive"
else:
    neg_pos_zero = "zero"

print("The random number",random_number, "is", neg_pos_zero,"!")