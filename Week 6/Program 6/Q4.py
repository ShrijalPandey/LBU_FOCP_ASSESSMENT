'''
Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a
message and reverse the resulting string. Write, and test, a function that
takes a string containing a message and "encrypts" it in this way
'''

string="There is no God higher than truth"
encrypt=string.replace(" ","")[::-1]
print(encrypt)