// ************************************************************
// Sample NorthTek program
// Free Fall warning
// sends an alarm if the compass is in free fall.
// This script can run while data is being output.
// ************************************************************

// ************************************************************
// Marker to be able to purge the progam on reload.
forget fallingCount

: help ." \r\n\r\nType falling <cr> or enter key to run the program \r\n\r\n" ; 

// ************************************************************
// Variable to hold how many samples we've been falling
// ************************************************************

variable fallingCount
f500.0  constant lowG

// ************************************************************
// Bump the falling count if the G's are low.
// Otherwise reset the falling count.
// This gives instant recovery, but short onset.
// ************************************************************

: bump
  lowG < 
  if
    fallingCount @ 1 + fallingCount !
  else
      0 fallingCount !
  then
;

// ************************************************************
// Falling function
// ************************************************************
: falling 

  // ************************************************************
  // Start out with count = 0
  // ************************************************************

  0 fallingCount !

  // ************************************************************
  // loop until an 'esc' is pressed
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

    accelp di@ |v| bump

    // ************************************************************
    // if the counter is > 5 seconds make some noise
    // ************************************************************

    fallingCount @ 5 > 
    if 
      ." Falling!\r\n"
    then

    // ************************************************************
    // wait 10 ms before sampling again.
    // ************************************************************

    10 delay
  repeat 
;

help
