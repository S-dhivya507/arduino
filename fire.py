const int buzzer = 8;
const int ledClose = 9;
const int ledDistant = 10;
const int ledNone = 11;

void setup() {
  Serial.begin(9600);
  pinMode(buzzer, OUTPUT);
  pinMode(ledClose, OUTPUT);
  pinMode(ledDistant, OUTPUT);
  pinMode(ledNone, OUTPUT);
  Serial.println("Fire Alarm Ready");
}

void loop() {
  int flame = analogRead(A0);
  digitalWrite(ledClose, LOW);
  digitalWrite(ledDistant, LOW);
  digitalWrite(ledNone, LOW);
  noTone(buzzer);

  if (flame < 200) {
    Serial.println("Close Fire");
    digitalWrite(ledClose, HIGH);
    tone(buzzer, 1000);
    delay(500);
    noTone(buzzer);
  } else if (flame < 500) {
    Serial.println("** Distant Fire **");
    digitalWrite(ledDistant, HIGH);
  } else {
    Serial.println("No Fire");
    digitalWrite(ledNone, HIGH);
  }

  delay(500);
}
