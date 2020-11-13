# Navaneeth Krishna Anilkumar
# NSID: nka629
# Student number: 11306665
# DR. Mark Keil

import numpy as np

f = open("election_SK_2016.csv","r")
ls = []

for line in f:
    temp = line.rstrip()
    ls.append(temp.split(","))

header = ls[0].copy()
del ls[0]

constituency = []
vote_tallies = []

for i in ls:
    constituency.append(i[0])
    vote_tallies.append(i[1:])

constituency = np.array(constituency)
vote_tallies = np.array(vote_tallies)
vote_tallies = vote_tallies.astype(np.int64)


total_votes = vote_tallies[:,0]

for i in range(1,vote_tallies[0].size):
    total_votes += vote_tallies[:,i]


total_votes = np.array(total_votes)

sk_pary_index = header.index("saskparty") -1


logic = vote_tallies[:,sk_pary_index] > total_votes/2
sk_pary_won = constituency[logic]
print("The Saskatchewan Party won a vote majority in",sk_pary_won.size,"constituencies.")
print(sk_pary_won)