from flask import Flask

app2 = Flask(__name__)

@app2.route('/')
def home():
    return 'Bu app2 uygulamasıdır.'

if __name__ == '__main__':
    app2.run(host='0.0.0.0', port=5001)

