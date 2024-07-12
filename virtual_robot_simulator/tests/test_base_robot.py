import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from robots.base_robot import Robot

class TestRobot(Robot):
    def work(self):
        # Implement the abstract method for testing purposes
        pass

class TestRobotClass(unittest.TestCase):
    def setUp(self):
        self.robot = TestRobot("TestBot", 50)

    def test_initialization(self):
        self.assertEqual(self.robot.get_name(), "TestBot")
        self.assertEqual(self.robot.get_battery_level(), 50)
        self.assertEqual(self.robot.get_status(), "Idle")

    def test_charge(self):
        self.robot.charge()
        self.assertEqual(self.robot.get_battery_level(), 100)
        self.assertEqual(self.robot.get_status(), "Charging")

    def test_set_and_get_status(self):
        self.robot.set_status("Working")
        self.assertEqual(self.robot.get_status(), "Working")

    def test_set_and_get_name(self):
        self.robot.set_name("NewName")
        self.assertEqual(self.robot.get_name(), "NewName")

    def test_set_battery_level(self):
        self.robot.set_battery_level(150)
        self.assertEqual(self.robot.get_battery_level(), 100)
        self.robot.set_battery_level(-10)
        self.assertEqual(self.robot.get_battery_level(), 0)
        self.robot.set_battery_level(50)
        self.assertEqual(self.robot.get_battery_level(), 50)

    def test_report_status(self):
        self.robot.set_status("Working")
        with self.assertLogs(level='INFO') as log:
            self.robot.report_status()
            self.assertIn("The robot's current status is: Working", log.output[0])

if __name__ == '__main__':
    unittest.main()