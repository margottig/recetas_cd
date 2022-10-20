from flask import Flask

app = Flask(__name__)
app.secret_key = "llavesecreta de sesion"
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER