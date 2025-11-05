#include "DHT.h"
#define DHTPIN 12
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

const int buzzer = 8;
const int ledError = 9;
const int ledHighTemp = 10;
const int ledNormal = 11;

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(buzzer, OUTPUT);
  pinMode(ledError, OUTPUT);
  pinMode(ledHighTemp, OUTPUT);
  pinMode(ledNormal, OUTPUT);
  Serial.println("Climate Monitoring Ready");
}

void loop() {
  digitalWrite(ledError, LOW);
  digitalWrite(ledHighTemp, LOW);
  digitalWrite(ledNormal, LOW);
  noTone(buzzer);
  delay(2000);

  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Sensor Error!");
    digitalWrite(ledError, HIGH);
    delay(1000);
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print("% Temp: ");
  Serial.print(t);
  Serial.println("°C");

  if (t > 29) {
    Serial.println("HIGH TEMP ALERT!");
    digitalWrite(ledHighTemp, HIGH);
    tone(buzzer, 1000);
    delay(500);
    noTone(buzzer);
  } else {
    Serial.println("Normal Climate");
    digitalWrite(ledNormal, HIGH);
  }

  delay(1000);
}