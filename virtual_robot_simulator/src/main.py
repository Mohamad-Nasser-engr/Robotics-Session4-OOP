from robots.base_robot import Robot
from robots.cleaning_robot import CleaningRobot
from robots.cooking_robot import CookingRobot
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

robot1 = Robot("normal", 110)
robot2 = CleaningRobot("clean", -88, "Vaccum")
robot3 = CookingRobot("Chef", 75,"expert")

print(robot1.get_battery_level())
print(robot2.get_battery_level())
print(robot3.get_battery_level())

print()
robot2.report_status()
robot2.work()
robot2.report_status()
robot2.charge()
robot2.report_status()
print(robot2.get_battery_level())
robot2.work()
robot2.work()
robot2.work()
robot2.work()
robot2.work()
robot2.report_status()
print(robot2.get_battery_level())
robot2.work()

print()
robot3.report_status()
robot3.work()
robot3.report_status()
print(robot3.get_battery_level())
robot3.charge()
robot3.report_status()
print(robot3.get_battery_level())


