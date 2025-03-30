

questions = [
    "how many elements are there in perodic Table?",
    "Which animal layes the largest eggs ?",
    "what is the most abundant gas in Earth's atmosphere ?",
]

options = (("A. 126",'B. 102','C. 118'),("A. Whale","B. Elephant","C. Ostrich"),("A. Nitrogen","B. 02","C. co2"))
answer = ("c","c","a")
guesses = []
score =0
question_num = 0

for question in questions :
    print("..................")
    print(question)
    
    for  option in options[question_num]:
        print(option)
    

    guess = input("enter correct answeer : ").lower()
    guesses.append(guess)

    
    if guess == answer[question_num]:
        print("correct")
        question_num+=1
        score += 1

    else:
        print("incorrect")
         
print("..............Result..............")
print(f"\n Here Your total score is {score}")