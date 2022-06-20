from flask import Flask
from flask import jsonify
import requests
import json
import os
import sys
import urllib.request
client_id='Kar9EeMSFFOvtYvTMfDe'
client_secret='q8L0Fr19MW'

app = Flask(__name__)

@app.route('/test')
def test():
    return "<b>[Test]service-b:v2</b> is called★<br /><br />"

@app.route('/b')
def b():
    encText = urllib.parse.quote("반갑습니다")
    data = 'source=ko&target=en&text='+encText
    url = 'https://openapi.naver.com/v1/papago/n2mt'
    request = urllib.request.Request(url)
    request.add_header('X-Naver-Client-Id', client_id)
    request.add_header('X-Naver-Client-Secret', client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        response_json = json.loads(response_body.decode('utf-8'))
        print(response_json)
        response_text = "<b>service-b:v2</b> is called ▶<br /><br /><b>Naver Papago API is called: 반갑습니다 ▶ "+response_json['message']['result']['translatedText']+"★"
        return response_text
    else:
        return 'Error Code:' + rescode

@app.route('/b/c')
def bc():
    req = requests.get("http://service-c.default.svc.cluster.local:9000/c")
    return "<b>service-b:v2</b> is called★<br /><br />" + req.text

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9000, debug=False)

