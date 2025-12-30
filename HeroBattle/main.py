from Enemy import *
from Zombie import *
from Ogre import *

ogre = Ogre(20, 3)
zombie = Zombie(10, 1)

print(f"{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do {zombie.attack_damage} damage")
print(f"{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do {ogre.attack_damage} damage")

zombie.talk()
ogre.talk()