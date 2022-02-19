#Rock Paper & Scissors Game

from random import randint, random
from trace import Trace

def gamewin(comp, you):
   if comp==you:
    return None
   elif comp== 'r':
       if you=='s':
         return False
       if you=='p':
            return True
   elif comp== 's':
       if you=='p':
         return False
       if you=='r':
            return True
   elif comp== 'p':
       if you=='r':
         return False
       if you=='s':
            return True
randno=randint(1, 3)
if randno==1:
    comp = 'r'
elif randno==2:
    comp = 'p'
elif randno==3:
    comp = 's'

you= input("Your's Turn: Please Choose your turn-- Rock(r) Paper(p) or Scissors(s)?\n")

a= gamewin(comp, you)

print(f"computer choose {comp}")
print(f"you choose {you}")


if a==None:
    print("the game is tie!")
elif a==True:
    print("Congratualations: you win!")
else:
    print("You Lose!- Better Luck Next time")

    #Thank You 

    #Ankur Dey