// ************************************************************
// If the macro gets reloaded in the same session
// Forget the previous version
// Needs  revision 2.1.1 or later.
// ************************************************************
// This forgets the comp_rot_matrix from a previous load of the macro
// this is standard practice with NorthTek for debugging
// so as to not overflow the wordlist space.
// When this file is reloaded with a terminal a second time
// this removes the previous program.
forget comp_rot_matrix

// ************************************************************
// Declare a few working variables.
// ************************************************************
variable comp_rot_matrix 9 allot
variable sat_rot_matrix 9 allot
variable tare_rot_matrix 9 allot
variable azimuth
variable pitch1
variable roll1
variable cosine_phi
variable sine_phi
variable cosine_theta
variable sine_theta
variable cosine_psi
variable sine_psi
variable copyarray 5 allot

// ************************************************************
// Function (aka NorthTek word): index!
// Shorthand to compute an array index into the variable
// copyarray and write the given value to that index position
// Inputs:
//   TOS-1: value to be written
//     TOS: index into copyarray
// Modifies:
//    NorthTek variable: copyarray
// This word takes a value and an index and stores that element
// in that position in the copyarray.
// ************************************************************
( value index -- )
: index! 4 * copyarray + ! ;


// ************************************************************
// Function (aka NorthTek word): cp
( array_ptr -- ) 
// copies a 3 element array into the copyarray
// copyarray ends up with 0 2 V1 V2 V3 which is
// the right form for setting in the database
// Inputs:
//    TOS: ptr to source array
// Modifies:
//    NorthTek variable: copyarray
// ************************************************************
: cp 
  0 0 index!             // store 0 in position 0 of copyarray
  2 1 index!             // 2 in position 1, therefore we set items 0..2
  dup @ 2 index!         // make copy of pointer,for next index, store 1st element.
  4 + dup @ 3 index!     // move to second element, make copy, store value
  4 + @ 4 index!         // move to third element, store it.
;
: compute_vars
	roll1 @ d>r cos cosine_phi !
	roll1 @ d>r sin sine_phi !
	pitch1 @ d>r cos cosine_theta !
	pitch1 @ d>r sin sine_theta !
	azimuth @ d>r cos cosine_psi !
	azimuth @ d>r sin sine_psi !
;

// ************************************************************
// Functions (aka NorthTek words): row0, row1, row2
// some convenient shorthand for matrices
// Inputs:
//  TOS: Ptr to start of a matrix
// Outputs:
//  TOS: Ptr. to start of a row within the given matrix
// ************************************************************
// Since in Forth you must do matrix/array index calculations
// explicitly, these operators just make it easy to 
// get to rows 1 and 2 of a 3x3 matrix.
: row0 0 + ;
: row1 12 + ;
: row2 24 + ;

// ************************************************************
// Function (aka NorthTek word): compute
// The actual computation
( -- )
// This stack diagram indicates that there are no params
// and no explicit results.
// This function uses the global variables comp_rot_matrix and sat_rot_matrix
// Uses:
//   Database variables: cp2, cp1, accelEst
// Modifies:
//   NorthTek variable: comp_rot_matrix
// ************************************************************
: compute
  compute_vars
  cp2 di@ cp1 di@ accelEst di@  // get the three desired columns
  comp_rot_matrix buildMatrix            // build the comp_rot_matrix with rows

  cosine_theta @ cosine_psi @ f* sat_rot_matrix row0 !
  cosine_theta @ sine_psi @ f* sat_rot_matrix row0 4 + !
  f0.0 sine_theta @ f- sat_rot_matrix row0 8 + !

  cosine_psi @ sine_theta @ sine_phi @ f* f* cosine_phi @ sine_psi @ f* f- sat_rot_matrix row1 !
  sine_psi @ sine_theta @ sine_phi @ f* f* cosine_phi @ cosine_psi @ f* f+ sat_rot_matrix row1 4 + !
  cosine_theta @ sine_phi @ f* sat_rot_matrix row1 8 + !

  cosine_phi @ cosine_psi @ sine_theta @ f* f* sine_phi @ sine_psi @ f* f+ sat_rot_matrix row2 !
  cosine_phi @ sine_theta @ sine_psi @ f* f* sine_phi @ cosine_psi @ f* f- sat_rot_matrix row2 4 + !
  cosine_theta @ cosine_phi @ f* sat_rot_matrix row2 8 + !

  sat_rot_matrix comp_rot_matrix tare_rot_matrix m*m>r
;

// 

// ************************************************************
// Function (aka NorthTek word): copyit
// Copy each row of the matrix into the
// The corresponding row of the boresight matrix.
// Uses:
//    NorthTek variable: matrix
// Modifies:
//    Database variables:
//         boresightMatrixX
//         boresightMatrixY
//         boresightMatrixZ
// ************************************************************
: copyit
  tare_rot_matrix row0 cp           // Copy row 0 of matrix to
                                    //   the copyarray
  boresightMatrixX copyarray        // Set the database with the row
  set drop                          //   and then drop the result
                                    //   from the stack
  tare_rot_matrix row1 cp                    // same as before, Y row
  boresightMatrixY copyarray set drop
  tare_rot_matrix row2 cp                    // same as before Z row
  boresightMatrixZ copyarray set drop
;

// ************************************************************
// Function (aka NorthTek word): printit
// Printout the computed tare_rot_matrix and the current boresight
// matrix.
// ************************************************************
: printit
  tare_rot_matrix cr m.         // Use the matrix print function
  boresightMatrixX  di.         // Use the database print function
  boresightMatrixY  di. 
  boresightMatrixZ  di. 
;

// ************************************************************
// Function (aka NorthTek word): tare
// Create a small program to perform the Tare function
// Uses:
//   Database variables (used by compute): cp2, cp1, accelEst
// Modifies:
//   NorthTek variable: tare_rot_matrix
//   Database variable: orientation
//   Database variables (set by copyit):
//         boresightMatrixX
//         boresightMatrixY
//         boresightMatrixZ
// ************************************************************
: apr_tare
  roll1 !
  pitch1 !
  azimuth !
  tare_rot_matrix clear(m)       // clear the matrix we declared
  orientation 0 set     // setup to default orientation, required.
  1000 delay            // Wait 1 second for this to settle in computation
  compute copyit        // compute the matrix and copy to the boresight matrix.
  printit               // Print it for verification.
;

// Input format is azimuth pitch1 roll1 apr_tare CRLF
//    ex. f191.4 f49.5 f15.0 apr_tare [ENTER]
