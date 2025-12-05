from keymap import Keymap
from robot_systems import RobotSystems


def setup_controls(robot_systems: RobotSystems):
    # Use the hasattr pattern so that if we comment out this subsystem, the program doesn't crash

    # Set up key bindings for the "single_motor" subsystem
    if hasattr(robot_systems, "single_motor"):
        Keymap.SingleMotor.RUN.onTrue(
            #  When the RUN button is pressed, start the motor
            robot_systems.single_motor.cmd_start_motor,
        ).onFalse(
            # When the RUN button is released, stop the motor
            robot_systems.single_motor.cmd_stop_motor,
        )
