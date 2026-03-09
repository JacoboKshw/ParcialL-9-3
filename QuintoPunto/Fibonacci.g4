grammar Fibonacci;

// Regla principal
programa: expresion EOF;

expresion: FIBO '(' NUMERO ')';

// Tokens
FIBO   : 'FIBO';
NUMERO : [0-9]+;
WS     : [ \t\n\r]+ -> skip;
