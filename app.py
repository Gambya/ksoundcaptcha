from flask import Flask
from flask_restful import Resource, Api


from controllers.sound_captcha import SoundCaptcha


myapp = Flask(__name__)
api = Api(myapp)

api.add_resource(SoundCaptcha, '/resolvercaptcha')
# comentario
if __name__=='__main__':
    myapp.run()