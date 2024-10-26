grammar calculator;

start: expr EOF;
expr: term ((ADD | SUB) term)*;
term: factor ((MUL | DIV) factor)*;
factor: (ADD | SUB)? NUMBER | LPAREN expr RPAREN;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';
//NUMBER: [0-9]+;
NUMBER: [0-9]* '.' [0-9]+ | [0-9]+ '.'? ;
WS: [ \t\r\n]+ -> skip;
