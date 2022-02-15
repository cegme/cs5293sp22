
# g/re/p 


## Regular Expressions

- Characters:
Normal characters that we would like to match

    grep "pluto" planets.txt

- Special characters

\ ^ { } ( ) + ? . [ ] | $ 

    grep "\{ \}" language.txt

- OR - alternatives | 

    grep "cat|dog|lizard" pets.csv

- character classes []
  A way to group sets of charaters together 

    - vowels: [aeiou]
    - range: [l-p]
    - not classes: [^aeiou] 

    grep -n "[Ll]eanna" names.txt

- shorthand classes

    - \w \d \s - word, digit, whitespace 
    - \w == [a-zA-Z0-9_]
    - \W \D \S - not word, not digit, not whitespace
    - \W == [^a-zA-Z]

    grep "\d\d\d-\d\d-\d\d\d\d" socialsecurity.txt

- occurences

    - ? -  zero or 1 

        grep "Leanna?" names.txt 

    - * - 0 or more

        grep "Lean*a?" namess.txt 
           > Lea
           > Leannnnnnnnnna

    - + - one or more
    

    - custom occurences (extended grep) 
       - a{n} -- a appear n times
       - a{n,} -- a appear n or more times
       - a{,n} -- a appears atleast n times
       - a{n,m} -- a appears between n and m times
 
