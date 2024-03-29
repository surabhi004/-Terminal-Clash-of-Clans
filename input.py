"""Defining input class."""
import sys
import termios
import tty
import signal


class Get:
    """Class to get input."""

    def __call__(self):
        """Defining __call__."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class AlarmException(Exception):
    """Handling alarm exception."""
    pass


def alarmHandler(signum, frame):
    """Handling timeouts."""
    raise AlarmException


def exit_handler(signum, frame):
    exit(0)


def input_to(timeout=1.0):
    """Taking input from user."""
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    signal.signal(signal.SIGINT, exit_handler)

    try:
        text = Get()()
        signal.alarm(0)
        return text
    except AlarmException:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return None
