import random
import os
import pyperclip

clear = lambda: os.system('cls')
cwords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
swords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chars = ['!','@','#','$','&','*','%','^']
clear()
print("- Specify the level of password security.")
print("")
print("[1] Secure Password - (Includes uppercase and lowercase letters)")
print("[2] Secure Plus Password - (Includes letters and numbers)")
print("[3] Ultra Secure Password - (Includes letters, numbers and characters)")
print("")



def generate(first_user_input , second_user_input):
    if first_user_input == "1":
        clear()
        list = cwords + swords
        result = random.choices(list, k=int(second_user_input))
        print('Generated Password: ',''.join(result))
        pyperclip.copy(''.join(result))
        print("")
        print("# (Password copied to your clipboard)")
        print("")

    elif first_user_input == "2":
        clear()
        list = cwords + swords + numbers
        result = random.choices(list, k=int(second_user_input))
        print('Generated Password: ',''.join(result))
        pyperclip.copy(''.join(result))
        print("")
        print("# (Password copied to your clipboard)")
        print("")

    elif first_user_input == "3":
        clear()
        list = cwords + swords + numbers +chars
        result = random.choices(list, k=int(second_user_input))
        print('Generated Password: ',''.join(result))
        pyperclip.copy(''.join(result))
        print("")
        print("# (Password copied to your clipboard)")
        print("")



def pwdlen (second_user_input):
    if not second_user_input.isdigit() or int(second_user_input) < 10:
        clear()
        print("The inserted password length not valid or not secure.")
        print("")
        second_user_input = input("[?] Try Again :")
        pwdlen(second_user_input)
    else:
        generate(first_user_input , second_user_input)

def check(first_user_input):
    if first_user_input not in ['1', '2', '3']:
        clear()
        print("- Your input not valid.")
        print("")
        print("[1] Secure Password - (Includes uppercase and lowercase letters)")
        print("[2] Secure Plus Password - (Includes letters and numbers)")
        print("[3] Ultra Secure Password - (Includes letters, numbers and characters)")
        print("")
        first_user_input1 = input("[?] Try Again :")
        first_user_input1 = check(first_user_input1)
        return first_user_input1
    else:
        return first_user_input

    

first_user_input = input("[?] Select Number :")
first_user_input = check(first_user_input)

clear()

print("- Specify the password length.")
print("")
second_user_input = input("[?] insert Number :")

pwdlen(second_user_input)


