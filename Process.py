

#Import saved code file
from usercode import code
code=code





#A1 test product
if 'An example of' in code:
    code = code.replace('An example of', 'An illustration of')

if 'an example of' in code:
    code = code.replace('an example of', 'an illustration of')

if 'tesla' in code:
    code = code.replace('tesla', 'BMW')




#B


#Output section
print(" ")
print(" ")
print("Work Done:")
print(" ")
print(code)
