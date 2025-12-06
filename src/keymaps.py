from commands2.button import CommandJoystick


# Define our controllers as module-level singletons
# These are safe to share because they just wrap WPILib Joystick objects
class Controllers:
    OPERATOR_PORT = 0
    DRIVER_PORT = 1

    OPERATOR = CommandJoystick(OPERATOR_PORT)
    DRIVER = CommandJoystick(DRIVER_PORT)


# KeyMaps are the only place where we should hard-code things related to button-ids.
# Think of this as giving names to the different buttons we want to use. This way, to
# change which actual button does an action, this is the only place we have to modify
# things.
#
# NOTE: Even though it would be a little less verbose to make these static class-members,
# We don't do so because it interferes with running unit-tests which might create
# multiple robot instances in the same process.
class SingleMotorKeymap:
    RUN_BUTTON_ID = 1

    def __init__(self) -> None:
        # Button to run the single motor
        self.RUN = Controllers.OPERATOR.button(self.RUN_BUTTON_ID)


class RobotKeymaps:
    def __init__(self) -> None:
        # Keymaps for the single motor subsystem
        self.single_motor = SingleMotorKeymap()
