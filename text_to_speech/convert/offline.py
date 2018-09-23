"""
This module deals with offline conversion of text to speech using
pyttsx3 library
"""

import pyttsx3


class OfflineConversion(object):
    def __init__(self, text):
        self.__voice_id = "english+f2"
        self.__voice_rate = 150
        self.__voice_volume = 0.9
        self.__text = text

    def speak(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', self.__voice_rate)
        engine.setProperty('volume', self.__voice_volume)
        engine.setProperty('voice', self.__voice_id)
        engine.say(self.__text)
        engine.runAndWait()
        engine.stop()
