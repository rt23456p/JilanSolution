

#Import saved code file
from usercode import code
code=code





#Code Section, don't touch it unless you know python well!
if 'An example of' in code:
    code = code.replace('An example of', 'An illustration of')

if 'an example of' in code:
    code = code.replace('an example of', 'an illustration of')

if 'faced some issues' in code:
    code = code.replace('faced some issues', 'faced a variety of issue')

if 'tesla' in code:
    code = code.replace('tesla', 'BMW')




#B


#Output section
print(" ")
print(" ")
print("Work Done:")
print(" ")
print(code)
