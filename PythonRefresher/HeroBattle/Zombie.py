from Enemy import *
import random

class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy = 'Zombie',
                        health_points = health_points,
                        attack_damage = attack_damage)
    
    def talk(self):
        print("*Gurgling...*")
    
    def spread_disease(self):
        print("This zombie is trying to spread infection")

    def special_attack(self):
        did_special_attack_work = random.randint(0, 1)
        if did_special_attack_work == 1:
            self.health_points += 2
            print("Zombie regenerated 2HP!")