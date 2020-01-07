from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hurray! We are up and running!!!"

if __name__ == '__main__':
    app.run()
