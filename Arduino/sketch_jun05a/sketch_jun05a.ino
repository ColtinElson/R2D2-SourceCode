#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3);

void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);
  mySerial.begin(9600);

  delay(1000);

  mySerial.write((uint8_t)0x00);
  mySerial.write(0x29);

  delay(100);
  
  Serial.println("Starting..");
  while( mySerial.available() ) {
    Serial.print(mySerial.read());
  }
  Serial.println("Done.");

  delay(1000);

  mySerial.write((uint8_t)0x00);
  mySerial.write(0x2D);

  delay(100);

  Serial.println("Reading errors..");
  while( mySerial.available() ) {
    Serial.print(mySerial.read(), HEX);
  }
  Serial.println("Done.");
  
  delay(1000);

  mySerial.write((uint8_t)0x00);
  mySerial.write(0x34);
  mySerial.write(2);
  delay(100);
  
  Serial.println("Changing mode..");
  while( mySerial.available() ) {
    Serial.print(mySerial.read(), HEX);
  }
  Serial.println("Done.");
}

void loop() {
  // put your main code here, to run repeatedly:

  delay(1000);

  mySerial.write((uint8_t)0x00);
  mySerial.write(0x31);
  mySerial.write(128);
  mySerial.write(0x32);
  mySerial.write(30);
}
