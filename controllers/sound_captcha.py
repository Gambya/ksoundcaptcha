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
        try:
            language = request.form.get('language')
            audio = request.files.getlist('audio')
            if len(audio) <= 0:
                return jsonify({'error' : 'lista de audio vazia.', 'solucao' : '', 'status' : 'ERROR' })
                
            for file in audio:
                filename = file.filename
                destino = path.join(target, filename)
                file.save(destino)
            if language:
                solucao = self.leitor_service.ler_audio(destino, language=language)
            else
                solucao = self.leitor_service.ler_audio(destino)
        except Exception as error:
            return jsonify({ 'error' : str(error), 'solucao': '', 'status': 'ERROR' })
        return jsonify({ 'solucao': solucao, 'status': 'SUCESSO' })