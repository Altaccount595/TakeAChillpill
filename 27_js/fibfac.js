//Team JASON :: Caden Khuu, Jonathan Metzler
//SoftDev pd5
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>

function fact(n){
  if (n == 1){
    return 1;
  }
  return fact(n - 1) * n;
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

fact(4)
fact(5)

//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>

function fib(n){
  if(n < 2){
    return n;
  }
  return fib(n-1) + fib(n-2);
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

fib(4)
fib(5)

//=================================================================




