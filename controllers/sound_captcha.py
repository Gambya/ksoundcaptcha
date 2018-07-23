from os import path, mkdir
from flask import jsonify
from flask_restful import Resource, request


from services.leitor_service import LeitorService


APP_ROOT = path.dirname(path.abspath(__file__))

class SoundCaptcha(Resource):
    def __init__(self):
        self.leitor_service = LeitorService()

    def post(self):
        solucao = ''
        target = path.join(APP_ROOT, 'tempfiles\\')

        if not path.isdir(target):
            mkdir(target)
        
        for file in request.files.getlist('audio'):
            filename = file.filename
            destino = path.join(target, filename)
            file.save(destino)
            solucao = self.leitor_service.ler_audio(destino)
            
        return jsonify({ 'solucao': solucao, 'status': 'SUCESSO' })