#include <M5Core2.h>

void setup() {
  M5.begin();
  Serial2.begin(115200, SERIAL_8N1, 32, 33);
}

void loop() {
  M5.update();
  if ( M5.BtnA.wasPressed() ) {
    println_ext("Button A");
    M5.Lcd.fillScreen(MAGENTA);
  }  
  if ( M5.BtnB.wasPressed() ) {
    println_ext("Button B");
    M5.Lcd.fillScreen(CYAN);
  }

}

void println_ext(char* str){
  Serial2.write(str);
  M5.Lcd.setCursor(0, 5, 4);
  M5.Lcd.println(str);
}
