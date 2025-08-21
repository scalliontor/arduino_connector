const int outputPin = 12;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(outputPin, OUTPUT);

  Serial.begin(9600);
  
  Serial.println("Pin 12 Controller Ready. Send '1' for HIGH, '0' for LOW.");
}

void loop() {
  if (Serial.available() > 0) {
    
    char command = Serial.read();
    
    if (command == '1') {
      digitalWrite(LED_BUILTIN, HIGH); 
      digitalWrite(outputPin, HIGH); 
      Serial.println("Command '1' received. Pin 12 is HIGH.");
    }
    else if (command == '0') {
      digitalWrite(LED_BUILTIN, LOW);  
      digitalWrite(outputPin, LOW);  
      Serial.println("Command '0' received. Pin 12 is LOW.");
    }
  }
}