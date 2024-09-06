#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// Replace with your network credentials
const char* ssid = "SCIENT-GUEST";
const char* password = "Guest@123";

// MQTT Broker
const char* mqtt_broker = "test.mosquitto.org";
const char* topic = "sensor/ir";
const int mqtt_port = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

// IR sensor pin
const int irPin = D1;

void setup() {
  Serial.begin(115200);

  pinMode(irPin, INPUT);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Set up MQTT client
  client.setServer(mqtt_broker, mqtt_port);

  // Connect to MQTT Broker
  while (!client.connected()) {
    String client_id = "esp8266-client-";
    client_id += String(WiFi.macAddress());

    if (client.connect(client_id.c_str())) {
      Serial.println("Connected to MQTT Broker!");
    } else {
      Serial.print("Failed to connect to MQTT Broker. State: ");
      Serial.println(client.state());
      delay(2000);
    }
  }
}

void loop() {
  // Read IR sensor
  int irState = digitalRead(irPin);

  // Publish sensor state
  if (irState == HIGH) {
    client.publish(topic, "1");  // Object detected
    Serial.println("IR sensor triggered: 1");
  } else {
    client.publish(topic, "0");  // No object detected
    Serial.println("IR sensor not triggered: 0");
  }

  // delay(200); // Send reading every 1 second
}
