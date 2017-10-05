import subprocess
import datetime
import os
import time
time.sleep(30)
path = os.path.dirname(os.path.realpath(__file__)) + '/gitbutt.py'
message = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
with open(path, 'r') as f:
    doc = f.readlines()
    doc[-1] = '#' + message
with open(path, 'w') as f:
    for i in doc:
        f.write(i)
subprocess.run(['git', 'commit', '-a', '-m', message])
subprocess.run(['git', 'push', 'origin', 'master'])
#2017-10-04 22:15:57