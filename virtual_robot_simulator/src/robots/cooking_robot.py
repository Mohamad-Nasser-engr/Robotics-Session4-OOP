from .base_robot import Robot

class CookingRobot(Robot):

    def __init__(self, name, battery_level,cooking_skill):
        super().__init__(name, battery_level)
        self.set_status("Idle")
        self.set_cooking_skill(cooking_skill)

    def work(self):
        if self.get_battery_level()<30:
            print("Not enough battery. Please charge the robot")
            self.set_status("Idle")
        else:
            self.battery_level = self.get_battery_level() - 30
            self.set_status("Working")
            print("Robot is Cooking")

    def set_cooking_skill(self, new_cooking_skill):
        self.cooking_skill = new_cooking_skill

    def get_cooking_skill(self):
        return self.cooking_skill