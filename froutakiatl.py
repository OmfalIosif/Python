#-*-coding:cp1253-*-
import random
no100=0
play=input('1. ��� �� ������� \n2. ��� �������� ���������\n')
while no100==0:
    if play==1:
        mny=input('���� ������ �������� ��� �����: ')
        if mny>0:
            while mny>0:
                play=input('-----------------------------\n2. ��� �������� ���������  \n����������� ���� ������ ��� ��������\n')
                if play != 2:
                    win=0
                    pos=input('--------------------------------\n���� ���� �������������: ')
                    a=random.randint(1,9)
                    b=random.randint(1,9)
                    c=random.randint(1,9)
                    d=b-1
                    e=c-1
                    f=b+1
                    print a,b,c
                    if a==b and b==c:
                        win=pos*2
                        mny=mny+win
                    elif a==b and b==c and c==7:
                        win=pos*5
                        mny=mny+win
                    elif a==d and b==e and c==f:
                        win=pos*0.5
                        mny=mny+win
                    else:
                        win=0
                        mny=mny-pos
                    if win>0:
                        print '�� ����� ����� ',win
                    else:
                        print '������'
                        print mny
                else:
                    break
        elif mny<=0:
                print '��� �������� �������.'
    else:
        break

