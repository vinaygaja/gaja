#Quesion:

##Prompt the user to enter a long sentence
##        - What is the last character in the sentence ?
##        - What are the last 5 characters in the sentence ?
##        - Print the characters that are present in 2nd and 5th position of the sentence
##        - Print the character at the center of the string, along with the 2 adjoining characters. 
##        Ex : If the string entered is "Web Browser”
##        the character at its centre is "r" and so print "Bro"

#code:

#user to enter long sentence
sent=input('enter a long sentence:')

print('last characte:',sent[-1])
print('last 5 character:',sent[-5:])
print('character present in 2nd & 5th position:',sent[2],'&',sent[5])
i=len(sent)
i=i//2
print('character at its center:',sent[i])
print(sent[i-1],sent[i],sent[i+1])






## getting out put:

##RESTART: C:\Users\Administrator\Desktop\pythonexercises\S07Q03longsentence.py 
##enter a long sentence:web browser
##last characte: r
##last 5 character: owser
##character present in 2nd & 5th position: b & r
##character at its center r
##b r o
