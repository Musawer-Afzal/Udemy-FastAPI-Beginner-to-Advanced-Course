from Enemy import *

class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy = 'Zombie',
                        health_points = health_points,
                        attack_damage = attack_damage)
    
    def talk(self):
        print("*Gurgling...*")
    
    def spread_disease(self):
        print("This zombie is trying to spread infection")
