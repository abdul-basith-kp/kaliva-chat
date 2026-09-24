

from flask import Flask, render_template, redirect, request, session, url_for
from flask_socketio import SocketIO, emit

from validators.general_validator import GeneralValidator
from validators.user_validator import UserValidator
from utils.hash_manager import HashManager
from database import Database
from repositories.user_repository import UserRepo
from repositories.message_repository import MessageRepo
from managers.user_manager import UserManager
from managers.message_manager import MessageManager

gv = GeneralValidator()
uv = UserValidator(gv)
hm = HashManager()

db = Database()
ur = UserRepo(db)
mr = MessageRepo(db)
um = UserManager(ur, uv, hm, gv)
mm = MessageManager(mr)

app = Flask(__name__)
app.secret_key = '1234567897653243467768'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        password = data.get('password')
      
        if not name or not password:
            return {
                'success': False,
                'message': 'input cannot be empty'
            }

        try:
            um.login_user(name, password)
            session['name'] = name
            return{
                'success': True,
                'redirect': '/home'
            }
        except Exception as e:
            return {
                'success': False,
                'message': str(e)
            }

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get("name")
        password = data.get("password")

        if not name or not password:
            return {
                'success': False,
                'message': 'input cannot be empty'
            }
    
        try:
            um.create_user(name, password)
            session['name'] = name
            return {
                'success': True,
                'redirect': '/home'
            }
        
        except Exception as e:
         
            return {
                'success': False,
                'message': str(e)
            }

    return render_template('register.html')

@app.route('/home')
def home():
    if not session.get('name'):
        return render_template('register.html')
    return render_template('home.html')

@app.route('/get-messages')
def get_messages():
    messages =  mm.get_messages()
    return messages

@app.route('/current-user')
def current_user():
    return um.get_user_by_name(session.get('name'))


@socketio.on('connect')
def connect():
    emit('connected', f"{session.get('name')} connected", broadcast=True)
    
@socketio.on('disconnect')
def connect():
    emit('disconnected', f"{session.get('name')} disconnected", broadcast=True)

@socketio.on('send-message')
def send_message(message):
    
    user_id = um.get_user_by_name(session.get('name'))['user_id']

    try:
        mm.create_message(user_id, message)
        emit('message-created', 
            {
                'user_id': user_id,
                'name': session.get('name'),
                'message': message
            },
            broadcast=True)
    except Exception as e:
        emit('error', f'{str(e)}')
   
if __name__ == '__main__':
    socketio.run(
        app=app,
        host='0.0.0.0',
        debug=True,
        port=5000
    )