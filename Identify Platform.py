#Identifier Test Platform, Only for feedback to improve on Process.py, not for final release




#So the Purpose of this is to make two way repleace possible, as the process.py still have one way repleace, so the other way will not work, but with this been used as planned, it should word

# Test Var
subject= 'summit'

# Triggering subject
trigger = 0


if 'summit' in subject:
    subject = subject.replace('summit', 'peak')
    print("Trigger Active(0 Pos)")
    trigger == 'hash'


if trigger == 'hash':
    #Notify on the test Platform, final will not have this
    print("Trigger Active (1 pos)")

else:
    if 'peak' in subject:
        subject = subject.replace('peak', 'summit')



#Final Test Output
print(subject)
