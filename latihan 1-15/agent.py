import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)
client.loop_start()

print("Agent hidup")

while True:
    suhu = random.uniform(25, 32)
    client.publish("kampus/pj/suhu", f"{suhu:.2f}")
    print("Kirim:", suhu)
    time.sleep(2)