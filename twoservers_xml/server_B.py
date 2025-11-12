import json

from flask import Flask,jsonify, request, Response
import redis
import xmltodict

app = Flask(__name__)
def connect():
    return redis.Redis(
    host='localhost',
    port=6379,
    db=0
)

@app.route("/xml", methods = ["POST"])
def json_to_xml():
    json_data = request.get_json()
    json_data["person"]["name"]=json_data["person"]["name"]+f" "+json_data["person"]["surname"]
    del json_data["person"]["surname"]
    xml_data = xmltodict.unparse(json_data, pretty=True)
    r = connect()
    r.set("xml",xml_data )
    return Response(xml_data, mimetype="application/xml", status=200)

@app.route("/json", methods = ["POST"])
def xml_to_json():
    xml_data = request.data
    json_data = xmltodict.parse(xml_data)
    json_data["person"]["name"] = json_data["person"]["name"] + f" " + json_data["person"]["surname"]
    del json_data["person"]["surname"]
    r = connect()
    r.set("json", json.dumps(json_data))
    return jsonify(json_data)

@app.route("/getj", methods = ["GET"])
def get_data():
    key = request.args.get("key")
    r = connect()
    item = r.get(key)
    return item.decode()

@app.route("/del", methods = ["POST"])
def del_data():
    key = request.args.get("key")
    r = connect()
    r.delete(key)
    return jsonify({"message":"opsie"})

if __name__ == "__main__":
    app.run(port= 5001)