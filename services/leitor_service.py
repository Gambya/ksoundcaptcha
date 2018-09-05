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
    
    def __limpar_ruidos(self, path_arq:str):
        ip = wave.open('C:\\Users\\anagha\\Documents\\Python Scripts\\a1.wav', 'r')

        op = wave.open('C:\\Users\\anagha\\Documents\\Python Scripts\\r_1.wav', 'w')
        op.setparams(ip.getparams())

        for i in range(ip.getnframes()):
        iframes = ip.readframes(1)
        amp = int(binascii.hexlify(iframes))
        if amp > 32767:
            amp = 65535 - int(binascii.hexlify(iframes))#-ve
            print(amp)
        else:
            amp = int(binascii.hexlify(iframes))#+ve
            print(amp)
        if amp < 2000:
            #make it zero
            final_frame = '\x00\x00'
        else:
            #Keep the frame 
            final_frame = iframe
        op.writeframes(final_frame)
        op.close()
        ip.close()