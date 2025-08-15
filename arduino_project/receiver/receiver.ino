// File: receiver/receiver.ino

void setup() {
  Serial.begin(9600);
  Serial.println("Arduino is ready to receive messages.");
}

void loop() {
  if (Serial.available() > 0) {
    String message = Serial.readStringUntil('\n');
    Serial.print("Arduino received: ");
    Serial.println(message);
  }
}