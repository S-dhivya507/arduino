// 🌿 Fully Calibrated Soil Moisture Monitoring with Pump & LEDs

// Pin Definitions
const int buzzer = 11;
const int redLED = 13;     // Dry soil indicator
const int yellowLED = 10;  // Humid soil indicator
const int greenLED = 12;   // Wet soil indicator
const int pump = 9;        // Relay / pump
const int sensorPin = A0;  // Soil moisture sensor

// Thresholds (calibrate these with your soil)
const int SENSOR_DISCONNECTED_LOW = 10;   // Sensor not in soil (too low)
const int SENSOR_DISCONNECTED_HIGH = 1020; // Sensor not in soil (too high)
const int DRY_THRESHOLD = 650;            // Sensor value ≥ 650 → Dry
const int HUMID_THRESHOLD = 350;          // 350 ≤ Sensor value < 650 → Humid
// Wet: Sensor value < HUMID_THRESHOLD

void setup() {
  pinMode(sensorPin, INPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(pump, OUTPUT);

  Serial.begin(9600);
  Serial.println("Annamalai University BE CSE 2022");
  Serial.println("Soil Moisture Program (No LCD)");
  Serial.println("Calibrated thresholds: Dry ≥650, Humid 350-649, Wet <350");
}

void loop() {
  int sensorValue = analogRead(sensorPin);
  float moisture = 100 - ((sensorValue / 1023.0) * 100.0);

  Serial.print("Moisture: ");
  Serial.print(moisture, 1);
  Serial.print("% | Raw Value: ");
  Serial.println(sensorValue);
  Serial.println("----------");

  if (sensorValue <= SENSOR_DISCONNECTED_LOW || sensorValue >= SENSOR_DISCONNECTED_HIGH) {
    Serial.println("⚠️ Sensor not in soil or disconnected");
    allOff();
  }
  else if (sensorValue >= DRY_THRESHOLD) {  // Dry soil
    Serial.println("🌵 DRY SOIL - Pump ON");
    digitalWrite(redLED, HIGH);
    digitalWrite(yellowLED, LOW);
    digitalWrite(greenLED, LOW);
    tone(buzzer, 1000);        // Continuous beep
    digitalWrite(pump, HIGH);  // Pump ON
  }
  else if (sensorValue >= HUMID_THRESHOLD && sensorValue < DRY_THRESHOLD) { // Humid soil
    Serial.println("🌱 HUMID SOIL - Pump OFF");
    digitalWrite(redLED, LOW);
    digitalWrite(yellowLED, HIGH);
    digitalWrite(greenLED, LOW);
    noTone(buzzer);
    digitalWrite(pump, LOW);
  }
  else { // Wet soil
    Serial.println("💧 WET SOIL - Pump OFF");
    digitalWrite(redLED, LOW);
    digitalWrite(yellowLED, LOW);
    digitalWrite(greenLED, HIGH);
    noTone(buzzer);
    digitalWrite(pump, LOW);
  }

  delay(1000); // Loop every 1 second
}

// Function to turn everything OFF
void allOff() {
  digitalWrite(redLED, LOW);
  digitalWrite(yellowLED, LOW);
  digitalWrite(greenLED, LOW);
  digitalWrite(pump, LOW);
  noTone(buzzer);
}