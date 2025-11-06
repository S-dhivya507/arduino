const int fsrPin = A0;

void setup() {
  Serial.begin(9600);
  Serial.println("Force Sensor Ready");
}

void loop() {
  int reading = analogRead(fsrPin);
  Serial.print("Force Reading: ");
  Serial.print(reading);

  if (reading < 10)
    Serial.println(" → No Pressure");
  else if (reading < 200)
    Serial.println(" → Light Touch");
  else if (reading < 500)
    Serial.println(" → Light Pressure");
  else if (reading < 800)
    Serial.println(" → Medium Pressure");
  else
    Serial.println(" → Heavy Pressure");

  delay(200);
}