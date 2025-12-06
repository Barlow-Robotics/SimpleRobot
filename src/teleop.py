from keymaps import RobotKeymaps
from robot_systems import RobotSystems


def setup_controls(robot_systems: RobotSystems, keymaps: RobotKeymaps):
    """
    Create button bindings between the mapped keys and robot commands.
    """

    # Set up key bindings for the "single_motor" subsystem
    if hasattr(robot_systems, "single_motor"):
        keymaps.single_motor.RUN.onTrue(
            #  When the RUN button is pressed, start the motor
            robot_systems.single_motor.cmd_start_motor,
        ).onFalse(
            # When the RUN button is released, stop the motor
            robot_systems.single_motor.cmd_stop_motor,
        )
