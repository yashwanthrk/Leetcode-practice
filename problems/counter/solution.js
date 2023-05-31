/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    return function() {
        return n++
    };
};


// let n = 5;

// console.log(--n); // Output: 4
// console.log(n);   // Output: 4

// let m = 5;

// console.log(m--); // Output: 5
// console.log(m);   // Output: 4

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */