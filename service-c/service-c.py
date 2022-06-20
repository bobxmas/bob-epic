from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)

@app.route('/test')
def test():
    return "<b>[Test] service-a</b> is called★<br /><br />"

@app.route('/c')
def c():
    return "<b>service-a</b> is called★<br /><br />"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9000, debug=False)
