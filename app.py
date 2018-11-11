"""Beispiel mit Usern

Weitere Infos und ein ähnliches Beispiel unter:
https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm
"""
import flask_socketio
import sqlalchemy
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# turn the flask app into a socketio app
socketio = flask_socketio.SocketIO(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, password, email):
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


@socketio.on('newChatMessage', namespace='/test')  # Decorator to catch an event called "my event":
def broadcast_message(message):  # test_message() is the event callback function.
    print("Message: ", message)
    socketio.emit('newMessage', {'message': message}, namespace='/test')


@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    print('Client connected')


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('main.html')


@app.route("/data", methods=['GET'])
def data():
    random_data = [{"data": [49.9, 54.4], "name": "Tokyo"}, {"data": [42, 30.4], "name": "AC"}]
    return render_template('data.html', data=random_data)


@app.route("/time", methods=['GET'])
def timer():
    return render_template('timer.html')


@app.route("/loader", methods=['GET'])
def loader():
    return render_template('loader.html')


@app.route("/socket", methods=['GET'])
def socket():
    return render_template('socket.html')


@app.route("/users", methods=['GET'])
def usersget():
    return render_template('users.html', users=User.query.all())


@app.route("/users", methods=['POST'])
def userspost():
    user = User(request.form['password'], request.form['email'])
    try:
        db.session.add(user)
        db.session.commit()
        flash('Record was successfully added', category="success")
    except sqlalchemy.exc.IntegrityError:
        flash('Record could not be added, username already taken', category="error")
    return redirect(url_for('usersget'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host="127.0.0.1")
