import random

""" Plays a game of mental math derived from the Mental Math book. """

def multiplyByEleven():
    """ Multiply by 11 """
    #print("Multiply by 11")
    #print("--------------\n")
    a = random.randint(10, 99)
    correct_answer = str(a * 11)
    user_answer = input(str(a) + " x 11 = ")
    if (correct_answer == user_answer):
        print("Correct!")
        return 1
    else: 
        print("Wrong! The correct answer is " + correct_answer)
        return 0



def main():
    print("\n==================")
    print("|Mental Math Game|")
    print("==================\n")

    total_correct = 0
    total_correct += multiplyByEleven()
    total_correct += multiplyByEleven()
    total_correct += multiplyByEleven()
    total_correct += multiplyByEleven()

    print("\nTotal correct: " + str(total_correct))
main()