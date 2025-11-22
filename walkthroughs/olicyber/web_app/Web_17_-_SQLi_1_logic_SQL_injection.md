# URL
https://training.olicyber.it/challenges#challenge-356
# Concept
* basic SQL injection
* login bypass
# Method of solve
* the challenge wants us to navigate to this webpage: `http://web-17.challs.olicyber.it/logic`
* we are given a very detailed description of how to do SQL injection on the following webpages
* in the final challenge, we're asked to do a basic SQL injection auth bypass
* the payload that works is `test' or 1=1 -- -`
