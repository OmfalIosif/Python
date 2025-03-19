from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton,QListWidget,QLineEdit,QTextEdit,QHBoxLayout, QVBoxLayout, QInputDialog
from PyQt5.QtCore import Qt
import json

app = QApplication([])

notes_win=QWidget()
notes_win.setWindowTitle("Smart Notes")
notes_win.resize(900,600)

notes={
    "Welcome":{
        "text":"This is the best note taking app in the world!",
       "tags":["good","instructions"]
    }

}

#window widgets

field_text = QTextEdit()
list_notes=QListWidget()
list_notes_label=QLabel("List of notes")
btn_note_create=QPushButton("Create note")
btn_note_delete=QPushButton("Delete note")
btn_note_save=QPushButton("Save note")

list_tags_label=QLabel("List of tags")
list_tags= QListWidget()

field_tag=QLineEdit()
field_tag.setPlaceholderText("Entertag...")

btn_add=QPushButton("Add to note")
btn_del=QPushButton("Untag from note")
btn_search=QPushButton("Search notes by tag")

col_1=QVBoxLayout()
col_2=QVBoxLayout()

line_1=QHBoxLayout()
line_2=QHBoxLayout()

line_1.addWidget(btn_note_create)
line_1.addWidget(btn_note_delete)
line_2.addWidget(btn_add)
line_2.addWidget(btn_del)


col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
col_2.addLayout(line_1)
col_2.addWidget(btn_note_save)
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
col_2.addLayout(line_2)
col_2.addWidget(btn_search)
col_1.addWidget(field_text)

#list_notes.addItems(notes)
line=QHBoxLayout()

line.addLayout(col_1,stretch=2)
line.addLayout(col_2,stretch=1)

notes_win.setLayout(line)

with open("notes_data.json","r") as file:
    notes=json.load(file)

notes["Constantinos"] = "Kopanos"

list_notes.addItems(notes)

notes_win.show()
app.exec()
