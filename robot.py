#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import wpilib

import teleop
from robot_systems import RobotSystems


class Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        """Robot initialization function"""
        self.robot = RobotSystems()

        self.robot.init()

        self.scheduler = commands2.CommandScheduler.getInstance()

    def robotPeriodic(self):
        try:
            self.scheduler.run()
        except Exception as e:
            self.log.error(e)
            self.nt.getTable("errors").putString("command scheduler", str(e))

    def autonomousPeriodic(self) -> None:
        pass

    def teleopInit(self):
        teleop.setup_controls(self.robot)

    def teleopPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
