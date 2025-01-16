#include <Servo.h>

Servo myServo;

int potPin = A0;

void setup() {
  Serial.begin(9600);
  myServo.attach(6);
}

void loop() {
  int potValue = analogRead(potPin);
  int degree = map(potValue, 0, 1023, 0, 175);

  myServo.write(degree);
}