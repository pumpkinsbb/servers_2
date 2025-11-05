from flask import Flask,jsonify, request, Response
import xmltodict

app = Flask(__name__)

@app.route("/xml", methods = ["POST"])
def json_to_xml():
    json_data = request.get_json()
    json_data["person"]["name"]=json_data["person"]["name"]+f" "+json_data["person"]["surname"]
    del json_data["person"]["surname"]
    xml_data = xmltodict.unparse(json_data, pretty=True)
    return Response(xml_data, mimetype="application/xml", status=200)

@app.route("/json", methods = ["POST"])
def xml_to_json():
    xml_data = request.data
    json_data = xmltodict.parse(xml_data)
    json_data["person"]["name"] = json_data["person"]["name"] + f" " + json_data["person"]["surname"]
    del json_data["person"]["surname"]
    return jsonify(json_data)

if __name__ == "__main__":
    app.run(port= 5001)