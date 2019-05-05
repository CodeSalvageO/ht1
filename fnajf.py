import time
import sys
import os

print("""There was always an empty farmhouse near the cemetery. Being a kid, you decided to be stupid and break into it. It would come to be that you would regret making that choice.""")

time.sleep(6)
os.system("cls")
print("""
T
H
A
J
F
""")
time.sleep(1)
os.system("cls")
print("""
Two
Hours
At
Jayden's
Farm
""")
time.sleep(1.5)
os.system("cls")
print("CONNECTING..............................")
time.sleep(1)
print("CONNECTED!")
time.sleep(1.5)
print("You: dude, I'm going to check out the old farmhouse.")
time.sleep(1.5)
print("Friend: I really don't think you should do that.")
time.sleep(1.5)
print("You: Why not?")
time.sleep(1.5)
print("Friend: Thats trespassing")
time.sleep(1.5)
print("You: I'll be careful not to get caught. ok?")
time.sleep(1)
os.system("cls")
print("First Hour")
time.sleep(2)
print("You enter a barn. It has a tractor, a bunch of hay, and a crossbow.")
time.sleep(0.8)
print("The tractor is broken.")
time.sleep(0.5)
tractor = input('(S)hoot the tractor with the crossbow. (W)alk Away.')
if tractor == 'S' or tractor == 's':
  print("Good. The motor is broken.")
else:
  print("As you turn to walk away, the FBI shows up and makes you go to jail.")
  sys.exit()
time.sleep(1)
print("You start to walk out of the barn, and head over to the house.")
choice2 = input('(S)ide Door or (F)ront Door: ')
if choice2 == 'S' or choice2 == 's':
  print("The side door creaks open and you start to walk in.")
else:
  print("You are forced to work on Jayden's farm for 5 hours.")
  sys.exit()
print("A small, flickering lantern is in the corner.")
choice3 = input('(T)ake it or (L)eave it.')
if choice3 == 'T' or choice3 == 't':
  print("You take it, shining the lantern around the dark room.")
else:
  print("The lantern turns off and you are arrested for trespassing.")
  sys.exit()
print("As you roam through the dark halls of the house, you see a door with a variety of strange machines.")
choice4 = input('(G)o in or (S)tay out: ')
if choice4 == 'S' or choice4 == 's':
  print("The machines stay inside the dark room.")
else:
  print("The door closes behind you and the machines pester you all day.")
  sys.exit()
print("Walking further down, an old TV flickers on and off.")
choice5 = input('(T)urn it off or (L)eave it be.')
if choice5 == 'T' or choice5 == 't':
  print("Jayden comes for you and screams at you for trespassing, like an hour or so.")
  sys.exit()
else:
  print("The TV remains untouched.")
print("The First Hour has passed lol!")
time.sleep(1)
os.system("clear")
print("Second Hour")
print("A Jayden comes and begins ranting about how his tractor broke down.")
choic1 = input('(H)ide behind tv or (d)uck under table: ')
if choic1 == 'H' or choic1 == 'h':
  print("Great. Jayden screams at you for....Not being Big Chungus?!")
  sys.exit()
else:
  print("Yay! Jayden stumbles off into the distance, shouting: OOF!")
print("Crawling out from under the table, you see a dog.")
choic2 = input('(P)et the dog or (S)neak away: ')
if choic2 == 'P' or choic2 == 'p':
  print("The dog barks and Jayden attac.")
  sys.exit()
else:
  print("The dog did not notice you.")
print("Creeping towards one of the rooms, Jayden lunges out.")
choic3 = input('(K)ick, (V)erbally abuse, or (P)unch: ')
if choic3 == 'V' or choic3 == 'v':
  print("Jayden cries and cries.")
else:
  print("Jayden screams at you for sooo long.")
  sys.exit()
print("Running from Jayden, you see light....")
time.sleep(1)
os.system("cls")
print("Jayden knocks you over to the side.")
choic4 = input('(Y)ell, (K)ick, or (P)uch: ')
if choic4 == 'K' or choic4 == 'k':
  print("Jayden screams in agony as you kick his weak spot.")
else:
  print("Jayden grabs you and destroys you.")
  sys.exit()
print("You see light again...")
choic5 = input('(T)rapdoor, (W)indow, (D)oor: ')
if choic5 == 'W' or choic5 == 'w':
  print("You escaped!")
else:
  print("You died.")


