Processing commands through 'run.py' will make it so that
the cmd shell will not close once a command finishes after a double-click or right-click run
(of Python scripts, Python wheel package installs, and other things after registry modifications)!

Before importing registry updates with regedit...
1. Drop 'run.py' in C:\
2. Drop 'runpy.bat' in a directory that is watched by the PATH environment variable (like System32)
(optionally) Install the Python Launcher, which helps with interpreting shebang lines at the top
             of Python script files.
3. Modify run.py to work with your currently installed versions of Python.

Then check to make sure everything is in order...
