#define BLYNK_PRINT Serial

#include <Adafruit_NeoPixel.h>
#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include <M5Core2.h>
#include "SD.h"
#define BLYNK_PRINT Serial

char auth[] = "e4hgw2eNe9U3UDQkw91ZfhMZUnIO31K2";
char ssid[] = "ICN11106";
char pass[] = "i7uw6yt3";

const int PIN_1A = 36;
const int PIN_2A = 1;
const int PIN_3A = 26;
const int PIN_4A = 17;

int count = 0;

void setup(){
  Serial.begin(115200);
  Blynk.begin(auth, ssid, pass);
  M5.begin();
  delay(500);
  M5.update();
  M5.Lcd.clear();
  Serial.print("Setup Completed");
  Serial2.begin(115200, SERIAL_8N1, 32, 33);
  pinMode(PIN_1A, OUTPUT);
  pinMode(PIN_2A, OUTPUT);
  pinMode(PIN_3A, OUTPUT);
  pinMode(PIN_4A, OUTPUT);
  M5.Lcd.fillScreen(MAGENTA);
}

void loop(){
  Blynk.run();
  M5.update();
  motor1( LOW,  LOW, 0);
  motor2( LOW,  LOW, 0);
}

void countndsend2unitv(int label){
  Serial2.write(label);
}

void motor1(int a1, int a2, int d){
  digitalWrite(PIN_1A, a1);
  digitalWrite(PIN_2A, a2);
  delay(d);
}

void motor2(int a3, int a4, int d){
  digitalWrite(PIN_3A, a3);
  digitalWrite(PIN_4A, a4);
  delay(d);
}

BLYNK_WRITE(V0){
  int val = param[0].asInt();
  if(val == 1){
    M5.Lcd.print("Move Left");
    Serial2.write("0");
    digitalWrite(PIN_1A, HIGH);
    digitalWrite(PIN_3A, HIGH);
    delay(100);
    digitalWrite(PIN_1A, LOW);
    delay(100);
    digitalWrite(PIN_3A, LOW);
    M5.Lcd.clear();
  }
}

BLYNK_WRITE(V1){
  int val = param[0].asInt();
  if(val == 1){
    M5.Lcd.print("Turn Left");
    Serial2.write("1");
    digitalWrite(PIN_3A, HIGH);
    delay(200);
    digitalWrite(PIN_3A, LOW);
    M5.Lcd.clear();
  }
}

BLYNK_WRITE(V2){
  int val = param[0].asInt();
  if(val == 1){
    Serial2.write("2");
    digitalWrite(PIN_1A, HIGH);
    digitalWrite(PIN_3A, HIGH);
    delay(200);
    digitalWrite(PIN_1A, LOW);
    digitalWrite(PIN_3A, LOW);
  }
}

BLYNK_WRITE(V3){
  int val = param[0].asInt();
  if(val == 1){
    Serial2.write("3");
    digitalWrite(PIN_1A, HIGH);
    delay(200);
    digitalWrite(PIN_1A, LOW);
  }
}

BLYNK_WRITE(V4){
  int val = param[0].asInt();
  if(val == 1){
    Serial2.write("4");
    digitalWrite(PIN_1A, HIGH);
    digitalWrite(PIN_3A, HIGH);
    delay(100);
    digitalWrite(PIN_3A, LOW);
    delay(100);
    digitalWrite(PIN_1A, LOW);
  }
}
