# Navaneeth Krishna Anilkumar
# NSID: nka629
# Student number: 11306665
# DR. Mark Keil

string_encoded = input("Please input the encoded string :")
index = int(input("Please input the location of the number in the encoded string :"))
K = int(string_encoded[index-1])

slice1 = K * string_encoded[:index-1]
slice2 = string_encoded[index:]
decoded_without_reverse = slice1+slice2
decoded = decoded_without_reverse[::-1]

if len(decoded)%2 ==0:
    key = decoded[int(len(decoded)/2)]
else:
    key = decoded[int(len(decoded)/2 + 0.5-1)]

print("The decoded string is :", decoded)
print("The key character of the decoded string is :", key)
