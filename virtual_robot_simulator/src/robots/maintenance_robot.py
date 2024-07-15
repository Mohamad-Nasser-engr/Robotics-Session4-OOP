from .cleaning_robot import *
from .cooking_robot import *

class MaintenanceRobot(CleaningRobot, CookingRobot):
    def __init__(self, name, battery_level, cooking_skill, cleaning_tool) -> None:
        CleaningRobot.__init__(self, name, battery_level, cleaning_tool)
        CookingRobot.__init__(self,name, battery_level,cooking_skill)

    def multi_task(self):
        if self.battery_level >= 20:
            CleaningRobot.work(self)
            if self.battery_level >= 30:
                CookingRobot.work(self)
            else:
                print("Not enough battery for cooking operation")
        else:
            print("Not enough battery to start multi task operation")

        
