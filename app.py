from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    return render_template('base.html')

# sio = socketio.Server()
# app = socketio.WSGIApp(sio, static_files={
#    '/': './public/'
#})
if __name__ == '__main__':
    socketio.run(app)
  

# @sio.event
# def connect(sid, environ):
#     print(sid, 'connected')


# @sio.event
# def disconnect(sid):
#     print(sid, 'disconnected')
