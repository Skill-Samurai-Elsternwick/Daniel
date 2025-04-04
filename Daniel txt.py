import sys
import random
import time

def typewriter(message):
    for L in message:
        sys.stdout.write(L)
        sys.stdout.flush
        time.sleep(0.05)
    sys.stdout.write('\n')

hp = random.randint(6, 12)

def game_over(hp):
    if hp <= 0:
        typewriter("Womp Womp, what did I tell you")
        time.sleep(3)
        sys.exit()
    else:
            typewriter("You have " + str(hp) + "HP left")

def damage(damage, hp):
     hp -= damage
     game_over(hp)

def fight_banana():
    typewriter("this is a strong and skibidi opponent. will you fight or run? [fight or run]")

def cavern():
    global hp

    typewriter("Will you bash down the door or climb the spring for the key? [hit or climb]: ")
    decision = input()

    if decision == "hit":
        typewriter("you hit the door and a giant skibidi toilet falls on you")
        damage(random.randint(2, 4), hp)
    elif decision == "climb":
        typewriter("you unleash your aura and climb to the top to get the key")
        typewriter("you walk through the door and a giant banana drops in front of you")
        fight_banana()

def way():
    global hp

    typewriter("you are in a cave. There are 2 ways you can go, left and right. Which way? [left or right]")
    decision = input()

    if decision == "left":
        typewriter("the left path leads you to a small cavern with a spring in the centre and a key on top of the spring")
        typewriter("the key must lead to the small rotted door to the right of the spring")
        cavern()
    elif decision == "right":
        typewriter("you walk down the right path, but run into some spikes")
        damage(random.randint(1, 3), hp)

def start_game():
    global hp

    typewriter("Begin? [yes or no]: ")
    play = input()
          
    if play == "yes":
        typewriter("Lets start!")
        way()
        game_over(hp)

typewriter("You are probably going to die so any last words?")

start_game()