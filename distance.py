const int buzzer = 8;
const int redLED = 9;
const int blueLED = 10;
const int echoPin = 11;
const int trigPin = 12;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(blueLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(buzzer, OUTPUT);

  Serial.begin(9600);
  Serial.println("Distance Measurement Ready");
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH, 30000);
  int distance = duration * 0.034 / 2;

  if (duration == 0) {
    Serial.println("Out of range");
    digitalWrite(blueLED, LOW);
    digitalWrite(redLED, LOW);
    noTone(buzzer);
  } else {
    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");

    digitalWrite(blueLED, LOW);
    digitalWrite(redLED, LOW);
    noTone(buzzer);

    if (distance <= 10) {
      Serial.println("VERY CLOSE!");
      digitalWrite(blueLED, HIGH);
      tone(buzzer, 1000);
      delay(500);
      noTone(buzzer);
    } else if (distance <= 50) {
      Serial.println("NEAR RANGE");
      digitalWrite(redLED, HIGH);
    } else {
      Serial.println("FAR RANGE");
    }
  }
  delay(100);
}
