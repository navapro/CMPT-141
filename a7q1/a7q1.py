# Navaneeth Krishna Anilkumar
# NSID: nka629
# Student number: 11306665
# DR. Mark Keil

import numpy as np


test1 = [
    [0, 0],
    [0, 1],
    [0, 1]
]
test2 = [
    [1, 1, 1, 1],
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 1]
]

quizResults = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
]

quizResultsArray = np.array(test2)

print("Poorly done questions:")

for i in range(quizResultsArray[0].size):
    temp = quizResultsArray[:,i:i+1]
    avg = 0

    for j in temp:
        avg += j[0]
    avg = (avg/temp.size) * 100
    if avg < 60:
        print("Only",round(avg,2),"percent of students solved question", i+1)

