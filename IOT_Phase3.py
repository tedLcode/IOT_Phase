import time
import random
import json
import paho.mqtt.client as mqtt

# Replace with your IoT sensor's unique identifier
sensor_id = "sensor123"

# MQTT broker settings (replace with your broker details)
broker_address = "mqtt.yourbroker.com"
broker_port = 1883
mqtt_topic = "noise_data"

def read_noise_level():
    # Simulate reading noise data from the sensor (replace with actual sensor code)
    return random.randint(40, 90)  # Simulated noise level (40-90 dB)

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(mqtt_topic)

def on_publish(client, userdata, mid):
    print("Data sent successfully.")

def send_noise_data(client, noise_level):
    data = {
        "sensor_id": sensor_id,
        "timestamp": int(time.time()),
        "noise_level": noise_level
    }
    payload = json.dumps(data)

    # Publish the data to the MQTT topic
    client.publish(mqtt_topic, payload)

# Create an MQTT client
client = mqtt.Client(sensor_id)
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Main loop to continuously read and send noise data
while True:
    try:
        noise_level = read_noise_level()  # Simulate reading noise data

        send_noise_data(client, noise_level)

        # Adjust the interval based on your requirements (e.g., every 10 seconds)
        time.sleep(10)

    except KeyboardInterrupt:
        print("Script terminated.")
        break

# Keep the script running
client.loop_forever()
