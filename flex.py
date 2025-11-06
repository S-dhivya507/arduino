const int flexPin = A0;
const int ledPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Flex Sensor Ready");
}

void loop() {
  int value = analogRead(flexPin);
  Serial.print("Flex Value: ");
  Serial.println(value);

  if (value > 890) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }

  delay(100);
}