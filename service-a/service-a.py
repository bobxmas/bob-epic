from flask import Flask
from flask import jsonify
import requests
import json

app = Flask(__name__)

@app.route('/api/login/<username>/<password>')
def login(username, password):
    url = "http://keycloak.keycloak-system.svc.cluster.local/realms/bob-realm/protocol/openid-connect/token"
    data = {
        "client_id": "grafana",
        "client_secret": "1zNboHpRw7Is94yWRh16dUefYwjAOw1P",
        "username": username,
        "password": password,
        "grant_type": "password"
    }
    res_keycloak = requests.post(url, data=data)
    res_json_obj = json.loads(res_keycloak.text)
    res = {'access_token': res_json_obj["access_token"]}
    return jsonify(res)

@app.route('/api/a')
def a():
    print('called /a')
    res = {'data': '<b>service-a</b> is called★'}
    return jsonify(res)

@app.route('/api/a/b/test')
def abtest():
    print('called /a/b/test')
    req = requests.get("http://service-b.default.svc.cluster.local:9000/test")
    res = {'data': '<b>service-a</b> is called ▶<br /><br />' + req.text}
    return jsonify(res)

@app.route('/api/a/b')
def ab():
    print('called /a/b')
    req = requests.get("http://service-b.default.svc.cluster.local:9000/b")
    res = {'data': '<b>service-a</b> is called ▶<br /><br />' + req.text}
    return jsonify(res)

@app.route('/api/a/b/v1/test')
def abv1test():
    print('called /a/b/v1/test')
    req = requests.get("http://service-b-v1.default.svc.cluster.local:9000/test")
    res = {'data': '<b>service-a</b> is called ▶<br /><br />' + req.text}
    return jsonify(res)

@app.route('/api/a/b/v1')
def abv1():
    print('called /a/b/v1')
    req = requests.get("http://service-b-v1.default.svc.cluster.local:9000/b")
    res = {'data': '<b>service-a</b> is called ▶<br /><br />' + req.text}
    return jsonify(res)

@app.route('/api/a/b/v2')
def abv2():
    print('called /a/b/v2')
    req = requests.get("http://service-b-v2.default.svc.cluster.local:9000/b")
    res = {'data': '<b>service-a</b> is called ▶<br /><br />' + req.text}
    return jsonify(res)

@app.route('/api/a/c')
def ac():
    print('called /a/c')
    req = requests.get("http://service-c.default.svc.cluster.local:9000/c")
    res = {'data': '<b>service-a</b> is called ▶<br /><br />' + req.text}
    return jsonify(res)

if __name__=='__main__':
    # app.run(host='0.0.0.0', port=9000, debug=False)
    app.run(host='127.0.0.1', port=9000, debug=False)