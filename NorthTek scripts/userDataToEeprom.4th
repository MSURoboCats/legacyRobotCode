// ***************************************************************************
// The is an example of using NorthTek to store user data in EEPROM
// The space allocated to users in EEPROM is 0x10000 to 0x17FFF.  The
// Navigation Module will look for a NorthTek script at 0x10000 so you
// should avoid using that address for simple data.  If you have a script
// at 10000 hex then you should start at a higher address than 10100 hex
// depending on the size of the script.


variable x       // allocate 4 bytes in RAM
hex 12345678 x ! // store 12345678 hex at x (RAM is least significant byte first)
hex 10100        // push the EEPROM address 10100 on the stack
x                // push the address of x on the stack
4                // push the number of bytes to be written
ee!              // write the 2 bytes at x to EEPROM address 10100 hex

// Use ".s" if you want to see what is on the stack before the ee! command.
// Wait a few seconds for the EEPROM write to complete and command
// a reset or cycle power to confirm that the data was store in non-volatile
// memory.

// now read the data back
variable y
hex 10100    // push the EEPROM address on the stack
y            // push the address of y on the stack
4            // push the number of bytes to be written
ee@          // read the 4 bytes at EEPROM 10100 and store them in y
			// read what is at y
y @ .
