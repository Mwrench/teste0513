from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Mateus Quintela'

@app.route('/index.html')
def index():
    return 'index.html'

if __name__== '__main__':
    app.run()
