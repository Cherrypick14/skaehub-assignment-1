#password generator
import random

def gen_random_pass():
    lower_case ="abcdefghijklmnopqrstuvwxyz"
    upper_case ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits= "0123456789"
    symbols = "@#$&_-(=%*:/!?+."

    string = lower_case + upper_case + digits + symbols
    length = int(input("What length do you want your password to be?: "))
    password = "".join(random.sample(string, length))
    print("Your password is: ", password)
    pass
gen_random_pass()