# shell_emulator.py

from pyxtermjs import TerminalNamespace
import pexpect
import pyte

# create a PTY-backed terminal namespace for Flask
terminal_ns = TerminalNamespace()

def spawn_shell():
    """Spawn a bash shell under pexpect, attach to xterm.js frontend."""
    child = pexpect.spawnu('/bin/bash', echo=False)
    # wrap child in pyte Screen for parsing
    screen = pyte.Screen(80, 24)
    stream = pyte.Stream(screen)
    return child, screen, stream

def process_input(child, stream, data):
    """Send keystrokes from browser to bash, update screen buffer."""
    child.send(data)
    # read available output
    output = child.read_nonblocking(size=1024, timeout=0.1)
    stream.feed(output)
    return screen.display
