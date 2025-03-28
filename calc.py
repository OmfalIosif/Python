def pros():
    apo=a+b

def afer():
    if a > b:
        apo = a-b
    else:
        apo = b-a

def pol():
    apo = a*b

def dier():
    apo = a/b


f = ''


while f == '':
    a = input("Dwse ton 1o arithmo: ")
    b = input("Dwse ton 2o arithmo: ")
    er=input("Dwse praksh(+,-,*,/) gia telos '!' : ")
    while er!='+' or er!='-' or er!='*' or er!='/' or er!='!':
        er=input("Dwse swsth praksh(+,-,*,/) gia telos '!' : ")
    if er=='+':
        pros(apo)
    elif er=='-':
        afer(apo)
    elif er=='*':
        pol(apo)
    elif er=='/':
        dier(apo)
    elif er=='!':
        break
        
