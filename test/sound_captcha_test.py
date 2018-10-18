from unittest import TestCase
import requests


from controllers.sound_captcha import SoundCaptcha


class TestSoundCaptcha(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.sound_captcha = SoundCaptcha()

    def test_post(self):
        response = requests.post('http://127.0.0.1:5000/resolvercaptcha', files={'audio': ('audio0.wav', open(r'test/audio/audio0.wav', 'rb'), 'multipart/form-data')})
        self.assertEqual({'solucao': 'fivn11', 'status': 'SUCESSO'}, response.json())