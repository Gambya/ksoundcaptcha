from os import path, remove
import wave
import sys


import binascii
import speech_recognition as sr


class LeitorService():
    def ler_audio(self, path_arq:str, language:str='pt') -> str:
        if path.isfile(path_arq):
            rec = sr.Recognizer()

            with sr.AudioFile(path_arq) as source:
                audio = rec.record(source)
            solucao = rec.recognize_google(audio, language=language)
            remove(path_arq)
        return solucao.strip()