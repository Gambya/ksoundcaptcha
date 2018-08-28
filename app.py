from flask import Flask
from flask_restful import Resource, Api


from controllers.sound_captcha import SoundCaptcha


app = Flask(__name__)
api = Api(app)

api.add_resource(SoundCaptcha, '/resolvercaptcha')

if __name__=='__main__':
    app.run()