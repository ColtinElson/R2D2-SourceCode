#include <AFMotor.h>

AF_DCMotor motor(1, MOTOR12_64KHZ);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  motor.run(FORWARD);
  motor.setSpeed(200);
  delay(2000);
}
