from Word import word
import random
import Error
ran_num = random.randint(0,2308)
hidden_word = word[ran_num]
res = 0
last_word = []


#main
print("THIS IS WORDLE!!! \n LET'S START! \n    _____")
for i in range(6):
    if i != 0:
        print("Guessed:",*last_word,sep="\n")
    while True:
        try:
            user = str(input("Enter your word: "))
            if len(user) < 5 or len(user) > 5:
                raise Error.InvalidLength()
            user.lower()
            break
        except Error.InvalidLength as e:
            print(str(e) + " has been raise")

    last_word.append(user)

    if user == hidden_word:
        print("Great!")
        res = 1
        break
    else:
        print(user)
        for j in range(5):
            if(user[j] not in hidden_word):
                print("x",end="")
            elif(user[j] != hidden_word[j]):
                print("-",end="")
            else:
                print("*",end="")
        print("\nTry again! You have %d more tries!" %(6-i-1))

if res == True:
    print("You win! The word is %s" %hidden_word)
else:
    print("You lose! The word is %s" %hidden_word)