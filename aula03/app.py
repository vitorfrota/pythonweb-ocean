from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

posts = [
  {
    "title": "Meu primeiro post",
    "body": "Este post é zica",
    "author": "Vitor",
    "created": datetime(2022,8,17)
  }
]

@app.route('/')
def index():
  return render_template("index.html", posts=posts)