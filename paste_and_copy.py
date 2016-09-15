"""
This file has been written with by Serkan Erip (serkanerip) for get last copied text from clipboard and set the clipboard new text via Python 3.5.
Feel free to cloning, sharing, editing and committing some new examples.
I have tried to explain each part basicly as I can.
For communicating with me:
mail: serkanerip@gmail.com
github: github.com/serkanerip
"""

import subprocess
import platform

# variables
clipboards = ['xsel', 'xclip']
current_os = platform.system()
check_cmd = 'where' if platform.system() == 'Windows' else 'which'
osx_notify_sender_package = 'terminal-notifier'

def check_clipboards(): # check system is have it clipboards packages
    clipboard = ''
    for cp in clipboards:
        clipboard = cp if subprocess.call([check_cmd, cp],
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE) == 0 else ''
    return clipboard

def check_is_exists_notifysender_on_mac():
    return subprocess.call([check_cmd], osx_notify_sender_package,
                           stdout=subprocess.PIPE,
                           bufsize=0,
                           stderr=subprocess.PIPE) == 0

def execute_command(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, close_fds=True)
    result, err = p.communicate()
    if(err):
        raise Exception( err )
    else:
        return result.decode('utf-8')

def execute_pasting_the_translate(command, translated_text):
    p = subprocess.Popen(command, stdin=subprocess.PIPE, close_fds=True)
    p.communicate(input=translated_text.encode('utf-8'))
    p.stdin.close()

def paste_the_translate_to_clipboard(translated_text): # set the translated text to clipboard last copy
    if (current_os == 'Linux'):
        return paste_onclipboard_linux(translated_text)
    elif (current_os == 'Darwin'):
        return paste_onclipboard_osx(translated_text)
    else:
        raise Exception('Operating system cannot defined.')

def paste_onclipboard_linux(translated_text):
    clipboard = check_clipboards()
    if (clipboard == ''):
        print("You need install xclip or xsel package on your linux system")
        exit()
    else:
        if (clipboard == 'xsel'):
            return execute_pasting_the_translate(['xsel', '-b', '-i'], translated_text)
        else:
            return execute_pasting_the_translate(['xclip', '-selection', 'c'], translated_text)

def get_currentcopy_linux():
    clipboard = check_clipboards()
    if (clipboard == ''):
        print("You need install xclip or xsel package on your linux system")
        exit()
    else:
        if (clipboard == 'xsel'):
            return execute_command(['xsel', '-b', '-o'])
        else:
            return execute_command(['xclip', '-selection', 'c', '-o'])

def paste_onclipboard_osx(translated_text):
    return execute_pasting_the_translate(['pbcopy', 'w'])

def get_currentcopy_osx():
    return execute_command(['pbpaste', 'r'])

def last_copy():
    if(current_os == 'Linux'):
        return get_currentcopy_linux()
    elif( current_os == 'Darwin' ):
        return get_currentcopy_osx()
    else:
        raise Exception('Operating system cannot defined.')



