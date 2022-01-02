import random
from tkinter import *
from tkinter import ttk

playernum = 0
number = 0
CPU = 0
PLAYER = 0
i = 0
runda = 0


# random number med NUMBER
def randnum():
    global number
    number = int(random.randrange(0, 3, 1))


# number som input
def stensaxpase(number):
    global word
    if number == 0:
        word = 'sten'

    elif number == 1:
        word = 'sax'

    else:
        word = 'påse'


# playerinput här ska playernum fås
def playerinput():
    global playernum
    print("välj mellan sten sax och påse, skriv ut valet")
    while True:
        player = input()
        if player == 'sten':
            playernum = 0
            break
        elif player == 'sax':
            playernum = 1
            break
        elif player == 'påse':
            playernum = 2
            break
        else:
            print("du måste skriva sten, sax eller påse")


def winner(number, playernum):
    global CPU
    global PLAYER
    if number == playernum:
        print("it's a tie")
    elif number == 0 and playernum == 1:
        print("cpu wins, rock beats scissors")
        CPU += 1
    elif number == 0 and playernum == 2:
        print("player wins, paper beats rock")
        PLAYER += 1
    elif number == 1 and playernum == 0:
        print("player wins, rock beats scissors")
        PLAYER += 1
    elif number == 1 and playernum == 2:
        print("cpu wins, scissors beat paper")
        CPU += 1
    elif number == 2 and playernum == 0:
        CPU += 1
        print("cpu wins, paper beats rock")
    elif number == 2 and playernum == 1:
        print("player wins, scissors beats paper")
        PLAYER += 1


def printdetails(playernum):
    if playernum == 0:
        x = 'sten'
    elif playernum == 1:
        x = 'sax'
    elif playernum == 2:
        x = 'påse'

    print("player:", x)


def printdetails2(number):
    if number == 0:
        k = 'sten'
    elif number == 1:
        k = 'sax'
    elif number == 2:
        k = 'påse'
    print("CPU:", k)


def sammanlagdvinnare():
    global i
    if i != runda - 1:
        print("CPU:", CPU)
        print("PLAYER:", PLAYER)
        i += 1
    elif i == runda - 1:
        if CPU == PLAYER:
            print("CPU:", CPU)
            print("PLAYER:", PLAYER)
            print("det är lika, det blir förlängning")
            i = i
        elif CPU > PLAYER:
            print("CPU:", CPU)
            print("PLAYER:", PLAYER)
            print("CPU vinner")
            i += 1
        else:
            print("CPU:", CPU)
            print("PLAYER:", PLAYER)
            print("player vinner")
            i += 1


def rundor():
    print("hur många rundor vill du köra?")
    while True:
        try:
            global runda

            runda = int(input())
            if runda > 0:
                print("du vill köra", runda, "runda/or")
                break
            else:
                print("får inte vara noll, försök igen")
        except ValueError:

            print("Måste vara ett nummer och större än 0")


"""
rundor()
while i < runda:
    playerinput()
    randnum()
    stensaxpase(number)
    printdetails(playernum)
    printdetails2(number)
    winner(number, playernum)
    sammanlagdvinnare()

"""
root = Tk()
ja = 0


def createNewWindow():
    newWindow = Toplevel(root)
    root.withdraw()
    newWindow.title("STEN SAX PÅSE")

    sten = ttk.Button(newWindow, text="sten", command=datorvalsten).grid(column=0, row=1)
    sax = ttk.Button(newWindow, text="sax", command=datorvalsax()).grid(column=1, row=1)
    pase = ttk.Button(newWindow, text="påse", command=datorvalpase).grid(column=2, row=1)
    pase = ttk.Button(newWindow, text="sluta spela", command=root.destroy).grid(column=1, row=3)


def skapanyram():
    global frm
    frm = ttk.Frame(root, padding=10)
    frm.grid()


def villduspel():
    ttk.Label(frm, text="vill du lira sten sax påse").grid(column=0, row=0)
    btn1 = ttk.Button(frm, text="ja", command=createNewWindow).grid(column=1, row=1)
    btn2 = ttk.Button(frm, text="nej", command=root.destroy).grid(column=1, row=0)


def datorvalsten():
    randnum()
    stensaxpase(number)
    if number == 0:
        print("lika")
    elif number == 1:
        print("sten vinner mot sax")
    else:
        print("sten förlorar mot påse")
    print(word)


def datorvalsax():
    randnum()
    stensaxpase(number)
    if number == 0:
        print("sax fölorar")
    elif number == 1:
        print("lika")
    else:
        print("sax vinner mot påse")
    print(word)


def datorvalpase():
    randnum()
    stensaxpase(number)
    if number == 0:
        print("påse vinner mot sten")
    elif number == 1:
        print("sax vinner mot påse")
    else:
        print("lika")
    print(word)


# main

skapanyram()
villduspel()

root.mainloop()