from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QGroupBox, QRadioButton, QHBoxLayout, QVBoxLayout, QPushButton,QButtonGroup
#from random import shuffle, randint
app = QApplication([])

main_win= QWidget()
main_win.resize(500,400)
main_win.setWindowTitle("Memory Card")
#main_win.right_ans = 0
#main_win.qcounter = 1
#Widget Creation
question_lbl = QLabel("Which nationality does not exist?")
box = QGroupBox("Answer options")
rbtn1 = QRadioButton("Enets")
rbtn2= QRadioButton("Chulyns")
rbtn3 =QRadioButton("Smurfs")
rbtn4 = QRadioButton("Aleuts")
btn =QPushButton("Answer")

layout_ans1= QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 =QVBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn3)
layout_ans3.addWidget(rbtn2)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
box.setLayout(layout_ans1)
box.show()

answerbox=QGroupBox("Test Result") 
lbl_result=QLabel("Are you right or wrong?")
lbl_correct=QLabel("Correct answer placement")
layout_res=QVBoxLayout()
layout_res.addWidget(lbl_result)
layout_res.addWidget(lbl_correct)
answerbox.setLayout(layout_res)

layout_l1=QHBoxLayout()
layout_l2=QHBoxLayout()
layout_l3=QHBoxLayout()

layout_line=QVBoxLayout()

layout_l1.addWidget(question_lbl,alignment=Qt.AlignLeft)
layout_l2.addStretch(1)
layout_l2.addWidget(box,stretch=4)
layout_l2.addWidget(answerbox,stretch=4)
answerbox.hide()
layout_l2.addStretch(1)
layout_l3.addStretch(1)
layout_l3.addWidget(btn,stretch=4)
layout_l3.addStretch(1)

layout_line.addStretch(1)
layout_line.addLayout(layout_l1)
layout_line.addStretch(1)
layout_line.addLayout(layout_l2,stretch=4)
layout_line.addStretch(1)
layout_line.addLayout(layout_l3)

RadioGroup=QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_line.setSpacing(0)
main_win.setLayout(layout_line)

answers=[rbtn1,rbtn2,rbtn3,rbtn4]

def show_result():
    box.hide()
    answerbox.show()
    btn.setText("Next Question")

def show_correct(message):
    show_result()
    lbl_result.setText(message)

def check_answer():
     if answers[0].isChecked():
        show_correct("Correct")
     elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct("Incorrect :'( ")

def show_question():
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
    answerbox.hide()
    box.show()
    btn.setText("Answer")
def show_test():
    if btn.text()=="Answer":
        check_answer()
    else:
        ask("What's my favorite food?","Spagetti","beans","meatballs",'pork')

def ask(question,right_answer,wrong1,wrong2,wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    question_lbl.setText(question)
    lbl_correct.setText(right_answer)
    show_question()





btn.clicked.connect(show_test)

main_win.show()

app.exec_()
