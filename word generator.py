letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
vowels = ["A", "E", "I", "O", "U"]
consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
import random

minlen = ""
maxlen = ""
nulls = ""
words = ""

while(minlen == "" or maxlen == "" or int(minlen) > int(maxlen) or int(minlen) < 3):
    minlen = input("Minimum word length: ")
    maxlen = input("Maximum word length: ")
    if int(minlen) > int(maxlen):
        print("The minimum word length cannot be greater than the maximum word length.")
    if int(minlen) < 3:
        print("The minimum word length cannot be 2 or less.")

while(nulls == "" or int(nulls) < 1):
    nulls = input("How many word terminators would you like? (The larger the number, the smaller the average word length): ")
    if int(nulls) <= 0:
        print("The number of word terminators cannot be negative or zero.")

while(words == "" or int(words) < 1):
    words = input("How many words would you like to generate? ")

for i in range(int(nulls)):
    letters.append("NULL")

for i in range(int(words)):
    word = ""
    prev = "NULL"
    while(True):
        choice = random.choice(letters)
        vowcount = 0
        if choice in vowels:
            vowcount += 1
        if len(word) > int(maxlen):
            print(word)
            break
        if choice == "NULL":
            if any([letter in word for letter in vowels]) and any([letter in word for letter in consonants]) and len(word) > int(minlen):
                if prev == "J" or prev == "V":
                    word += "E"
                if prev == "F" or prev == "L" or prev == "S" and vowcount == 1 and word[-2] != prev:
                    word += prev
                prevletter = "NULL"
                prevprevletter = "NULL"
                for j,letter in enumerate(word):
                    if prevletter != "NULL" and prevprevletter != "NULL":
                        if vowcount == 2:
                            if prevprevletter in consonants and prevletter in vowels and letter in consonants:
                                word = word[:j] + letter + word[j:]
                        if prevletter == prevprevletter and prevletter == letter:
                            word = word[:j-1] + word[j:]
                    prevprevletter = prevletter
                    prevletter = letter
                print(word)
                break
            else:
                pass
        else:
            if choice == "Q":
                word += "QU"
                vowcount += 1
                prev = "U"
            elif prev in consonants and choice in consonants:
                if prev == choice and len(word) > 2 and word[-2] != choice:
                    word += choice
                    prev = choice
                elif prev == "D":
                    if choice == "R":
                        word += choice
                        prev = choice
                elif prev == "S":
                    if choice in ["T","C","L","K","M","N","P","T","W","H"]:
                        word += choice
                        prev = choice
                elif prev == "P": 
                    if choice in ["H", "L", "R"]:
                        word += choice
                        prev = choice
                elif prev == "T": 
                    if choice in ["H","R","L","W"]:
                        word += choice
                        prev = choice
                elif prev == "W": 
                    if choice in ["R","H"]:
                        word += choice
                        prev = choice
                elif prev == "B": 
                    if choice in ["R","L"]:
                        word += choice
                        prev = choice
                elif prev == "C":
                    if choice in ["L","R","H","K"]:
                        word += choice
                        prev = choice
                elif prev == "F":
                    if choice in ["L","R"]:
                        word += choice
                        prev = choice
                elif prev == "G":
                    if choice in ["L","R","H"]:
                        word += choice
                        prev = choice
                elif prev == "N":
                    if choice in ["K","G"]:
                        word += choice
                        prev = choice
                else:
                    pass
            elif prev in vowels and choice in vowels:
                if (prev == "I" or choice == "I") and (prev == "E" or choice == "E"):
                    if len(word) > 2 and word[-2] == "C":
                        word = word[:-1] + "E"
                        word += "I"
                        prev = "I"
                    else:
                        word = word[:-1] + "I"
                        word += "E"
                        prev = "E"
            else:
                if prev == "C":
                    if choice in ["E","I","Y"]:
                        word = word[:-1] + "K" + choice
                    else:
                        word += choice
                else:
                    word += choice
                prev = choice