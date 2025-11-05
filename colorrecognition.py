#define s0 8 
#define s1 9
#define s2 10
#define s3 11
#define out 12

int data = 10; 

void setup() 
{
  pinMode(s0, OUTPUT); 
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(out, INPUT);

  Serial.begin(9600);

  // Set frequency scaling to 100% (HIGH-HIGH)
  digitalWrite(s0, HIGH); 
  digitalWrite(s1, HIGH); 
}

void loop() {
  // RED filter (LOW-LOW)
  digitalWrite(s2, LOW); 
  digitalWrite(s3, LOW);
  Serial.print("Red value= "); 
  GetData(); 

  // BLUE filter (LOW-HIGH)
  digitalWrite(s2, LOW);
  digitalWrite(s3, HIGH);
  Serial.print("Blue value= ");
  GetData();

  // GREEN filter (HIGH-HIGH)
  digitalWrite(s2, HIGH);
  digitalWrite(s3, HIGH);
  Serial.print("Green value= ");
  GetData();

  Serial.println();
  delay(2000);
}

void GetData() {
  data = pulseIn(out, LOW); // Measure duration of LOW pulse
  Serial.print(data); 
  Serial.print("\t"); 
  delay(20);
}
 colour recognition