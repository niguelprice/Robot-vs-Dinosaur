from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = 'robot'
        self.robot_health = 100
        self.active_weapon = 50
    
    def attack(self, dinosaur):
        dinosaur -= self.active_weapon
        print(dinosaur)
        
    

    
    