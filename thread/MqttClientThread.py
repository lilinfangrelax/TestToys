from PySide6.QtCore import QThread, Signal
import paho.mqtt.client as mqtt

class MqttClientThread(QThread):
    client_started = Signal(str)
    client_stopped = Signal()

    def __init__(self, parent=None, button_name=""):
        super().__init__(parent)
        self.button_name = button_name
        self.mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_message = self.on_message

    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code: {reason_code}")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("button/"+self.button_name)
    
    def publish(self, topic, payload):
        self.mqttc.publish(topic, payload)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic+": "+str(msg.payload))

    def run(self):
        self.client_started.emit("Client started")
        self.mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)
        self.mqttc.loop_forever()
        self.client_stopped.emit()