#Identifier Test Platform, Only for feedback to improve on Process.py, not for final release


#Update Sep 3 2020, this test is finished successfully today, therefore, this is the final version

#So the Purpose of this is to make two way repleace possible, as the process.py still have one way repleace, so the other way will not work, but with this been used as planned, it should worl both ways.


# Test Var# Triggering subject
trigger = "1"
subject= 'summit'

if 'summit' in subject:
    subject = subject.replace('summit', 'peak')
    print("Trigger Active(0 Pos)")
    trigger == '2'


if trigger == '1':
    #Notify on the test Platform, final will not have this
    print("1")
    subject = subject.replace('peak', 'summit')

else:
    print("Trigger Active (1 pos)")



#Final Test Output
print(subject)
