def UserInput():
    return input("please enter your word :")


def checker():
    text = UserInput()
    if text == text[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

def run():
    checker()
run()
