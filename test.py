import dotenv
import os
import datetime

# Python 2 import
from xmlrpclib import Server

try:
    PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
    dotenv.load_dotenv(os.path.join(PROJECT_PATH, ".env"))
except Exception:
    pass

def save(line, minutes, measured_at):
    print line, minutes, measured_at
    pass

DEV_KEY = os.environ.get('DEV_KEY')

s1 = Server('http://muovi.roma.it/ws/xml/autenticazione/1')
s2 = Server('http://muovi.roma.it/ws/xml/paline/7')

token = s1.autenticazione.Accedi(DEV_KEY, '')

now = datetime.datetime.utcnow()
rome_now = now + datetime.timedelta(hours=2)

res = s2.paline.Previsioni(token, '71427', 'it')
for p in res['risposta']['primi_per_palina']:
    print 'Arrivi: ', len(p)
    for a in p['arrivi']:
        line = a['linea']
        if 'nessun_autobus' in a:
            minutes = None
        else:
            minutes = a['tempo_attesa']
            
        save(line, minutes, rome_now)
