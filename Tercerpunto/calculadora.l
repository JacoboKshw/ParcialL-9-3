%{
#include "calculadora.tab.h"
%}

%%

[0-9]+(\.[0-9]+)?   { yylval.num = atof(yytext); return NUMERO; }
"sqrt"              { return SQRT; }
[ \t\n]             { /* ignorar espacios */ }
.                   { return yytext[0]; }

%%

int yywrap() { return 1; }
