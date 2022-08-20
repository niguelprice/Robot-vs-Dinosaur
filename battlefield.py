from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot('robot')
        self.dinosaur = Dinosaur('trex',50)
    
    
    def run_game (self):
        print(f'dinosaur health: {self.dinosaur.health}')
        print(f'robot attacks dinosaur, and the dinosaur health is now:')
        self.robot.attack(self.dinosaur.health)
        print(f'robot health: {self.robot.robot_health}')
        print(f'dinosaur attacks robot, and the robot health is now:')
        self.dinosaur.attack(self.robot.robot_health)
        print(f'dinosaur has won')
        
        
        

       
        
      



        






