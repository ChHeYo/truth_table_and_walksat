(a) Any Collaborators: No, it was an individual effort

(b) How to run the program.


- = negation
^ = and
v = or
=> if..then
<=> if and only if


1. Open a terminal and type ‘python truth_table_app.py’. It would open the program.

2. It would ask a user to input knowledge base. 
(Each clause MUST BE separated by COMMA)

I solved question #1, #2, #3, so knowledge base for each would be respectively,

Q1. p, p => q; (No CAPITALIZATION needed)

Q2. -p11, b11 <=> (p12 v p21), b21 <=> (p11 v p22 v p31), -b11, b21;

Q3. myth => -mort, -myth => (mort ^ mamm), (-mort v mamm) => horn, horn => magic;


3. The program then would ask the user, ‘What do we need to prove?’
For each question, we want to prove

Q1. q

Q2. p12

Q3. 
a) myth
b) magic
c) horn

****Answer to Q3.

Horn and magic can be inferred but myth can’t be inferred because myth is True when mort, mama, horn, and magic are all False 
or it’s False when all others are True. Therefore, premises are true but conclusion is false and can’t be drawn from the premises.


