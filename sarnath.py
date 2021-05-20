#!/usr/bin/python3
from  time import sleep,time
import art
from getkey import getkey
from pygame import mixer
import cursor
from playsound import playsound
cursor.hide()
mixer.init()
CLEAR_ST="\x1b[H\x1b[2J\x1b[3J"
def clear():
    print(CLEAR_ST)
def print_a(text,font,**kwargs):
    m=art.text2art(text,font=font)
    print(m,**kwargs)
def main():
    clear()
    mixer.music.load("music/lost-places.wav")
    mixer.music.play()

    print_a("          DOOM OF SARNATH" ,"fancy91")
    print("\n" *4)
    print_a("           By BANANA STUDIO ", "fancy92")
    print("\n" *4)
    print_a("           Loading... ", "fancy95",end="\r")
    sleep(3)
    print_a("           Press S to start or Q to quit","fancy93")

    while True:
        key=getkey()
        if key in ['s', 'S']:
            clear()
            break
        elif key in ['q','Q']:
            clear()
            cursor.show()
    mixer.music.fadeout(3)
    mixer.music.load("music/outside.wav")
    mixer.music.play(loops=-1)
    print("\n"*9)
    print_a("Sarnath, India, 3000 B.C." ,"fancy91")
    sleep(5)
    clear()
    print("You wasn't in the city when it happened.")
    sleep(3)
    print("Everybody was there, celebrating The 100th anniversary of Defeat of Yb...")
    sleep(3)
    print("Except you. You was on important bussiness meeting in Ferannta.")
    sleep(3)
    print("You wasn't there when it happened.")
    sleep(3)
    print("You wasn't there when", end=" ",flush=True)
    sleep(0.2)
    print_a("DOOM", "fancy91", end=" ",flush=True)

    playsound("music/thunder.wav")
    print("came to Sarnath.",flush=True)
    sleep(2)
    print("You wasn't there, when all who you ever loved died.")
    sleep(2)
    print("And you wonder...")
    sleep(3)
    print_a("WHY?","fancy87")
    sleep(2)
    clear()
    sleep(0.1)
    print("You thought you was leading peaceful life...")

    sleep(3)
    
    print("You never killed anyone, neither your father did so, nor your grandfather...")

    sleep(2)
    print("Maybe...")
    sleep(1)
    print("Maybe this disaster has roots in the past...")
    sleep(2)
    print("You thought about that...")
    sleep(3)
    print("And at that time...")
    sleep(2)
    print("Your curiosity won fight with your self-preservation instinct...")
    playsound("music/thunder.wav")
    print("And you decided to set out on the long trip from Ferannta to Sarnath.")
    sleep(3)
    clear()

if __name__=='__main__':
    try:
        main()
    except:
        cursor.show()
        raise
    cursor.show()
