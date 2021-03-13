import flask
from threading import Thread
import subprocess
import time

app = flask.Flask('')

@app.route('/')
def home():
    return "Your bot is alive!  All is running well!"

def run():
  app.run(host="0.0.0.0", port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()
