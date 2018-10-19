from app import myapp


import unittest
from os import getcwd


class TestSoundCaptcha(unittest.TestCase):
    def setUp(self):
        app = myapp.test_client()
        
        data = dict({'audio':(open(fr'{getcwd()}\audio0.wav', 'rb'), r'audio0.wav'), 'language':'pt'})
        self.response = app.post('/resolvercaptcha', data=data, follow_redirects=True, content_type='multipart/form-data')

    def test_post(self):
        ''' Testando o código de retorno da requisição '''
        self.assertEqual(200, self.response.status_code)
    
    def test_json_response(self):
        ''' Testando o retorno da requisição '''
        self.assertEqual(dict({'solucao': 'fivn11', 'status': 'SUCESSO'}), self.response.json)

    def test_content_type(self):
        ''' Testando se o content type da resposta está correta '''
        self.assertIn('application/json', self.response.content_type)