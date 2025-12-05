"""
This is a stub file to launch the robot code via robotpy.

See `src/robot_core.py` for the main robot code entry point.
"""

import wpilib

from robot_core import Robot


class _Robot(Robot):
    pass


if __name__ == "__main__":
    wpilib.run(_Robot)
