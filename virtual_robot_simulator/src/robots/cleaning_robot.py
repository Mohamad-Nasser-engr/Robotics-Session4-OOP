from .base_robot import Robot

class CleaningRobot(Robot):

    def __init__(self, name, battery_level, cleaning_tool):
        super().__init__(name, battery_level)
        self.set_status("Idle")
        self.set_cleaning_tool(cleaning_tool)

    def work(self):
        if self.get_battery_level() < 20:
            print("Not enough battery. Please charge the robot")
            self.set_status("Idle")
        else:
            self.battery_level = self.get_battery_level() - 20
            self.set_status("Working")
            print("Robot is Cleaning")

    def set_cleaning_tool(self, new_cleaning_tool):
        self.cleaning_tool = new_cleaning_tool

    def get_cleaning_tool(self):
        return self.cleaning_tool