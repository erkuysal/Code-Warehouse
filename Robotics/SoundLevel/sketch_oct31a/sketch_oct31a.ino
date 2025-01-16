int ledPin = 3;

void setup() {
  // pinMode(ledPin, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  int potentioMeter = analogRead(A0);  
  // analogRead()

  int pvmVal =  map(potentioMeter, 0, 1023, 0, 255);

  
  Serial.println((String)potentioMeter + " - " + pvmVal);
  analogWrite(ledPin, pvmVal);

  delay(10);

}


void FadeIn(){
  for(int i = 0; i <= 255; i++){
    analogWrite(ledPin, i);
    delay(2.5);
  }
}

void FadeOut(){
  for(int i = 255; i >= 0; i--){
    analogWrite(ledPin, i);
    delay(2.5);
  }
}