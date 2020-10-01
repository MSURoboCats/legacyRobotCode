forget variable
variable delay1
variable value1
variable value2
// Magnetometers
variable mx1
variable mx2
variable mvx

variable ytot

variable filterK



: deviation

// Initialize variables
f0.04 filterK !
    
    delay1 @ 0 do

    10 delay

// Process Magnetometers    
	mx1 @
	yaw &di @ dup
	mx2 @ f+ f2.0 f/ mx1 @ f- fabs 
	ytot @ f- filterK @ f* ytot @ f+ ytot !
	mx1 ! mx2 !

     loop
	." \r\nytot" ytot @ f.
;

: tOutput 
    delay1 !
    km0 f0.1 set drop
    begin 
        // ?key 0= 
		km0 &di @ f0.0 > while
                km0 dup &di @ f0.01 f- set drop
				km0 di.
				deviation
     repeat 
;

// type (delay in ms) tOutput <CTRL-m> to start and <CTRL-z> to stop
// example: '50 tOutput <CTRL-m>' will output the data every 50ms
