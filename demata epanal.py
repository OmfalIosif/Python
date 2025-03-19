# -*- coding: cp1253 -*-
baros=float(input('dwse baros tou dematos: '))
zwnh=input('dwse zwnh proorismou (A,B,d): ')
xre=0 
if zwnh=='d':
    if baros<=3:
        xre=baros*0.5
    elif baros<=10:
        xre=(3*0.5)+(baros-3)*1.5
    elif baros<=20:
        xre=(3*0.5)+(7*1.5)+(baros-10)*2
    else:
        xre=(3*0.5)+(7*1.5)+(10*2)+(baros-20)*2.5      
elif zwnh=='d':
    if baros<=3:
        xre=baros*1
    elif baros<=10:
        xre=3+(baros-3)*2
    elif baros<=20:
        xre=3+(7*2)+(baros-10)*2.5
    else:
        xre=3+(7*2)+(10*2.5)+(baros-20)*4
elif zwnh=='d':
    if baros<=3:
        xre=baros*1.5
    elif baros<=10:
        xre=(3*1.5)+(baros-3)*2.5
    elif baros<=20:
        xre=(3*1.5)+(7*2.5)+(baros-10)*3.5
    else:
        xre=(3*1.5)+(7*2.5)+(10*3.5)+(baros-20)*5


        
ekpt=xre*(15/100.0)
xre=xre-ekpt
print ("to poso pou plhrwneis einai: "), xre
