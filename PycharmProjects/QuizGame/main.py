def new_game():
    ans = []
    correct_ans = 0
    ques_num = 1

    for key in ques_ans:
        print(".......................")
        print(key)
        for i in options[ques_num-1]:
            print(i)
        guess = input("ANSWER: ").upper()
        ans.append(guess)
        correct_ans += check_answer(ques_ans.get(key), guess)
        ques_num += 1

    display(correct_ans, ans)
    play_again()
#-----------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!!")
        return 1
    else:
        print("WRONG ANSWER!!")
        return 0


#-----------------------------------
def display(correct_ans, ans):
    print("......................")
    print("---RESULT---")
    print("CORRECT ANSWER: ", end="")
    for i in ques_ans:
        print(ques_ans.get(i), end=" ")
    print("\n......")

    print("YOUR ANSWER: ", end="")
    for i in ans:
        print(i, end=" ")
    print("\n......")

    score = int((correct_ans/len(ques_ans))*100)
    print("Your score is "+str(score)+"%")
#-------------------------------------
def play_again():
    respond = input("Do you want to play again, YES or NO: ").upper()
    if respond == "YES":
        new_game()



#-------------------------------------

#dictionary
ques_ans = {
    "Who created Python?: ": "A",
    "What was the year Python was created?": "B",
    "Python is tributed to which comedy show?: ": "C",
}
#2D list
options =[["A. Guido van Rossum", "B. James Gosling", "C. Bjarne Stroustrup"],
          ["A. 1979", "B. 1991", "C. 1995"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python"]]

new_game()
print("Good luck!")