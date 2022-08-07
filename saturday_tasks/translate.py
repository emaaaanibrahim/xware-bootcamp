from ctypes.wintypes import WORD
from xml.dom import WrongDocumentErr


def pig_latin (text):
    say = ''
    words=text.split()
    for word in words :
        texts=word[1:]+word[0]+'ay'+' '
        say+=texts
    return say
print(pig_latin('fox fox'))
