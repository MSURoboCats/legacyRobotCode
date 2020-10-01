forget storeCalX

variable storeCalX 4 allot
variable storeCalY 4 allot
variable storeCalZ 4 allot

: store
0 3 pick 0 4 * + !
1 3 pick 1 4 * + !
	2 pick 2 4 * + !  // get from stack, offset
		swap 3 4 * + !  // get from stack, divisor
;

: saveHomeCal
	storeCalX magFieldCalX &di dup 1 4 * + @ swap 0 4 * + @ store
	storeCalY magFieldCalY &di dup 1 4 * + @ swap 0 4 * + @ store
	storeCalZ magFieldCalZ &di dup 1 4 * + @ swap 0 4 * + @ store
	hex 10400 storeCalX 32 ee!
	100 delay
	hex 10500 storeCalY 32 ee!
	100 delay
	hex 10600 storeCalZ 32 ee!
	100 delay
;

: grabHomeCal
	hex 10400 storeCalX 32 ee@
	100 delay
	hex 10500 storeCalY 32 ee@
	100 delay
	hex 10600 storeCalZ 32 ee@
	100 delay
;

: restoreHomeCal
	magFieldCalX storeCalX set drop
	magFieldCalY storeCalY set drop
	magFieldCalZ storeCalZ set drop
;

variable alternateX 4 allot
variable alternateY 4 allot
variable alternateZ 4 allot

: saveCustomer
	alternateX magFieldCalX &di dup 1 4 * + @ swap 0 4 * + @ store
	alternateY magFieldCalY &di dup 1 4 * + @ swap 0 4 * + @ store
	alternateZ magFieldCalZ &di dup 1 4 * + @ swap 0 4 * + @ store
;

: setCustomer
	magFieldCalX alternateX set drop
	magFieldCalY alternateY set drop
	magFieldCalZ alternateZ set drop
;

