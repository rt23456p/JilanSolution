

#Import saved code file
from usercode import code
code=code




#Code Section, don't touch it unless you know python well!




##Repleace Number Counter
repleace_works=0
int(repleace_works)



#Remove this later, just for testing purposes
if 'tesla' in code:
    code = code.replace('tesla', 'BMW')
    repleace_works = repleace_works + 1




#Longer Term Para Section


#Short Term Para


        ###General English
if 'An example of' in code:
    code = code.replace('An example of', 'An illustration of')
    print("hi")
if 'an example of' in code:
    code = code.replace('an example of', 'an illustration of')

if 'faced some issues' in code:
    code = code.replace('faced some issues', 'faced a variety of issue')




        ###Aerospace
if 'Space Shuttle Challenger' in code:
    code = code.replace('Space Shuttle Challenger', 'American Shuttle Challenger')

if 'Space Shuttle Columbia' in code:
    code = code.replace('Space Shuttle Columbia', 'American Shuttle Columbia')


    ##Single/Dual Word para
if ' ' in code:
    pass




#Output section
print(" ")
print(" ")
print("Work Done: We repleaced a total of " + str(repleace_works) + " words/short terms")
print("The output in the next line")
print(code)
