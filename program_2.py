#Math Quiz
#Samuel Renneke, 2/13/2026

import random

def quiz (n1, n2):
    print("  ", n1)
    print("+ ", n2)
    print("______")
    answer = n1 + n2
    return answer

output = quiz(random.randrange(100,1000), random.randrange(100,1000))

user_answer = float(input("What's your answer? "))

if user_answer == output:
    print("Congratulations! You're answer is correct!")
else:
    print("Sorry, your answer is incorrect. \nThe correct answer was:", output)
