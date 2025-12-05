#!/usr/bin/env python3
import sys
import debugpy

# RobotPy's CLI entrypoint lives here
from robotpy.__main__ import main as robotpy_main


def main() -> None:
    # Start debug server *first*
    debugpy.listen(("localhost", 5678))
    print("Waiting for VS Code debugger on port 5678...", file=sys.stderr)
    debugpy.wait_for_client()

    robotpy_argv = ["robotpy", "sim", *sys.argv[1:]]

    sys.argv = robotpy_argv

    robotpy_main()


if __name__ == "__main__":
    main()
