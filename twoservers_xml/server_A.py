from flask import Flask, jsonify, request, Response
import requests

app = Flask(__name__)

@app.route("/xml", methods = ["POST"])
def json_to_xml():
    json_data = request.get_json()
    answer = requests.post("http://127.0.0.1:5001/xml", json = json_data)
    return Response(answer.content, mimetype="application/xml", status=200)

@app.route("/json", methods = ["POST"])
def xml_to_json():
    xml_data = request.data.decode("utf-8")
    answer = requests.post("http://127.0.0.1:5001/json", data = xml_data)
    return jsonify(answer.json()), 200

if __name__ == "__main__":
    app.run(port= 5000)