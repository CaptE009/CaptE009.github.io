import random 
import string

def generate_pass(amount):

    print("We are going to prompt you to create a password " + str(amount), "times, you may then select which one is most fitting to you!")
    
    for i in range(amount):

        random_password = [ ]

        randomizer_list = [string.digits, string.ascii_lowercase, string.punctuation, string.ascii_uppercase]

        count = 0

        password_length = int(input("How long would you like your new password to be? Numbers # only: "))

        while password_length < 8:
            password_length = int(input("Please enter a positive digit greater than or equal to 8. Passwords under 8 characters aren't up to safety standards. Try again: "))
        
        while count < password_length: 
            initial_pick = random.choice(randomizer_list)
            final_pick = random.choice(initial_pick)

            while final_pick == (',', '`'): 
                final_pick = random.choice(initial_pick)
                if final_pick != (',', '`'):
                    break

            random_password.append(final_pick)
            count += 1

        print("Your new randomly-generated unique password is", ''.join(random_password))


print("In today's world, where cybersecurity plays a significant part in our daily lives, it is often overlooked by many. This password generator is meant to help you " \
"pick a safe and strong password to use for anything from video games, to school/work accounts, to emails, etc.\n")
print("Your passwords are always recommended to be over 8 characters long to be up to security standards, changed often, and stored somewhere safely where it doesn't end up in the wrong hands. ")


badpassword_list = ["superman", "spiderman", "password", "123456", "Mustang"]
decision = int(input("We will showcase a bad password and a good password that you will generate yourself, what would you like first? 1. Bad Password  2. Good Password "))
 
while decision != (1 or 2):
        
    if decision == 1:
        print()
        print(badpassword_list)
        print()
        print("Now let's generate some better passwords!\n")
        generate_pass(5)
        print("Remember to use strong passwords for your different online applications and to ensure that they meet safety standards! ")
        break

    elif decision == 2: 
        generate_pass(5)

        print("Those are some good passwords, select whicever one you find most fitting!\n")
        print("Now lets check out some examples of bad passwords you should avoid: \n")

        print(badpassword_list)
        
        print("Remember to use strong passwords for your different online applications and to ensure that they meet safety standards! \n")
        break 
    else: 
        decision = int(input("Please enter a valid digit: "))

    
        