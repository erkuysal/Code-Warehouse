#include <CapacitiveSensor.h>

// Notes
#define NOTE_C4  262
#define NOTE_D4  294
#define NOTE_E4  330
#define NOTE_F4  349
#define NOTE_G4  392
#define NOTE_A4  440
#define NOTE_B4  494

// Common send pin
const int sendPin = 2;

// Initialize capacitive sensors (Common Send Pin, Unique Receive Pin)
CapacitiveSensor csC = CapacitiveSensor(sendPin, 3); // C4
CapacitiveSensor csD = CapacitiveSensor(sendPin, 4); // D4
CapacitiveSensor csE = CapacitiveSensor(sendPin, 5); // E4
CapacitiveSensor csF = CapacitiveSensor(sendPin, 6); // F4
CapacitiveSensor csG = CapacitiveSensor(sendPin, 7); // G4
CapacitiveSensor csA = CapacitiveSensor(sendPin, 8); // A4
CapacitiveSensor csB = CapacitiveSensor(sendPin, 9); // B4

const int buzzerPin = 10; // Moved to pin 10 to avoid conflict

// Threshold for touch detection
long threshold = 1000; // Adjust this value if needed

void setup() {
  // Initialize serial communication at 9600 baud
  Serial.begin(9600);

  // Disable autocalibration to prevent baseline drift
  csC.set_CS_AutocaL_Millis(0xFFFFFFFF);
  csD.set_CS_AutocaL_Millis(0xFFFFFFFF);
  csE.set_CS_AutocaL_Millis(0xFFFFFFFF);
  csF.set_CS_AutocaL_Millis(0xFFFFFFFF);
  csG.set_CS_AutocaL_Millis(0xFFFFFFFF);
  csA.set_CS_AutocaL_Millis(0xFFFFFFFF);
  csB.set_CS_AutocaL_Millis(0xFFFFFFFF);
}

void loop() {
  // Read capacitive sensors
  long valC = csC.capacitiveSensor(30);
  long valD = csD.capacitiveSensor(30);
  long valE = csE.capacitiveSensor(30);
  long valF = csF.capacitiveSensor(30);
  long valG = csG.capacitiveSensor(30);
  long valA = csA.capacitiveSensor(30);
  long valB = csB.capacitiveSensor(30);

  // Print sensor values to Serial Monitor
  Serial.print("C: "); Serial.print(valC);
  Serial.print("\tD: "); Serial.print(valD);
  Serial.print("\tE: "); Serial.print(valE);
  Serial.print("\tF: "); Serial.print(valF);
  Serial.print("\tG: "); Serial.print(valG);
  Serial.print("\tA: "); Serial.print(valA);
  Serial.print("\tB: "); Serial.println(valB);

  delay(200); // Delay to make the output readable
}