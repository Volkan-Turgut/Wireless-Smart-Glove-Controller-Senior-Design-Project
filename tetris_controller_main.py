import paho.mqtt.client as mqtt
import pyautogui


# MQTT broker information
broker = "localhost"  # Replace with your MQTT broker address
port = 1883  # Replace with the MQTT broker port
topic = "my_topic"  # Replace with the MQTT topic you want to subscribe to

# Callback function when a connection is established with the MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(topic)
   
# Callback function when a message is received from the MQTT broker
def on_message(client, userdata, msg):
    
    message = msg.payload.decode("utf-8")  # Decode the payload using UTF-8 encoding
    print(message)
    if message=="1":
      pyautogui.press('down')
      print("asd")
    if message=="2":
        pyautogui.press('left')
    if message=="3":
        pyautogui.press('right')
    if message=="4":
        pyautogui.press('space')
    if message=="5":
        pyautogui.press('p')




# Create an MQTT client instance
client = mqtt.Client()

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker, port, 60)

# Start the MQTT network loop in a separate thread
client.loop_start()

# Keep the program running to receive messages
while True:
    pass
