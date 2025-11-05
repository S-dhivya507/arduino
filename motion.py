const int buzzer = 8;
const int led = 9;
const int pirPin = 10;
bool motionDetected = false;
void setup() {
  Serial.begin(9600);
  pinMode(pirPin, INPUT);
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);
  Serial.println("Motion Detection Ready");
}
void loop() {
  int motion = digitalRead(pirPin);
  if (motion == HIGH) {
    if (!motionDetected) {
      Serial.println("Motion Detected");
      digitalWrite(led, HIGH);
      tone(buzzer, 1000);
      delay(500);
      noTone(buzzer);
      motionDetected = true;
    }
  } else {
    if (motionDetected) {
      Serial.println("Motion stopped!");
      digitalWrite(led, LOW);
      motionDetected = false;
    }
  }
  delay(100);
}