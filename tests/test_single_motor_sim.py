"""
Simulation-based tests for the SingleMotorSubsystem using pyfrc

These tests run the full robot simulation loop in headless mode, including:
- Robot periodic methods
- Command scheduler
- Simulated hardware updates

This allows us to schedule commands and read back actual values from the simulator.
"""

import pytest
from wpilib.simulation import JoystickSim

from keymaps import Controllers, SingleMotorKeymap
from robot_core import Robot


def test_motor_with_joystick_button(control, robot: Robot):
    """Test motor control via simulated joystick button press - the realistic way!"""

    with control.run_robot():
        subsystem = robot.robot_systems.single_motor
        phoenix_motor = subsystem.motor

        # Create a simulated operator joystick
        operator_joy = JoystickSim(Controllers.OPERATOR_PORT)

        # Run disabled briefly
        control.step_timing(seconds=0.02, autonomous=False, enabled=False)

        # Start teleop mode - this calls teleopInit which sets up button bindings
        control.step_timing(seconds=0.05, autonomous=False, enabled=True)

        # Press RUN
        operator_joy.setRawButton(SingleMotorKeymap.RUN_BUTTON_ID, True)

        # Step the simulation
        control.step_timing(seconds=0.1, autonomous=False, enabled=True)

        # Motor should now be running
        assert phoenix_motor.get_applied_output() == pytest.approx(4.0, abs=0.1)

        # Release RUN
        operator_joy.setRawButton(SingleMotorKeymap.RUN_BUTTON_ID, False)

        # Step the simulation
        control.step_timing(seconds=0.1, autonomous=False, enabled=True)

        # Motor should now be stopped
        assert phoenix_motor.get_applied_output() == pytest.approx(0.0, abs=0.1)
