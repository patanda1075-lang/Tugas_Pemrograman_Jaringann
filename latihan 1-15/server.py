from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
from datetime import datetime
import json

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

DATA_FILE = "data.json"

def simpan(data):
    with open(DATA_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")

def on_message(client, userdata, msg):
    suhu = msg.payload.decode()
    data = {"suhu": suhu, "waktu": str(datetime.now())}
    print("Diterima:", data)
    simpan(data)
    socketio.emit("suhu", data)

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.connect("broker.hivemq.com", 1883, 60)
mqttc.subscribe("kampus/pj/suhu")
mqttc.loop_start()

@app.route("/login", methods=["POST"])
def login():
    d = request.json
    if d["username"] == "admin" and d["password"] == "123":
        return jsonify({"status": "ok"})
    return jsonify({"status": "fail"})

if __name__ == "__main__":
    socketio.run(app, port=5000)