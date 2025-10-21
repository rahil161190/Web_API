from flask import Flask

app = Flask(__name__)
@app.route('/',methods=['GET'])
# by default method = get
def hello_world():
    return 'Hello, World!'

@app.route('/panda')
def hello_panda():
    return 'Hello, Panda!'
@app.route('/ping')
def hello_ping():
    return 'Hi i am json reply'