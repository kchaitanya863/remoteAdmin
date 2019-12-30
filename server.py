from flask import Flask
import subprocess

from flask import request
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'remoteAdmin is up and running!'

#run as /run?cmd=curl -s ifconfig.co
@app.route('/run')
def run():
    cmd = request.args.get('cmd')
    try:
        output = subprocess.getoutput(cmd)
    except Exception as e:
        output = str(e)
    print(output)
    return str(output)

if __name__ == '__main__':
    app.run()