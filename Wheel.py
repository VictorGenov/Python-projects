import random as rd

class Enemy():
    def __init__(self,health,atack):
        self.health = health
        self.atack = atack
    def be_atacked(self,atack):
        self.health -= self.atack
        

zombie = Enemy(rd.randint(100,999),rd.randint(10,63))
print(zombie.health)
zombie.be_atacked(2)
print(zombie.health)
ghost = Enemy(rd.randint(100,999),rd.randint(10,63))
print(ghost.atack)

hits = 0 
while True:
    if zombie.health <= 0 and ghost.health <= 0:
        print("This was a good fight betwen real monster and spirit gind monster nether zombie nor ghost won. I betere run I a bout to be etean!!!!!!")
        break
    if zombie.health <= 0:
        print(f"Ghost wins the game with healths {ghost.health}")
        break
    if ghost.health <= 0:
        print(f"Zombie wins the game with healths left {zombie.health}")
        break
    zombie.be_atacked(ghost.atack)
    ghost.be_atacked(zombie)
    hits += 1
    print(hits,zombie.health,ghost.health)
    
