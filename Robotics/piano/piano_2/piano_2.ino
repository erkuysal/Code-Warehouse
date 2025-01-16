#define PIN_1 A5
#define MAX_SAMPLE 100

void setup(){
  Serial.begin(9600);
}

void loop(){
    int total = 0;

  for(int i = 0; i <= MAX_SAMPLE; i++){
    int temp = analogRead(PIN_1);
    Serial.println(temp);
    delay(100);
    // total += temp;
  }

  //int avg = total / MAX_SAMPLE;

 // Serial.println(avg);
}