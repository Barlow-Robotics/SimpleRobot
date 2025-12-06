#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

# This import is here to improve unit-test shutdown behavior
# It must be done before importing anything that depends on
# the phoenix libraries.
import fix_tests as _  # noqa: E402, isort:skip


import commands2
import ntcore
import wpilib

import keymaps
import teleop
import utils
from robot_systems import RobotSystems


class Robot(wpilib.TimedRobot):
    def robotInit(self) -> None:
        # The command scheduler is responsible for dispatching commands
        # while the robot is running. `self.scheduler.run()` must be called
        # periodically -- this happens in `robotPeriod` below.
        self.scheduler = commands2.CommandScheduler.getInstance()

        # It is important to be able to make errors observable via stored logs
        # and network tables.
        self.log = utils.LocalLogger("Robot")
        self.nt = ntcore.NetworkTableInstance.getDefault()

        # Robot systems encapsulate different subsystems and their commands.
        self.robot_systems = RobotSystems()

        self.robot_systems.init()

        # Keymaps define which physical buttoms correspond to different logical
        # actions on the robot.
        self.keymaps = keymaps.RobotKeymaps()

        # Set up teleop controls, which bind the buttons to the commands of the
        # robot systems.
        #
        # NOTE: Some teams choose to put this inside of `teleopInit`, but that
        # teleopInit runs EVERY time you switch back to teleop mode, leading to
        # duplicate bindings. By putting this here in `robotInit`, we ensure
        # that the bindings are only set up once. If we move it to teleopInit,
        # we need to make sure to clear all existing bindings first.
        wpilib.DriverStation.silenceJoystickConnectionWarning(True)
        teleop.setup_controls(self.robot_systems, self.keymaps)

    def robotPeriodic(self):
        try:
            # This will run any commands that were scheduled by sensing or
            # button presses.
            self.scheduler.run()
        except Exception as e:
            self.log.error(str(e))
            self.nt.getTable("errors").putString("command scheduler", str(e))

    def autonomousPeriodic(self) -> None:
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
