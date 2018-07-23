from os import path
import speech_recognition as sr


class LeitorService():
    def ler_audio(self, path_arq:str) -> str:
        if path.isfile(path_arq):
            rec = sr.Recognizer()

            with sr.AudioFile(path_arq) as source:
                audio = rec.record(source)
        return rec.recognize_google(audio, language="pt")
        