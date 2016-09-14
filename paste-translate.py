"""
This file has been written with by Serkan Erip (serkanerip) for translate copied texts from clipboard via Python 3.5.
Feel free to cloning, sharing, editing and committing some new examples.
I have tried to explain each part basicly as I can.
For communicating with me:
mail: serkanerip@gmail.com
github: github.com/serkanerip
"""

import get_last_copy
import translate
import os

# variables
last_copied_text = get_last_copy.last_copy()
linux_command = 'nofity-send'
notify_title = 'Paste-translate app'
source_language = 'en' # translate from english
target_language = 'tr' # transalte to turkish

def check_last_copied_text(): # if just haven't any text on the clip board send informing notification
    test_text = last_copied_text
    if(test_text.replace(' ', '') == ''):
        send_notification("Clipboard haven't any copied text yet")
        exit()

def send_notification(notif): # sending translated text via linux notify-send command
    os.system('notify-send "{}" "{}"'.format(notify_title, notif))

if __name__ == '__main__':
    check_last_copied_text()
    translate_obj = translate.Translate(word=last_copied_text, source='en', target='tr')
    text_translate = translate_obj.translate()
    message = '\nTranslated from {} to {}\n\nTranslated text = {}\n\nTranslate = {}\n'
    message = message.format( source_language, target_language, last_copied_text, text_translate )
    send_notification(message)




