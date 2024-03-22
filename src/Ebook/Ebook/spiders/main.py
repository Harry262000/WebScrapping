import sys
import subprocess

python = sys.executable
subprocess.check_call(
    [python, '-m', 'pip', 'install', 'requests'],
    stdout=subprocess.DEVNULL
)
