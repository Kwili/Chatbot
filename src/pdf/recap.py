from src.pdf.generator import create_pdf
import uuid
import os

env = os.getenv('PYTHON_ENV', 'dev')

default_dir = './reports/' if env == 'dev' else '/tmp/reports/'
default_url = 'http://localhost:8080/' if env == 'dev' else 'http://kwili-bot.herokuapp.com/'


def ensure_path(path):
	if not os.path.exists(path):
		os.makedirs(path)


ensure_path(default_dir)


def find_emergencies(user, req):
    return True

def send_recap(user, req):
    session_id = str(uuid.uuid1())
    create_pdf(default_dir, session_id, user.profile)
    ret_string = 'Your recap is available here: ' if user.lang == 'en' else 'Votre compte rendu est disponible ici: '
    return ret_string + default_url + 'reports/' + session_id + '.'
