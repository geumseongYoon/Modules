import os
import sys

euid = os.geteuid()
if euid != 0:
    print("Script not started as root. Running sudo..")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # the next line replaces the currently-running process with the sudo
    # os.execlpe('sudo', *args)
else:
    print('Running. Your euid is', euid)
