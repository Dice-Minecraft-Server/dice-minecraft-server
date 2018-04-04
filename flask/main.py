# -*- coding: utf8 -*-
from flask import Flask
from flask import render_template
from mcstatus import MinecraftServer
app = Flask(__name__)
def get_server_status():
    server = MinecraftServer.lookup("127.0.0.1:25565")
    status = server.status()
    return status
@app.route('/')
def index():
    status = get_server_status()
    return render_template('index.html', status=status)
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
