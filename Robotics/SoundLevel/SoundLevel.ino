const int potPin = A0;
const int micPin = A1;

const int ledPins[] = {3, 5, 6, 9, 10};

int sensitivity = 512;         // Default sensitivity
int soundLevel = 0;

void setup() {
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
  }

  // Startup light sequence: Turn each LED on and off sequentially
  for (int i = 0; i < 5; i++) {
    analogWrite(ledPins[i], 255); // Turn on LED
    delay(200);                   // Wait 200ms
    analogWrite(ledPins[i], 0);   // Turn off LED
  }

  // Blink all LEDs twice as a final check
  for (int j = 0; j < 2; j++) {
    for (int i = 0; i < 5; i++) {
      analogWrite(ledPins[i], 255); // Turn on all LEDs
    }
    delay(300);                     // Wait 300ms

    for (int i = 0; i < 5; i++) {
      analogWrite(ledPins[i], 0);   // Turn off all LEDs
    }
    delay(300);                     // Wait 300ms
  }

  Serial.begin(9600);
}

void loop() {
  // Dynamically set sensitivity using the potentiometer

  // map(value, fromLow, fromHigh, toLow, toHigh)
  sensitivity = map(analogRead(potPin), 0, 1023, 50, 800);

  // Read the current sound level
  soundLevel = analogRead(micPin);

  // Check if the sound level exceeds the sensitivity threshold
  if (soundLevel > sensitivity) {
    
    int scaledLevel = map(soundLevel, sensitivity, 1023, 1, 5);
    // int scaledLevel = map(soundLevel, sensitivity, 1023, 5, 1); // EXPERIMENTAL
    
    scaledLevel = constrain(scaledLevel, 1, 5); // Ensure within 1-5 range
    // scaledLevel = constrain(scaledLevel, 5, 1); // EXPERIMENTAL

    // Light up LEDs based on scaledLevel
    for (int i = 0; i < 5; i++) {
      if (i < scaledLevel) {
        analogWrite(ledPins[i], 0); // Turn off LED
      } else {
        analogWrite(ledPins[i], 255);   // Turn on LED
      }
    }
  } else {
    // Turn off all LEDs if sound is below the sensitivity threshold
    for (int i = 0; i < 5; i++) {
      analogWrite(ledPins[i], 0);
    }
  }

  // Debugging output for sound level and sensitivity
  Serial.print("Sound Level: ");
  Serial.print(soundLevel);
  Serial.print(" | Sensitivity: ");
  Serial.println(sensitivity);

  delay(5); // Small delay for stability
}