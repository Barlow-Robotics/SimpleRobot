#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpimath
import wpilib.drive
import wpimath.filter
import wpimath.controller
from robot_systems import Robot
import commands2



class _Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        """Robot initialization function"""
        self.controller = wpilib.XboxController(0)
        self.robot = Robot()

        self.cool_button_motorspin = commands2.button.JoystickButton(
            wpilib.Joystick(0), 1
        )

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
        self.cool_button_motorspin.onTrue(
            commands2.cmd.runOnce(self.robot.drivetrain.move_motor)
        ).onFalse(commands2.cmd.runOnce(self.robot.drivetrain.stop_motor))

    def teleopPeriodic(self) -> None:
        pass
 