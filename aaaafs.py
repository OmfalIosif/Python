from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QGroupBox, QRadioButton, QHBoxLayout, QVBoxLayout, QPushButton,QButtonGroup
from random import shuffle
 
app = QApplication([])
 
main_win = QWidget()
main_win.resize(500,400)
main_win.setWindowTitle("Memory Card")
 
question_lbl = QLabel("Which nationality does not exist?")
box = QGroupBox("Answer options")
rbtn1 = QRadioButton("Enets")
rbtn2 = QRadioButton("Chulyms")
rbtn3 = QRadioButton("Smurfs")
rbtn4 = QRadioButton("Aleuts")
btn = QPushButton("Answer")
 
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
 
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn3)
layout_ans3.addWidget(rbtn2)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
box.setLayout(layout_ans1)
box.show()
answerbox = QGroupBox("Test Result")
lbl_result = QLabel("Are you right or wrong?")
lbl_correct = QLabel("Correct answer placement")
layout_res = QVBoxLayout()
layout_res.addWidget(lbl_result)
layout_res.addWidget(lbl_correct)
answerbox.setLayout(layout_res)
 
layout_l1 = QHBoxLayout()
layout_l2 = QHBoxLayout()
layout_l3 = QHBoxLayout()
 
layout_line = QVBoxLayout()
 
layout_l1.addWidget(question_lbl, alignment =  Qt.AlignLeft)
layout_l2.addStretch(1)

layout_l2.addWidget(box,stretch = 4)
layout_l2.addWidget(answerbox, stretch = 4)
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
 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
layout_line.setSpacing(0)
main_win.setLayout(layout_line)
 
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer=right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
q1 = Question("What's your favorite sport","football","baseball","basket","tennis")
q2 = Question("What's your favorite sport1","football1","baseball1","basket1","tennis1")
q3 = Question("What's your favorite sport2","football2","baseball2","basket2","tennis2")
 
index=-1
questions=[q1,q2,q3]
answers = [rbtn1, rbtn2, rbtn3, rbtn4]
layout_line.setSpacing(0)
def show_result():
    box.hide()
    answerbox.show()
    btn.setText("Next Question")
 
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
        next_question()
 
        
 
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question_lbl.setText(q.question)
    lbl_correct.setText(q.right_answer)
    show_question()
 
def next_question():
    global index
    index +=1
    if index>=len(questions):
        index=0
    q = questions[index]
    ask(q)
btn.clicked.connect(show_test)
 
main_win.show()
 
app.exec_()