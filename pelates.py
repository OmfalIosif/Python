# -*- coding: cp1253 -*-

def fun(tem):
    timh=0
    if tem>0 and tem<6:
        timh=tem*50
    elif tem<11:
        timh=(5*50)+(tem-5)*43
    elif tem<21:
        (5*50)+(4*43)+(tem-15)*40
    else:
        (5*50)+(4*43)+(10*40)+(tem-20)*35
return timh


pel=0
name=raw_input('Dose onoma , gia telos dwse TELOS: ')
while name!="TELOS":
    tem=int(abs(input('Dose plhthos temaxiwn: ')))
    timh=fun(tem)
    print "H timh einai ",timh
    pel+=1
    name=raw_input('Dose onoma , gia telos dwse TELOS: ')
if pel=0:
    print "No pelates sto magazi"
