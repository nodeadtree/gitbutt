import subprocess
import datetime


message = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
subprocess.run(['git', 'commit', '-a', '-m', message])
subprocess.run(['git', 'push', 'origin', 'master'])
