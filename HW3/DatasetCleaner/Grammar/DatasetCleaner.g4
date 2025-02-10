grammar DatasetCleaner;

cleaning returns [datatype=str()]:
    CLEAN file_path commandList EOF;

commandList returns [datatype=str()]:
    (command (',' command)*)?;

command returns [datatype=str()]:
    REMOVE DUPLICATES #rmvDupCommand
    | DROP MISSING #drpMissCommand
    | FILL MISSING column WITH value #fillMissCommand
    | FILTER column COMPARISON_OPERATOR value #filterCommand
    | RENAME column TO column #renameCommand
    ;

column returns [datatype=str()]:
    QUOTE STRING QUOTE;

value returns [datatype=str()]:
    NUMBER | QUOTE STRING QUOTE;

file_path returns [datatype=str()]:
    QUOTE STRING '.' STRING QUOTE #filePath
    ;

CLEAN: 'CLEAN';
REMOVE: 'REMOVE';
DUPLICATES: 'DUPLICATES';
DROP: 'DROP';
MISSING: 'MISSING';
FILL: 'FILL';
WITH: 'WITH';
FILTER: 'FILTER';
RENAME: 'RENAME';
TO: 'TO';
COMPARISON_OPERATOR: '==' | '!=' | '<' | '>' | '<=' | '>=' ;

NUMBER: [0-9]+ ('.' [0-9]+)?;
fragment ESC: '\\';
STRING: [a-zA-Z_] [a-zA-Z0-9_]+;
QUOTE: '"';

WS: [ \t\r]+ -> skip;
NEWLINE: ('\n' | '\r\n' | '\r') -> skip;
