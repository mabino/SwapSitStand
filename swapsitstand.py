#!/usr/bin/env python3
import re
import sys
from subprocess import call, PIPE, CalledProcessError, check_output

standing = 'B7C4E432-5F60-47F4-93EE-583CA59C8A74'
sitting = '92A62516-4A5E-49C9-BD3A-3BCA692E539A'

arrangement_query = ["displayplacer","list"]

def print_exc(msg):
    print('exit code: {}'.format(msg.returncode))
    print('stdout: {}'.format(msg.output.decode(sys.getfilesystemencoding())))
    print('stderr: {}'.format(msg.stderr.decode(sys.getfilesystemencoding())))
 
try:
    current_arrangement_query = check_output(arrangement_query, stderr=PIPE)
except CalledProcessError as e:
	print_exc(e)
else:     
	current_arrangement_string = re.search(".*Persistent screen id: ([0-9A-Z-]+)", str(current_arrangement_query))
	current_primary_display = current_arrangement_string.groups()[0]
	
if current_primary_display == standing:
	switch_cmd = f'displayplacer "id:{standing} res:2560x1440 scaling:off origin:(0,0) degree:0" "id:{sitting} res:2560x1440 scaling:off origin:(2560,0) degree:0"'
else:
	switch_cmd = f'displayplacer "id:{sitting} res:2560x1440 scaling:off origin:(0,0) degree:0" "id:{standing} res:2560x1440 scaling:off origin:(-2560,0) degree:0"'

call(switch_cmd, shell=True)
