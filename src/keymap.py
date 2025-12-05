from commands2.button import CommandJoystick


# Define our controllers
class Controllers:
    OPERATOR = CommandJoystick(0)
    DRIVER = CommandJoystick(1)


# KeyMap is the only place where we should hard-code things related to button-ids
class Keymap:
    class SingleMotor:
        RUN = Controllers.OPERATOR.button(1)
