import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from robots.cleaning_robot import CleaningRobot

class TestCleaningRobot(unittest.TestCase):
    def setUp(self):
        self.robot = CleaningRobot("CleanerBot", 50, "vacuum")

    def test_initialization(self):
        self.assertEqual(self.robot.get_name(), "CleanerBot")
        self.assertEqual(self.robot.get_battery_level(), 50)
        self.assertEqual(self.robot.get_status(), "Idle")
        self.assertEqual(self.robot.get_cleaning_tool(), "vacuum")

    def test_work_with_sufficient_battery(self):
        self.robot.work()
        self.assertEqual(self.robot.get_battery_level(), 30)
        self.assertEqual(self.robot.get_status(), "Working")

    def test_work_with_insufficient_battery(self):
        self.robot.set_battery_level(10)
        self.robot.work()
        self.assertEqual(self.robot.get_battery_level(), 10)
        self.assertEqual(self.robot.get_status(), "Idle")

    def test_set_and_get_cleaning_tool(self):
        self.robot.set_cleaning_tool("mop")
        self.assertEqual(self.robot.get_cleaning_tool(), "mop")

    def test_charge(self):
        self.robot.charge()
        self.assertEqual(self.robot.get_battery_level(), 100)
        self.assertEqual(self.robot.get_status(), "Charging")

    def test_set_and_get_status(self):
        self.robot.set_status("Working")
        self.assertEqual(self.robot.get_status(), "Working")

if __name__ == '__main__':
    unittest.main()


