import numpy as np
choices = ["rock","paper","scissors"]

user_input = input("Pick rock, paper or scissors: ")
print(f'You chose {user_input}.')


computer_num = np.random.randint(0,3)
computer_pic = choices[computer_num]
print(f'Computer chose {computer_pic}.')

def rps(user_input,computer_pic):
    if user_input == computer_pic:
        return f"It's a draw!"
    elif user_input == "rock" and computer_pic == "paper":
        return f"You loose!"
    elif user_input == "rock" and computer_pic == "scissors":
        return f"You win!"
    elif user_input == "paper" and computer_pic == "rock":
        return f"You win!"
    elif user_input == "paper" and computer_pic == "scissors":
        return f"You loose!"
    elif user_input == "scissors" and computer_pic == "rock":
        return f"You loose!"
    elif user_input == "scissors" and computer_pic == "paper":
        return f"You win!"

print(rps(user_input,computer_pic))
    
    
    