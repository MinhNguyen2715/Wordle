from Word import word
import random
ran_num = random.randint(0,2308)
hidden_word = word[ran_num]
res = 0
print(hidden_word)

#main
print("THIS IS WORDLE!!! \n LET'S START! \n    _____")
for i in range(6):
    user = str()
    while(len(user) != 5):
        print("Word's length must be 5")
        user = str(input("Enter your word: ")).lower()
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