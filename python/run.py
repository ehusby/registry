#!/usr/bin/env python2

# Created by Erik Husby

import argparse
import re
import sys
from subprocess import call
from traceback import print_exc


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('command_tokens', help="Tokens of the command to be executed.", nargs="+")
        args = parser.parse_args()

        print "--- PROCESSING PYTHON SCRIPT WITH {} ---".format(sys.argv[0].upper())

        scriptFile = None
        if args.command_tokens[0].endswith('.py'):
            # The first argument to run.py is a Python script!
            scriptFile = args.command_tokens[0]
            interp_path = None


            PY_LAUNCHER_SHEBANG_REGEX = "#! *((/usr/local/bin/|/usr/bin/)|/usr/bin/env +)([^ ]+)$"

            PY_LAUNCHER = r'C:\Users\husby036\AppData\Local\Programs\Python\Launcher\py.exe'

            PYTHON2_7 = r'C:\Python27\python.exe'
            PYTHON3_6 = r'C:\Python36\python.exe'
            PYPY2_5   = r'C:\pypy2-v5.4.1-win32'
            # PYTHON2_7_ARCGIS_10_4 = r'C:\Python27\ArcGIS10.4\python.exe'
            # PYTHON3_4_ARCPRO      = r'C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe'

            PYTHON_DEFAULT = PY_LAUNCHER

            INTERP_ID_DICT = {}
            for key in ('python2', 'python2.7'):
                INTERP_ID_DICT[key] = PYTHON2_7
            for key in ('python3', 'python3.6'):
                INTERP_ID_DICT[key] = PYTHON3_6
            for key in ('pypy', 'pypy2', 'pypy2.5'):
                INTERP_ID_DICT[key] = PYPY2_5
            # for key in ('python-arcgis', 'python2.7-arc'):
            #     INTERP_ID_DICT[key] = PYTHON2_7_ARCGIS_10_4
            # for key in ('python-arcpro', 'python3.6-arc'):
            #     INTERP_ID_DICT[key] = PYTHON3_4_ARCPRO


            pybang_pattern = re.compile(PY_LAUNCHER_SHEBANG_REGEX)
            scriptFP = open(scriptFile)
            shebang = scriptFP.readline().strip()
            result = re.match(pybang_pattern, shebang)
            if result is not None:
                # There is a shebang at the top of the script!!
                inpterp_id = result.group(3)
                if inpterp_id in INTERP_ID_DICT:
                    interp_path = INTERP_ID_DICT[inpterp_id]
                else:
                    print "Invalid Python interpreter id specified in shebang at top of Python script"
                    sys.exit(1)
            else:
                print "WARNING: Python Launcher-style shebang not detected by run.py"
                print "Using default Python interpreter: {}".format(PYTHON_DEFAULT)
                interp_path = PYTHON_DEFAULT

            args.command_tokens.insert(0, interp_path)

        command = ' '.join(args.command_tokens)
        print r"Running: {}".format(command)
        print
        call(command)

    except:
        print_exc()

    finally:
        raw_input("\n--- PROGRAM EXECUTION IS FINISHED, PRESS [ENTER] ---")



if __name__ == '__main__':
    main()
