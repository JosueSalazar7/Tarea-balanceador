from flask import Flask, redirect

servidor4 = Flask(__name__)

@servidor4.route('/')
def hola():
    return redirect('https://www.viki.com')

if __name__ == '__main__':
    servidor4.run(host='0.0.0.0')
