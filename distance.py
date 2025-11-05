#define echoPin 3 
#define trigPin 2 
long duration; 
int distance; 
const int buzzer = 8;
const int light = 13;
const int light2 = 12;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT); 
  pinMode(buzzer, OUTPUT); 
  pinMode(light, OUTPUT);
  pinMode(light2, OUTPUT);
  Serial.begin(9600); 

  Serial.println("Annamalai University BE CSE 2022");
  Serial.println("Distance Measure Program");
}

void loop() {
  // Trigger the ultrasonic pulse
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure the echo time
  duration = pulseIn(echoPin, HIGH);

  // Convert time to distance
  distance = duration * 0.034 / 2;

  // Display distance
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Default: LEDs off
  digitalWrite(light, LOW);
  digitalWrite(light2, LOW);
  noTone(buzzer);

  // Decision logic
  if (distance <= 10) {
    Serial.println("Very Close");
    digitalWrite(light, HIGH);
    tone(buzzer, 1000);
    delay(500);
  }
  else if (distance > 10 && distance <= 50) {
    Serial.println("Near Range");
    digitalWrite(light2, HIGH);
    delay(500);
  }
  else {
    Serial.println("Far Range");
  }

  delay(500); // small delay for stable reading
}