import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from robots.cooking_robot import CookingRobot

class TestCookingRobot(unittest.TestCase):
    def setUp(self):
        self.robot = CookingRobot("CookerBot", 50, "intermediate")

    def test_initialization(self):
        self.assertEqual(self.robot.get_name(), "CookerBot")
        self.assertEqual(self.robot.get_battery_level(), 50)
        self.assertEqual(self.robot.get_status(), "Idle")
        self.assertEqual(self.robot.get_cooking_skill(), "intermediate")

    def test_work_with_sufficient_battery(self):
        self.robot.work()
        self.assertEqual(self.robot.get_battery_level(), 20)
        self.assertEqual(self.robot.get_status(), "Working")

    def test_work_with_insufficient_battery(self):
        self.robot.set_battery_level(20)
        self.robot.work()
        self.assertEqual(self.robot.get_battery_level(), 20)
        self.assertEqual(self.robot.get_status(), "Idle")

    def test_set_and_get_cooking_skill(self):
        self.robot.set_cooking_skill("expert")
        self.assertEqual(self.robot.get_cooking_skill(), "expert")

    def test_charge(self):
        self.robot.charge()
        self.assertEqual(self.robot.get_battery_level(), 100)
        self.assertEqual(self.robot.get_status(), "Charging")

    def test_set_and_get_status(self):
        self.robot.set_status("Working")
        self.assertEqual(self.robot.get_status(), "Working")

if __name__ == '__main__':
    unittest.main()
