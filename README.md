# Numeric Literals
Program utilizing deterministic finite automata to recognize numeric literals according to python 3.12 documentation

## Contributors 
### Group - Smurf Kat
Brenden Johnson - BVOLT

## Task Division
Brenden Johnson - Decimal Integer NFA & DFA Diagrams, DFA Class

## Decimal Integer

```python
decinteger   ::=  nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
nonzerodigit ::=  "1"..."9"
digit        ::=  "0"..."9"
```

![alt text](DecIntDFA.jpg?raw=true)