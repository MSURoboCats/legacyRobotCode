// EELE489R
// AUVSI Robosub 2017-2018
// Chris Major
// Created 2/23/18

// C code to test all 8 speed controllers and impellers via an Arduino Mega 2560
// Digital Pins 2 through 9 (PWM) are connected to the ESCs
// The PWM settings on the controller are centered at 1500 for the OFF state,
// a maximum of 1600 for FORWARD motion, and a minimum of 1400 for BACKWARD motion.
// Running the PWM at values above or below the max and/or min may result in system damage

// Include Servo library for PWM management
#include <Servo.h>

// Declare Servo objects to monitor the speed controllers and place in the array
Servo servo_1, servo_2, servo_3, servo_4, servo_5, servo_6, servo_7, servo_8;
Servo servoESC[] = {servo_1, servo_2, servo_3, servo_4, servo_5, servo_6, servo_7, servo_8};

// Digital PWM pin for the speed controller
int servoPins[] = {2, 3, 4, 5, 6, 7, 8, 9};

// Variabls to represent the motion states of the impeller
// OFF is a PWM of 1500
// Running the impellor FORWARDS is a PWM of 1550
// Running the impellor BACKWARDS is a PWM of 1450
int off = 1500;
int forw = 1550;
int back = 1450;

// Variables to change the stop and run times of the impeller
// PLAY = 500 MS = 0.5 S
// PAUSE = 1500 MS = 1.5 S
// WARNING: DO NOT RUN IMPELLORS FOR MORE THAN HALF A SECOND OUTSIDE OF WATER
// THE MOTORS WILL OVERHEAT AND POSSIBLY BURN OUT
int pause = 1500;
int play = 500;

// Variable for serial commands
int serial_cmd;
int press_key;

void setup() {
  // Open serial if on computer, ignore if disconnected
  Serial.begin(9600);
  Serial.print("BEGIN\n");

  // Set up motors
  setPins();
  Serial.print(" > Setting up motors\n");

  // Turn off all motors
  motorsOff();
  Serial.print(" > Turning motors off\n");

  // Pause impeller for allotted time
  delay(pause);
  Serial.print("\nREADY\n\n");
}

// Run loop
void loop() {
  // Check if Serial ports are available
  if (Serial.available() > 0){
    // Read serial command
    serial_cmd = Serial.parseInt();

    // Run motor
    runMotor(serial_cmd);
  }
}

// Attach the ESCs to the pins to set up PWM, set motors at off
void setPins() {
  int i = 0;
  for (i = 0; i < 8; i++) {
    servoESC[i].attach(servoPins[i]);  
  }
}

// Turn off all motors
void motorsOff() {
  int i = 0;
  for (i = 0; i < 8; i++) {
    servoESC[i].writeMicroseconds(off); 
  }
}

// Key to run impeller forwards
void runMotor(int key) {

  if (key <= 7 && key >= 0) {

    // Print status
    Serial.println("\nRunning Impellor ...");
    Serial.println(key);
    
    // Run impellor
    servoESC[key].writeMicroseconds(forw); 
    delay(play);  

    // Stop impellor
    servoESC[key].writeMicroseconds(off); 
    delay(pause);
    
  } else {
    Serial.println("\nInvalid Impellor number, please choose between 0 to 7!");
  }
}

// END OF CODE
