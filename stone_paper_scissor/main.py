name = input(" Hello player !! . Please enter your name: ")
print("")
print("Hey " + name + ", lets go through the RULES of this game first")
print("""
 lets start the game 
""")

import random

members = ['rock', 'paper', 'scissor']

print("""
reply with stone, paper or scissor
""")
cou = 0
for tc in range(3):
    computer_input = random.choice(members)

    inputt = input('Enter your attack: ')
    if inputt=='rock' and computer_input=='paper':
        print('you lose !!')
    elif inputt=='paper' and computer_input=='scissor':
        print('you lose !!')
    elif inputt=='scissor' and computer_input=='rock':
        print('you lose !!')
    elif inputt==computer_input :
        print('its a draw')
    else:
        print('you won !!')