import random 

words=["Hana" , "Yomna" , "Mariam" , "shad" ,"dareen"]

original_word=random.choice(words)

scrambled_word=""
for char inrandom.scrambled(original_word , len(original_word)):
    scrambled_word +=char

tries=5

print("welcome to the world scramble game!")
print(f"try to guess the original weord from the scrambled word :{scrambled_word}" )
print(f"you have {tries} a tries .")

while tries > 0:
    guess= input ("Enter your guess :").strip()

    if guess==original_word:
        print("congratulation ! you guessed the correct word !")
        break 
    else:
        tries -= 1
        print(f"incorrect ! you have {tries} tries ")

    if tries==0:
        print(f"game over! the correct word was :{original_word}")     