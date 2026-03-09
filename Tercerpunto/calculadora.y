%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void yyerror(const char *s);
int yylex();

/* Newton-Raphson: igual que la funcion de Python */
double raiz_cuadrada(double a) {
    double tolerancia = 1e-10;
    int max_iter = 1000;
    double x = a / 2;  /* estimacion inicial */

    for (int i = 0; i < max_iter; i++) {
        double x_nuevo = 0.5 * (x + a / x);

        if (fabs(x_nuevo - x) < tolerancia)
            return x_nuevo;

        x = x_nuevo;
    }
    return x;
}
%}

%union {
    double num;
}

%token <num> NUMERO
%token SQRT
%type  <num> expresion

%%

programa:
    programa expresion
    | /* vacio */
;

expresion:
    SQRT '(' NUMERO ')'  { printf("raiz aproximada: %f\n", raiz_cuadrada($3)); }
;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    yyparse();
    return 0;
}
