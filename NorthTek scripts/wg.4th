// ************************************************************
// War games
// ************************************************************

// ************************************************************
// Erase a previous instance of this file if it gets reloaded
// ************************************************************
forget signon

// ************************************************************
// Print a signon message
// ************************************************************
: signon
cr
."  _          _ _       "  cr
." | |__   ___| | | ___  "  cr
." | '_ \\ / _ \\ | |/ _ \\ "  cr
." | | | |  __/ | | (_) |"  cr
." |_| |_|\\___|_|_|\\___/ "  cr
;

// ************************************************************
// Print the menu
// ************************************************************
: game?
." Would you like to play a game?" cr
." 1) Marketing Bingo " cr
." 2) Development Sorry " cr
." 3) Engineering Pacheesi " cr
." 4) Sales Poker " cr
." 5) Investment Roulette" cr
." 6) Global Thermonuclear war" cr
;

// ************************************************************
// VT100 Sequences for home, red and black
// ************************************************************
: home
27 emit ." [2J" 27 emit ." [H"
;
: red
27 emit ." [5;30;41m" 
;
: black
27 emit ." [0m" 
;

// ************************************************************
// Print boom on a clear screen, in red.
// ************************************************************
: boom!
home red
// Note: I had to add extra "\" chars to
// what figlet created to 
// make them be escaped properly.
."  ____   ___   ___  __  __ _  " cr
." | __ ) / _ \\ / _ \\|  \\/  | | " cr
." |  _ \\| | | | | | | |\\/| | | " cr
." | |_) | |_| | |_| | |  | |_| " cr
." |____/ \\___/ \\___/|_|  |_(_) " cr  
black
;

                            

// ************************************************************
// Show dots to indicate a ticking time bomb.
// ************************************************************
: bomb
25 0 do 
." ." cr 100 delay 
loop
boom!
;

// ************************************************************
// ************************************************************
// Play the game
// basically take the characater and compare to
// each choice, provide an answer in each case.
// If you pick 6 you get a surprise.
// ************************************************************
// ************************************************************
: game
dup [ char 1 ] literal = if
." Too much drinking!" cr
else
dup [ char 2 ] literal = if
." Too depressing!" cr
else
dup [ char 3 ] literal = if
." Too boring!" cr
else
dup [ char 4 ] literal = if
." Too Risky!" cr
else
dup [ char 5 ] literal = if
." No upside!" cr
else
dup [ char 6 ] literal = if
bomb
else
drop ." bad choice " cr
then
then
then
then
then
then
;

// ************************************************************
// This runs the game.
// After it is loaded type go.
// ************************************************************
: go
home red signon black game?
." Press a letter, ESC to quit\r\n"
begin key dup 27 = 0= while
game
repeat
;
" Type go to begin the game!\r\n"
home count type

