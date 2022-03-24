This project is able to prove whether a given Knowledge Base (KB) is valid or invalid.

To learn about knowledge bases and reasoning in Artificial Intelligence, see this article:
https://ai.plainenglish.io/knowledge-and-reasoning-in-artificial-intelligence-4755d0f5d161

I'll give a quick summary.

A KB consists of a number of facts. For example, let's state the following facts: Craig likes ice cream - expressed as 
as L(Craig, IC). Fish can swim - S(F). Bob loves any candy - C(X) ^ L(Bob,X) (If X is a type of candy, then Bob loves X). 
Starbust is a type of candy - C(SB).  

So, our current KB is:
L(Craig, IC)
S(F)
C(X) 
L(Bob,X)
C(SB)

Let's say we wanted to add a statement to our KB: Bob loves Starburst - L(Bob, SB). Could we logically add this statement given 
the previous facts? In short, it is hard to directly prove that something is true. However, if we could definitively 
prove that the inverse is false, then that is the same thing. So, we will add the inverse of the statement to the KB
and try to prove a contradiction. If we do end up proving a contradiction, that means that the statement we want to add to the
KB is valid. 

-So, we add the contradiction to the KB - ~L(Bob, SB)
-Now, we just have to replace X with S, which we can do because SB is a specific type of X (Starburst is a specific
type of candy).
-We would then have a new fact L(Bob, SB) from having replaced X in the previous fact L(Bob, X) in the KB above.
-We see that L(Bob, SB) directly contradicts the new fact ~L(Bob, SB). So, we can say that the inverse is false and
the original statement that Bob loves Starbust must be true.

My program will go through all of the steps of a few pre-given KBs (but you can write your own and feed it to the program too!)
and show all of the additional facts logically added to the KB until a contradiction is found or until all logical possibilities
are exhausted and a contradiction can't definitively be proven false.

TO RUN THE PROGRAM:
Enter the given directory with all the KB files and py scripts in it.

RUN:
python main.py

You will be prompted to enter the name of the KB file. You can enter any of:
demo.in, elephants.txt, facts.txt, task1.in, task2.in, task3.in, task6.in, task7.in, or write your own text file.

The steps and final validity of the KB should show up!