#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3);
int motors = 0x31;
int turn = 0x32;

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
  mySerial.write(0x34);
  mySerial.write(2);

  delay(100);

  Serial.println("Changing modes..");
  while( mySerial.available() ) {
    Serial.print(mySerial.read(), HEX);
  }
  Serial.println("Done.");
  
  
}

void loop() {
  // put your main code here, to run repeatedly:
  int counter = 16;
  /*while (counter <= 15) {
    motorRun();
   /* counter++;
  }*/
 while (counter > 15) {
    motorTurn();
  }
}

void motorRun() {
  delay(1000);

  mySerial.write((uint8_t)0x00);
  mySerial.write(motors);
  mySerial.write(150);
}

void motorTurn() {
  delay(1000);

  mySerial.write((uint8_t)0x00);
  mySerial.write(turn);
  mySerial.write(10);
}


