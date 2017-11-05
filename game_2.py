import pyttsx
import random
'''
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-50)
'''
#volume = engine.getProperty('volume')
#engine.setProperty('volume', volume-20)
#engine.setProperty('voice',voice[1].id)
#engine.setProperty('voice',age=20,gender='female')

#def intro():
import pygame
import sys
import speech_recognition as sr
pygame.init()
#pygame.mixer.music.load('/home/anorak/Documents/projects/pygame_learning/Sabrepulse-Turbo-City-01-Cityscape-Dreams.ogg')
sound = pygame.mixer.Sound('/home/anorak/Documents/projects/pygame_learning/Sabrepulse-Turbo-City-01-Cityscape-Dreams.ogg')
pygame.mixer.Sound.set_volume(sound,0.1)
pygame.mixer.Sound.play(sound,100)

#from hotword import main
import os
def main():
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-40)

    engine.say('Welcome to the beginning of your secret adventure Galactic Traveler       ')
    engine.say('The Galaxy is in turmoil and you are the only one that can help!      ')
    engine.say('what class do you want to be?        ')
    engine.runAndWait()
    a = str(raw_input('class? '))
    if a == 'exit':
        os.system('python hotword.py')

    engine.runAndWait()
    engine.say('       the   ')
    engine.say(a)
    engine.say('  what an class intersting choice')
    engine.say('        ')
    engine.say('What  weapon do you choose?  ')
    engine.runAndWait()
    b = str(raw_input('weapon? '))
    if b == 'exit':
        os.system('python hotword.py')
    engine.say('intersting choice')
    engine.runAndWait()


    engine.say('            ')
    engine.say(b)
    engine.say('   hmm...     i hope you chose wisely   ')
    engine.say('             ')
    engine.say('You are currenely traversing  a planets  in search of lost alien technology ')
    engine.say('You pass by a bunch of ancient alien space ships and then you hear it  ')
    engine.say('I have a bad feeling about this      ')

    engine.say(' You encounter a huge galactic alien')
    engine.say('  It lunges at you but you dodge thanks to your ')
    engine.say(a)
    engine.say('     training')
    engine.say(' oh no             It looks like theres no escape the only option is too fight          ')
    engine.say('What do you doo with your weapon ???')
    engine.say('          ')
    engine.runAndWait()
    checker = True
    player_lp = 100
    enemy_lp = 200
    while checker:
        randy_1 = random.randint(0,10)
        randy_2 = random.randint(0,50)

        player_lp -= randy_1
        enemy_lp -= randy_2
        c = str(raw_input('action?  '))
        if c == 'exit':
            os.system('python hotword.py')
        engine.say("you        ")
        engine.say(c), engine.say('        ')
        engine.say(' at the giant beast     ')
        engine.say(' with your    ')
        engine.say(b)
        engine.say('the enemy has')
        engine.say(str(enemy_lp))
        engine.say('     health points remaining  ')
        #engine.runAndWait()
        if randy_2 > 40:
            engine.say(" Critical hit on the alien")
            #engine.runAndWait()

        engine.say(' you have   ')
        engine.say(str(player_lp))
        engine.say('        health points remaining')
        engine.runAndWait()
        #if randy_1 > 8:
            #engine.say('You suffered a critical hit')
            #engine.runAndWait()


        if player_lp == 0:
            engine.say('                 ')
            engine.say('OH NO YOU HAVE LOST ')
            engine.say('GAME OVER')
            engine.say('WANT TO PLAY AGAIN')
            engine.runAndWait()
            again = raw_input("again? (Y or N) ")
            if again == "Y" or again == "y":
                main()
            else:
                os.system('python hotword.py')
        elif enemy_lp == 0:
            engine.say('YOU WIN ')
            engine.say('You have saved the galaxy!!!')
            engine.say('Want to play again?')
            again = raw_input("again? (Y or N) ")
            if again == "Y" or again == "y":
                main()
            else:
                os.system('python hotword.py')






main()
