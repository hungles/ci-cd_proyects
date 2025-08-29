# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello CI/CD World!"})

@app.route("/sum", methods=["POST"])
def sum_numbers():
    data = request.get_json()
    result = data["a"] + data["b"]
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#Debo ejecutarse denuevo el pipeline porque he cambiado el path de ejecucion