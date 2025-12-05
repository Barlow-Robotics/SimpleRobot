import commands2

import config
from toolkit.motors.ctre_motors import TalonFX
from toolkit.subsystem import Subsystem


class SingleMotorSubsystem(Subsystem):  # single motor class
    # order of operations: __init__() called first, then init() called later.
    def __init__(self):
        super().__init__()

        # Declare the motor as a TalonFX
        self.motor = TalonFX(
            config.front_left_move_id,
            foc=config.foc_active,
            config=config.MOVE_CONFIG,
            inverted=config.front_left_move_inverted,
        )

        # Create subsystem commands to start/stop the motor
        self.cmd_start_motor = commands2.cmd.runOnce(
            self.start_motor,
        )
        self.cmd_stop_motor = commands2.cmd.runOnce(
            self.stop_motor,
        )

    def start_motor(self):
        print("START MOTOR")
        self.motor.set_voltage(4)  # set speed of motor to 0.1 volts

    def stop_motor(self):
        print("STOP MOTOR")
        self.motor.set_voltage(0)

    def init(self):
        print("Initializing single motor subsystem")
        self.motor.init()  # IMPORTANT: HAVE TO INIT ALL TALONFX MOTORS OR ERROR AND DO IT HERE NOT AT __init__


class Robot:
    def __init__(self):
        self.single_motor = SingleMotorSubsystem()

    def init(self):
        self.single_motor.init()
