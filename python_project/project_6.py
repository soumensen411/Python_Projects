#python Quiz Game

questions = (
    ('1. What is the capital of Bangladesh? '),
    ('2. How many elements are in the periodic table? '),
    ('3. What is the smallest prime number?'),
    ('4. Which country is known as the Land of the Rising Sun?'),
    ('5. Who wrote the play "Romeo and Juliet"?')
    )
options = (
    ('A. Sylet','B. Dhaka','C. Chittagong','D. Rajshahi'),
    ('A. 116','B. 117','C. 118', 'D. 120'),
    ('A. 1','B. 2','C. 3','D. 5'),
    ('A. China','B. South Korea','C. Japan','D.Thiland'),
    ('A. Charles Dickens','B. William Shakespeare', 'C. Mark Twain','D. Jane Austen')
)
answer = ('B','C','B','C','B')
guesses = []
question_num = 0
mark = 0
for question in questions:
    print('------------------')
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if(answer[question_num] == guesses[question_num]):
        print("Correct")
        mark = mark + 2
    else:
        print("Incorrect")
    question_num = question_num + 1
print("****************************")
print(f"Your total mark is {mark}")
print("****************************")

