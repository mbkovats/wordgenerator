import random

# Function to generate words
# minlen: minimum length of the word
# maxlen: maximum length of the word
# words: number of words to generate
# nulls: decreases average word length the higher the number
def word_generator(minlen: int, maxlen: int, words: int, nulls: int):
    wordlist = []
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    vowels = ["A", "E", "I", "O", "U"]
    consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    # Add the word terminators to the list of letters
    for _ in range(int(nulls)):
        letters.append("NULL")
    # Generate the words
    for _ in range(int(words)):
        # Decide if Y is a vowel or consonant
        if random.randint(0,1) == 1:
            vowels.append("Y")
        else:
            consonants.append("Y")
        word = ""
        # Keep track of previous letter
        prev = "NULL"
        # Keep track of the number of vowels in the word
        vowcount = 0
        # Create a word
        while(True):
            choice = random.choice(letters)
            if choice in vowels:
                vowcount += 1
            # If you hit a word terminator or the length of the word is greater than the maximum length, print the word after doing some checks to see if it is valid
            if choice == "NULL" or len(word) >= int(maxlen):
                # Check if the word is at least the minimum length, otherwise keep going
                if len(word) >= int(minlen):
                    # Check if the word has at least one vowel and one consonant
                    if vowcount > 0 and any([letter in word for letter in consonants]):
                        # Words can't end with J or V
                        if prev == "J" or prev == "V":
                            word += "E"
                        # Floss Rule
                        if prev in ["F", "L", "S", "Z"] and vowcount == 1 and word[-2] != prev:
                            word += prev
                        prevletter = "NULL"
                        prevprevletter = "NULL"
                        for j,letter in enumerate(word):
                            if prevletter != "NULL" and prevprevletter != "NULL":
                                # Make consonants double if vowel before is short and there are 2 syllables. Rabbit rule.
                                if vowcount == 2 and j < len(word) - 1:
                                    if prevprevletter in consonants and prevletter in vowels and letter in consonants and word[-1] not in vowels and word[j+1] in vowels and letter in ["B","D","R","P","T","M"] and random.randint(0,1) == 1:
                                        word = word[:j] + letter + word[j:]
                                # Make sure there are no triple letters
                                if prevletter == prevprevletter and prevletter == letter:
                                    word = word[:j-1] + word[j:]
                            prevprevletter = prevletter
                            prevletter = letter
                        wordlist.append(word)
                        break

                    # If the word is all vowels or consonants, start over
                    elif vowcount == len(word) or vowcount == 0:
                        word = ""
                        vowcount = 0
                        prev = "NULL"
            # If it's not a word terminator
            else:
                # Q is always followed by U
                if choice == "Q":
                    word += "QU"
                    vowcount += 1
                    prev = "U"
                # If there are back to back consonants in the word, make sure they are valid
                elif prev in consonants and choice in consonants:
                    # Two of the same consonant in a row is allowed
                    if prev == choice and len(word) > 2 and word[-2] != choice:
                        word += choice
                        prev = choice
                    # Common consonant blends
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
                    elif prev == "R":
                        if choice in ["B","T", "C", "D", "G", "K", "L", "M", "N", "P", "S", "T", "W"]:
                            word += choice
                            prev = choice
                    else:
                        pass
                # Back to back vowels are always allowed
                elif prev in vowels and choice in vowels:
                    # I before E except after C
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
                        word += choice
                        prev = choice
                # Consonants are always allowed after vowels or vice versa
                else:
                    # C is always K if followed by E, I, or Y
                    if prev == "C":
                        if choice in ["E","I","Y"]:
                            word = word[:-1] + "K" + choice
                        else:
                            word += choice
                    # Add the letter to the word if it's not a special case
                    else:
                        word += choice
                    # Update the previous letter
                    prev = choice
        
        # Remove Y from the list of vowels or consonants
        if "Y" in vowels:
            vowels.remove("Y")
        else:
            consonants.remove("Y")
    return wordlist


if __name__ == "__main__":
    minlen = ""
    maxlen = ""
    nulls = ""
    words = ""
    # Prompt the user for the minimum and maximum word length
    while(minlen == "" or maxlen == "" or int(minlen) > int(maxlen) or int(minlen) < 3):
        minlen = input("Minimum word length: ")
        maxlen = input("Maximum word length: ")
        if minlen == "" or maxlen == "":
            print("The minimum and maximum word length cannot be blank.")
        elif int(minlen) > int(maxlen):
            print("The minimum word length cannot be greater than the maximum word length.")
        elif int(minlen) < 3:
            print("The minimum word length cannot be 2 or less.")

    # Prompt the user for the number of word terminators
    while(nulls == "" or int(nulls) < 1):
        nulls = input("How many word terminators would you like? (The larger the number, the smaller the average word length): ")
        if nulls == "":
            print("The number of word terminators cannot be blank.")
        elif int(nulls) < 1:
            print("The number of word terminators cannot be negative or zero.")


    # Prompt the user for the number of words to generate
    while(words == "" or int(words) < 1):
        words = input("How many words would you like to generate? ")

    # Generate the words
    wordlist = word_generator(minlen, maxlen, words, nulls)
    for word in wordlist:
        print(word)