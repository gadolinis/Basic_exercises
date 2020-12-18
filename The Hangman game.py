import random

word_file = "Random words"
WORDS = open(word_file).read().splitlines()
wordW = random.choice(WORDS)
word = wordW.lower()

length = len(word)
wordl = str("_" * length)
print(" ".join(wordl))

z = input("Please enter the letter: ")
x = z.lower()
print(x)

i = 10

while i != 0:
    i = i - 1            #i -= 1 ?????????????
    print("jums liko spejimai")
    print(i)
    #output = search(x)
    wordx = ""
    for (letter, letterl) in zip(word, wordl):
        if letter == x:
            wordx = wordx + x
        else:
            wordx = wordx + letterl
    wordl = wordx
    output = " ".join(wordl)
    print(output)
    if wordl == word:
        print("You are right")
        break
    z = input("Please enter the letter: ")
    x = z.lower()

print(output)
print(word)





               # if letterx == "_ ":
             #   else:
                #    wordx = wordx + letterx
