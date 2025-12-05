#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import wpilib
from commands2.button import CommandJoystick

from robot_systems import Robot


# TODO: This can get moved to keymap.py
class Controllers:
    OPERATOR = CommandJoystick(0)
    DRIVER = CommandJoystick(1)


# KeyMap is the only place where we should hard-code things related to button-ids
class Keymap:
    class SingleMotor:
        RUN = Controllers.OPERATOR.button(1)


class _Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        """Robot initialization function"""
        self.robot = Robot()

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
        # When we init teleop, connect the RUN key -> start/stop motor commands
        # Avoid creating commands here; do that in the subsystem
        Keymap.SingleMotor.RUN.onTrue(
            self.robot.single_motor.cmd_start_motor,
        ).onFalse(
            self.robot.single_motor.cmd_stop_motor,
        )

    def teleopPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(_Robot)
