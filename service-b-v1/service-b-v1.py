from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)

@app.route('/test')
def test():
    return "<b>[Test]service-b:v1</b> is called★<br /><br />"

@app.route('/b')
def b():
    req = requests.get("http://service-c.default.svc.cluster.local:9000/c")
    return "<b>service-b:v1</b> is called ▶<br /><br />" + req.text

@app.route('/b/c')
def bc():
    req = requests.get("http://service-c.default.svc.cluster.local:9000/c")
    return "<b>service-b:v1</b> is called ▶<br /><br />" + req.text

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9000, debug=False)

