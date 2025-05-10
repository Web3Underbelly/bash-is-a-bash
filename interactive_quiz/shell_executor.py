# Module to execute and test Bash commands

import subprocess

def execute_bash_command(command):
    """Execute a Bash command and return its output."""
    # TODO: Add security checks and error handling
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr
import subprocess

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()
