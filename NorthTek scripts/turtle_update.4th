// ************************************************************
// Sample NorthTek program
// Turn turtle script
// sends an alarm is the compass is upside down for more than 5 seconds.
// This script can run while data is being output.
// ************************************************************

// ************************************************************
// Marker to be able to purge the progam on reload.
forget read_z

// ************************************************************
// Reads the z channel of the accelerometer
// Assumes a horizontal mounting.
( -- zvalue )
// ************************************************************

: read_z 
accelp &di 8 + @ // Read the accelerometer array
                 // Read from third position.
                 // i.e. index 2
;


// ************************************************************
// Variable to hold how many samples we've been turtle
// ************************************************************

variable turtleCount

// ************************************************************
// Bump the turtle count if the z channel is negative
// Otherwise reset the turtle count.
// This gives instant recovery, but 5 second onset.
// ************************************************************

: bump
  f0.0 < 
  if
    turtleCount @ 1 + turtleCount !
  else
      0 turtleCount !
  then
;

// ************************************************************
// Turtle function
// ************************************************************
: turtle 

  // ************************************************************
  // Start out with count = 0
  // ************************************************************

  0 turtleCount !

  // ************************************************************
  // loop until an 's' is pressed
  // ************************************************************

   begin 
		?key 0= 
		if
		  1
		else
		  key 27 = if 0 else 1 then
		then
			while 
    // ************************************************************
    // read the z channel, bump the counter possibly
    // ************************************************************

    read_z bump

    // ************************************************************
    // if the counter is > 5 seconds make some noise
    // ************************************************************

    turtleCount @ 5 > 
    if 
      ." Alert--Upside down" cr  
      7 7 7 emit emit emit
    then

    // ************************************************************
    // wait a second before sampling again.
    // ************************************************************

    1000 delay
  repeat 
;


" Type turtle <cr> or enter key to run the program \r\n" count type