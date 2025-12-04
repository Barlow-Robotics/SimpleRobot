from toolkit.motors.ctre_motors import TalonConfig
from phoenix6.hardware import CANcoder


foc_active = False  # foc for TalonFX requires paid subscription

front_left_move_id: int = 1
front_left_turn_id: int = 2
front_left_encoder_port: CANcoder = CANcoder(20)
front_left_encoder_zeroed_pos: float = 0.4736328125
front_left_turn_inverted = False
front_left_move_inverted = False

MOVE_CONFIG = TalonConfig(
    0.11,
    0,
    0,
    kF=0.25,
    kA=0.15,
    kV=0.12,
    brake_mode=True,
    current_limit=50,
)