#import all resources needed
import tkinter as tk
import random


#Import user entered code file

from usercode import code

root= tk.Tk()

def export ():
    label1 = tk.Label(root, text= code, fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(500, 700, window=label1)



#Code Section, don't touch it unless you know python well!


    ##Number Repleace Counter for user display
repleace_works=0
int(repleace_works)
    ##Word Count for user input
word_counter = len(code.split())
word_counter = word_counter - 1

while '~JilanSolution_SudoA' in code:
    rangenint = random.randint(1,2)
    if rangenint == 1:
        code = code.replace('~JilanSolution_SudoA', ' ',1)
    if rangenint == 2:
        code = code.replace('~JilanSolution_SudoA', '  ',1)

    ##General English


#UM-1
    while 'An example of' in code:
        rangenint = random.randint(1,2)
        if rangenint == 1:
            code = code.replace('An example of', 'An illustration of',1)
        if rangenint == 2:
            code = code.replace('An example of', 'A case in point of',1)
    while 'an example of' in code:
        rangenint = random.randint(1,2)
        if rangenint == 1:
            code = code.replace('an example of', 'an illustration of',1)
        if rangenint == 2:
            code = code.replace('an example of', 'a case in point of',1)

#UM-2
    while 'International corporation'.strip() in code:
        rangenint = random.randint(1,3)
        if rangenint == 1:
            code = code.replace('International corporation', 'Multinational corporation',1).strip()
            repleace_works= repleace_works + 1
        if rangenint == 2:
            code = code.replace('International corporation', 'Compaines that do businesses all over the globe',1).strip()
            repleace_works= repleace_works + 1
        if rangenint == 3:
            code = code.replace('International corporation', 'Compaines that do businesses with clients all over the world',1).strip()
            repleace_works= repleace_works + 1
    while 'international corporation' in code:
        rangenint = random.randint(1,3).strip()
        if rangenint == 1:
            code = code.replace('international corporation', 'Multinational corporation',1).strip()
            repleace_works= repleace_works + 1
        if rangenint == 2:
            code = code.replace('international corporation', 'Compaines that do businesses all over the globe',1).strip()
            repleace_works= repleace_works + 1
        if rangenint == 3:
            code = code.replace('international corporation', 'Compaines that do businesses with clients all over the world',1).strip()
            repleace_works= repleace_works + 1



if 'faced some issues' in code:
    code = code.replace('faced some issues', 'faced a variety of issue')



        ###Aerospace
if 'Space Shuttle Challenger' in code:
    code = code.replace('Space Shuttle Challenger', 'American Shuttle Challenger')

if 'Space Shuttle Columbia' in code:
    code = code.replace('Space Shuttle Columbia', 'American Shuttle Columbia')


    ##Single/Dual Word para

#Output section
canvas1 = tk.Canvas(root, width = 1000, height = 1000)
canvas1.pack()



generate = tk.Button(text='Click Me to see',command=export, bg='#03fc4e',fg='white')
canvas1.create_window(500, 500, window=generate)

root.mainloop()
