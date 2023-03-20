from random import randint, random


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

msg="Hello, you want to play BlackJack ? Enter 'y' if yes ,'n' if no:"



def randomCards(c,u):
      
      #To deal cards to players
      
      for i in range(2):
          x=randint(0,13)
          c.append(cards[x])
      for i in range(2):
          x=randint(0,13)
          u.append(cards[x])
      
 
 
def BlackJack(l):
      
      ##To verify if a player has a blackjack
      
      if 10 in l and 11 in l:
            return True
      else:
            return False
               
          

def start():
      #To start the game
      answer=input(msg)
      if answer=="y":
            play()
      else:
            if answer=="n":
                  print("ok !")
            else:
                  start()
                
  
  
def calcul(l):
      res=0
      for i in range(len(l)):
            res=res+l[i]
      return res
          
 
 


def dealing(computer,user):
      if BlackJack(computer):
            print("You lose")
            return True
      elif BlackJack(user):
            print("You Won !!CONGRATS!!")
            return True
            
      else:
            resul=calcul(user)
            if (resul>21):
                  if 11 in user:
                        if (resul-10)<21:
                              i=user.index(11)
                              user[i]=1
                              reponse=input("do you want another card ?? enter 'y' if yes ,'n' if no")
                              if reponse=="n":
                                    if calcul(computer)<resul-10:
                                          print("you lose")
                                          return True
                                          
                                    else:
                                          print("you won")
                                          return True
                                          
                              else:
                                    return False
                        else:
                              print("you lose")
                  else:
                        print("you lose")
            else:
                  reponse=input("do you want another card ?? enter 'y' if yes ,'n' if no ")
                  if reponse=="y":
                        return False
                  else:
                        if(calcul(user)<calcul(computer)and calcul(computer)<21):
                              print("you lose")
                        elif (calcul(user)>calcul(computer)):
                              print("you won Congrats !!!")
                        else:
                              ("draw")
                              
                        
                  

  
          
def play():
      computer=[]
      user=[]
      print(logo)
      randomCards(computer,user)
      print("you have :",user[0],"  ",user[1])
      print("the computer has ",computer[0])
      
      
      
      if (dealing(computer,user)==False):
            x=randint(0,13)
            y=randint(0,13)
            computer.append(cards[x])
            user.append(cards[y])
            dealing(computer,user)
                                               
                         
start()
    

    
    
    
