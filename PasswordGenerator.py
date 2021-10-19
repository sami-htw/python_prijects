# This Program should generate random passwords, that consist of:
# - capital and small Letters A to Z and a to z.
# - different Digits from 0 to 9.
# -Punctuation characters( . or ,).


import random
import string

part1 = list(string.ascii_lowercase)
part2 = list(string.ascii_uppercase)
part3 = list(string.digits)
part4 = list(string.punctuation)


char_Numbers = input("select The Number of Password digits: ")

while True:
    try:
        char_Numbers = int(char_Numbers)
        if char_Numbers < 8:
            print("Each Password should conatin at least 8 characters")
            char_Numbers = input("Enter a valid Number,please: ")
        else:
            break

    except:
        print('Enter only Numbers, please, another characters are invalid')

        char_Numbers = input(
            "Select the Number of Characters of your Password: ")


random.shuffle(part1)
random.shuffle(part2)
random.shuffle(part3)
random.shuffle(part4)

# 30% for small letters and also 30% for capitel letters
first_Segment = round(char_Numbers * (30/100))
# 20% for digits and  20% for punctuation
second_Segment = round(char_Numbers * (20/100))

password = []

for i in range(first_Segment):
    password.append(part1[i])
    password.append(part2[i])

for j in range(second_Segment):
    password.append(part3[j])
    password.append(part4[j])


random.shuffle(password[0:])

password = "".join(password)

print(password)
