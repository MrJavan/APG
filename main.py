import random
import os
clear = lambda: os.system('cls')
cwords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
swords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chars = ['!','@','#','$','&','*','%','^']
clear()
print("- Specify the level of password security.")
print("")
print("[1] Secure Password - (Includes uppercase and lowercase letters)")
print("[2] Secure Plus Password - (Includes uppercase and lowercase letters)")
print("[3] Ultra Secure Password - (Includes uppercase and lowercase letters)")
print("")



def generate(first_user_input , second_user_input):
    # if not first_user_input.isdigit() or 1 <= int(first_user_input) <= 3:
    #     clear()
    #     print("- Your input not valid.")
    #     print("")
    #     first_user_input = input("[?] Try Again :")
    #     generate(first_user_input , second_user_input)

    if first_user_input == "1":
        clear()
        list = cwords + swords
        result = random.choices(list, k=int(second_user_input))
        print(''.join(result))
    elif first_user_input == "2":
        clear()
        list = cwords + swords + numbers
        result = random.choices(list, k=int(second_user_input))
        print(''.join(result))
    elif first_user_input == "3":
        clear()
        list = cwords + swords + numbers +chars
        result = random.choices(list, k=int(second_user_input))
        print('Generated Password: ',''.join(result))
    # elif first_user_input not first_user_input.isdigit():

    # else:
    #     clear()
    #     print("- Your input not valid.")
    #     print("")
    #     first_user_input = input("[?] Try Again :")
    #     generate(first_user_input , second_user_input)



def pwdlen (second_user_input):
    if not second_user_input.isdigit() or int(second_user_input) < 8:
        clear()
        print("The inserted password length is not secure.")
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
        first_user_input = input("[?] Try Again :")
        check(first_user_input)
    # else:
        
    #     pwdlen(second_user_input)


first_user_input = input("[?] Select Number :")
check(first_user_input)

clear()

print("- Specify the password length.")
print("")
second_user_input = input("[?] insert Number :")

pwdlen(second_user_input)


