grammar TypeChecker;
start: assigns EOF;

assigns: assign+;
assign returns [datatype=str()]:
    ID ASSIGN expr ';';

expr returns [datatype=str()]:
    term #exprTerm
    | expr PLUS term  #exprPlus
    | expr MINUS term  #exprMinus
    ;

term returns [datatype=str()]:
    fact #termFact
    | term MUL fact  #termMul
    | term DIV fact #termDiv
    ;

fact returns [datatype=str()]:
     STRING #factString
    |INTEGER #factInteger
    |FLOAT #factFloat
    |LPAREN expr RPAREN #factExpr;

/* Lexical rules*/
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
ASSIGN: '=';
LPAREN: '(';
RPAREN: ')';

fragment DIGIT: [0-9];
INTEGER: DIGIT+;
FLOAT: DIGIT+;
STRING:'"' [~ "]* '"'; //\"
ID: [a-zA-Z_] [a-zA-Z0-9_]*;


WS: [ \t\r\n]+ -> skip;
