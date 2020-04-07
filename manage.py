import uuid
from flask import Flask, request, json, Response
from flask_sqlalchemy import SQLAlchemy
from util import data
import settings

app = Flask(__name__)
app.config.from_object(settings)
db = SQLAlchemy(app)
path_prefix= "/flask"
app.register_blueprint(data, url_prefix=path_prefix)
if __name__ == '__main__':
    app.run()