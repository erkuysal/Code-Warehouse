#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include "DHT.h"


#define DHTPIN 2       
#define DHTTYPE DHT11  

DHT dht(DHTPIN, DHTTYPE);

#define LCD_ADDRESS 0x27
#define LCD_COLUMNS 16
#define LCD_ROWS 2
LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

float calculateDewPoint(float temperature, float humidity) {
    const float A = 17.27;
    const float B = 237.7;
    float alpha = ((A * temperature) / (B + temperature)) + log(humidity / 100.0);
    return (B * alpha) / (A - alpha);
}

// Function to calculate absolute humidity
float calculateAbsoluteHumidity(float temperature, float humidity) {
    const float Mw = 18.01534;  // Molar mass of water vapor (g/mol)
    const float R = 8.314472;   // Universal gas constant (J/(mol·K))
    float tempKelvin = temperature + 273.15;  // Convert temperature to Kelvin
    float saturationPressure = 6.1078 * pow(10, (7.5 * temperature) / (237.3 + temperature));
    float actualPressure = (humidity / 100.0) * saturationPressure;
    return (actualPressure * Mw) / (R * tempKelvin) * 1000; // Convert to g/m³
}

void setup() {
    Serial.begin(9600);
    Serial.println(F("DHT11 with Advanced Calculations"));

    dht.begin();

    lcd.init();
    lcd.backlight();
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Initializing...");
    delay(2000);
    lcd.clear();
}

void loop() {
    delay(2000);  // Wait 2 seconds between measurements

    // Read humidity and temperature
    float h = dht.readHumidity();
    float t = dht.readTemperature();

    // Check for sensor errors
    if (isnan(h) || isnan(t)) {
        Serial.println(F("Failed to read from DHT sensor!"));
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Sensor Error!");
        return;
    }

    // Calculate dew point and absolute humidity
    float dewPoint = calculateDewPoint(t, h);
    float absHumidity = calculateAbsoluteHumidity(t, h);

    // Print to Serial Monitor
    Serial.print(F("Humidity: "));
    Serial.print(h);
    Serial.print(F("%  Temperature: "));
    Serial.print(t);
    Serial.println(F("°C"));
    Serial.print(F("Dew Point: "));
    Serial.print(dewPoint);
    Serial.println(F("°C"));
    Serial.print(F("Abs. Humidity: "));
    Serial.print(absHumidity);
    Serial.println(F(" g/m³"));

    // Print to LCD
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("H:");
    lcd.print(h);
    lcd.print("% T:");
    lcd.print(t);
    lcd.print("C");

    lcd.setCursor(0, 1);
    lcd.print("DP:");
    lcd.print(dewPoint);
    lcd.print("C AH:");
    lcd.print(absHumidity, 1);
    lcd.print("g");
}