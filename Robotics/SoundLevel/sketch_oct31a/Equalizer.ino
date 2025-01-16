const int ledPins[5] = {3, 5, 6, 9, 10}; // PWM-capable LED pins
const int potPin = A0; // Potentiometer pin
const int micPin = A1; // Microphone pin

int sensitivity = 0;
int micValue = 0;

void setup() {
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  // Read potentiometer value for sensitivity adjustment
  sensitivity = analogRead(potPin);
  int threshold = map(sensitivity, 0, 1023, 50, 400); // Map sensitivity

  // Read microphone input
  micValue = analogRead(micPin);

  // Determine dimness levels for LEDs based on sound level and sensitivity
  int dimLevel = map(micValue, 0, threshold, 0, 255); // Map to 0-255 for PWM
  
  // Calculate the brightness for each LED
  for (int i = 0; i < 5; i++) {
    int brightness = map(micValue, threshold * i / 5, threshold * (i + 1) / 5, 0, 255);
    brightness = constrain(brightness, 0, 255); // Ensure brightness is within 0-255 range
    analogWrite(ledPins[i], brightness);
  }

  // Delay for stability
  delay(50);
}