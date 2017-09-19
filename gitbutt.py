import subprocess
import datetime


message = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
with f as open('gitbutt.py', 'r'):
    doc = f.readlines()
    doc[-1] = '#' + message
    for i in doc:
        f.write(i)
subprocess.run(['git', 'commit', '-a', '-m', message])
subprocess.run(['git', 'push', 'origin', 'master'])
#2017-09-18 18:18:49