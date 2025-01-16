#include <Wire.h>                // Include I2C communication library
#include <LiquidCrystal_I2C.h>   // Include I2C LCD library
#include <Servo.h>               // Include Servo library

// Initialize I2C LCD with the address 0x27 (adjust if needed)
LiquidCrystal_I2C lcd(0x27, 16, 2);

Servo myServo;           // Create Servo object
int servoPin = 3;        // PWM pin connected to the servo
int potPin = A0;         // Potentiometer pin
int angle = 0;           // Variable to store the servo angle

void setup() {
  Serial.begin(9600);      // Start Serial communication
  lcd.init();              // Initialize the LCD
  lcd.backlight();         // Turn on the backlight
  myServo.attach(servoPin); // Attach the servo to the specified pin
  
  lcd.setCursor(0, 0);
  lcd.print("Servo Control");
  delay(2000);             // Display welcome message for 2 seconds
  lcd.clear();
  
  lcd.setCursor(0, 0);
  lcd.print("Angle: ");
}

void loop() {
  // Read potentiometer value and map to angle
  int potValue = analogRead(potPin);
  int potAngle = map(potValue, 0, 1023, 0, 180);

  // Update angle if changed
  if (potAngle != angle) {
    angle = potAngle;
    myServo.write(angle); // Set the servo angle
    
    // Update LCD display
    lcd.setCursor(7, 0);
    lcd.print("    "); // Clear previous value
    lcd.setCursor(7, 0);
    lcd.print(angle);
  }

  // Send the current angle to serial for Python
  Serial.print("Current Angle: ");
  Serial.println(angle);

  // Check for serial input to set the angle manually
  if (Serial.available() > 0) {
    String inputData = Serial.readStringUntil('\n'); // Read angle data until newline
    inputData.trim(); // Remove any trailing or leading whitespace
    int newAngle = inputData.toInt(); // Convert input to integer

    if (newAngle >= 0 && newAngle <= 180) {
      angle = newAngle;
      myServo.write(angle); // Set the servo angle
      
      // Update LCD display
      lcd.setCursor(7, 0);
      lcd.print("    "); // Clear previous value
      lcd.setCursor(7, 0);
      lcd.print(angle);

      // Send confirmation back to serial
      Serial.print("Angle set to: ");
      Serial.println(angle);
    } else {
      Serial.println("Invalid angle. Enter a value between 0 and 180.");
    }
  }

  delay(100); // Adjust the delay as needed
}
