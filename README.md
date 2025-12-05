# Simple Robot

## Installation
All dependencies are managed via [uv](https://docs.astral.sh/uv/).
- Please follow the [installation instructions](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

Once you have uv installed, you only need to run:
```
uv run robotpy sync
```

## Best Practices
We use ruff for formatting code. This ensures consistency and minimizes white-space-related conflicts.
 - VS Code should be set up to install the `charliemarsh.ruff` extension and will format-on-save.
 - Before pushing code always format using ruff:
    ```
    uv run ruff format
    ```

## Useful commands

### Start the simulator
In VS Code:
- Command > Run Task > Simulate Robot Code

From the Terminal:
```
uv run robotpy sim
```

## Important files
- `robot.py`
    - Main entry point for the program. This is high-level scaffoling that initiates the robot, sets up the scheduler, logging, etc.
- `config.py`
    - Constants related to physical robot configuration like CAN ids and gear ratios
- `robot_systems.py`
    - Container that defines all of subsystems that belong to the robot.
- `keymap.py`
    - Defines the mapping between PHYSICAL joysticks and buttons and LOGICAL behaviors. This is the only place we should talk about buttons by id.
- `teleop.py`
    - This file wires up LOGICAL behaviors to sub-system commands.
- `subsystem/`
    - Directory where we store the different subsystem definitions.