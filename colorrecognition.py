const int s0 = 8, s1 = 9, s2 = 10, s3 = 11, out = 12;

void setup() {
  pinMode(s0, OUTPUT);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(out, INPUT);

  Serial.begin(9600);
  digitalWrite(s0, HIGH);
  digitalWrite(s1, HIGH);
  Serial.println("Color Recognition Ready");
}

void loop() {
  digitalWrite(s2, LOW);
  digitalWrite(s3, LOW);
  Serial.print("Red = ");
  readColor();

  digitalWrite(s2, LOW);
  digitalWrite(s3, HIGH);
  Serial.print("Blue = ");
  readColor();

  digitalWrite(s2, HIGH);
  digitalWrite(s3, HIGH);
  Serial.print("Green = ");
  readColor();

  Serial.println();
  delay(2000);
}

void readColor() {
  long d = pulseIn(out, LOW, 30000);
  if (d == 0)
    Serial.print("NoSignal");
  else
    Serial.print(d);

  Serial.print("\t");
  delay(1000);
}
