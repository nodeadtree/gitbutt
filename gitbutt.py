import subprocess
import datetime
import os
import time
# Copyright (c) 2018 Juniper Overbeck
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#time.sleep(30)
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
#2022-03-10 12:00:01