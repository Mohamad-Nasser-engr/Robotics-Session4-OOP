from abc import abstractmethod
import logging

class Robot:
    def __init__(self,name,battery_level):
        self.set_name(name)
        self.set_battery_level(battery_level)
        self.set_status("Idle")

    def charge(self):
        self.battery_level=100
        self.set_status("Charging")

    @abstractmethod
    def work(self):
        None

    def report_status(self):
         logging.info(f"The robot's current status is: {self.get_status()}")

    def set_status(self, new_status):
        self.status = new_status

    def get_status(self):
        return self.status

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_battery_level(self, new_battery_level):
        if new_battery_level<0:
            self.battery_level =0
        elif new_battery_level>100:
            self.battery_level =100
        else:
            self.battery_level=new_battery_level

    def get_battery_level(self):
        return self.battery_level
    