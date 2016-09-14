"""
This file has been written with by Serkan Erip (serkanerip) for get last copied text from clipboard via Python 3.5.
Feel free to cloning, sharing, editing and committing some new examples.
I have tried to explain each part basicly as I can.
For communicating with me:
mail: serkanerip@gmail.com
github: github.com/serkanerip
"""

import subprocess
clipboards = ['xsel', 'xclip']

def check_clipboards(): # check system is have it clipboards packages
    clipboard = ''
    for cp in clipboards:
        clipboard = cp if subprocess.call(['which', cp],
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE) == 0 else ''
    return clipboard

def execute_command(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, close_fds=True)
    result, err = p.communicate()
    if(err):
        raise Exception( err )
    else:
        return result.decode('utf-8')

def last_copy():
    clipboard = check_clipboards()
    if(clipboard == ''):
        print("You need install xclip or xsel package on your linux system")
        exit()
    else:
        if(clipboard == 'xsel'):
            return execute_command(['xsel', '-b', '-o'])
        else:
            return execute_command(['xclip', '-selection', 'c' ,'-o'])

