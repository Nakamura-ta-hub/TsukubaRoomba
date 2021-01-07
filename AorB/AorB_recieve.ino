#include <M5Stack.h>
#include <Wire.h>
#include <SPI.h>
HardwareSerial serial_ext(2);

void setup() {
  M5.begin();
  M5.Lcd.setTextSize(10);
  
  Serial.begin(115200);
  Serial2.begin(115200, SERIAL_8N1, 21, 22);
  M5.Lcd.print("----");
}
 
void loop() {
  if (Serial2.available()) {
    int inByte = Serial2.read();
    M5.Lcd.setCursor(20, 60);
    if(inByte == 'A') {
      M5.Lcd.setTextColor(BLACK, MAGENTA);
      Serial.println("A");
      M5.Lcd.fillScreen(MAGENTA);
      M5.Lcd.print("A");
    }
    if(inByte == 'B'){
      M5.Lcd.setTextColor(BLACK, CYAN);
      Serial.println("B");
      M5.Lcd.fillScreen(CYAN);
      M5.Lcd.print("B");
    }
  }
}
