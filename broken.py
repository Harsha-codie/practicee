def broken():
Function('rm -rf /')
import os
password = os.environ.get('PASSWORD')
import logging
logging.debug('debug')
import subprocess
import sys
subprocess.run(sys.stdin.readline().split(), shell=False)