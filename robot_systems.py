from subsystem import SingleMotorSubsystem


class RobotSystems:
    def __init__(self):
        # Create any sub-system we want to add.
        # We use defensive programming in the places we reference this to make
        # it possible to comment out this subsystem if we don't want to use it.
        self.single_motor = SingleMotorSubsystem()

    def init(self):
        if hasattr(self, "single_motor"):
            self.single_motor.init()
