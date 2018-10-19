# KSoundCaptcha     [![Build Status](https://travis-ci.org/Gambya/ksoundcaptcha.svg?branch=master)](https://travis-ci.org/Gambya/ksoundcaptcha)  [![Coverage Status](https://coveralls.io/repos/github/Gambya/ksoundcaptcha/badge.svg?branch=master)](https://coveralls.io/github/Gambya/ksoundcaptcha?branch=master)
Api restful que soluciona captchas de audio.

## Pré-requesitos

* aniso8601==3.0.2
* astroid==2.0.1
* click==6.7
* colorama==0.3.9
* Flask==1.0.2
* Flask-RESTful==0.3.6
* isort==4.3.4
* itsdangerous==0.24
* Jinja2==2.10
* lazy-object-proxy==1.3.1
* MarkupSafe==1.0
* mccabe==0.6.1
* PyAudio==0.2.11
* pytz==2018.5
* six==1.11.0
* SpeechRecognition==3.8.1
* typed-ast==1.1.0
* Werkzeug==0.14.1
* wrapt==1.10.11
* gunicorn==19.9.0

## Instalar Api Web
Clonar projeto:
``` 
# git clone https://github.com/Gambya/ksoundcaptcha.git
```
Instalar dependencias:
```
# pip install -r requirements.txt
```

## Rodar servidor web
Não recomendado para rodar em produção na forma a seguir.
Para produção verificar na documentação do flask.

[Documentação - Deploy Flask](http://flask.pocoo.org/docs/0.12/deploying/)

Para debug:
```
# cd ksoundcaptcha
# python -m flask run
or
# python app.py
```

Em produção:
```
# cd ksoundcaptcha
# gunicorn app:app -b localhost:8000
```

## Exemplos de Requisição
### Python (módulo requests)
``` python
import requests
response = requests.post('127.0.0.1:5000/resolvercaptcha', files={'audio': ('audio0.wav', open('<caminho_arquivo>/audio0.wav', 'rb'), 'multipart/form-data')})

response.json()
```

### Postman

[postman1]: https://i.stack.imgur.com/kFxyI.jpg "Nova Versão"
[postman2]: https://i.stack.imgur.com/AYtMA.png "Versão Anterior"
[postman3]: https://i.stack.imgur.com/LiTtB.jpg "Versão Antiga"

Nova Versão

![alt text][postman1]

Versão Anterior

![alt text][postman2]

Versão Antiga

![alt text][postman3]


### Objeto de retorno
```
{ 'solucao' : '<resolução_captcha>', 'status' : 'SUCESSO' }
{'error' : '<msg de erro>', 'solucao' : '', 'status' : 'ERROR' }
```
