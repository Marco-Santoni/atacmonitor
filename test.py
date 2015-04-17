import dotenv
import os
try:
  # Python 2 import
  from xmlrpclib import Server
except ImportError:
  # Python 3 import
  from xmlrpc.client import Server

try:
    PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
    dotenv.load_dotenv(os.path.join(PROJECT_PATH, ".env"))
except Exception:
    pass

DEV_KEY = os.environ.get('DEV_KEY')

s1 = Server('http://muovi.roma.it/ws/xml/autenticazione/1')
s2 = Server('http://muovi.roma.it/ws/xml/paline/7')

token = s1.autenticazione.Accedi(DEV_KEY, '')

res = s2.paline.Previsioni(token, '71427', 'it')
for a in res['risposta']['arrivi']:
    print a['linea']
