from PyQt5.Qt import *
import sys
import json
import random
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("remake模拟器")
window.resize(900,800)
window.setWindowFlags(Qt.WindowCloseButtonHint)
window.setStyleSheet("background-color: rgb(254,253,201);")
mtitle=QLabel(window)
mtitle.setText("<h1>重开模拟器</h1>")
mtitle.move(350,50)
mypix=QLabel(window)
mypix.resize(240,200)
mypix.move(320,100)
mypix.setStyleSheet("background-color: white;")
myplain=QPlainTextEdit(window)
myplain.move(200,300)
myplain.resize(500,300)
myplain.setStyleSheet("background-color: grey;")
txtcruser=myplain.textCursor()
ss=QTextCharFormat()
ss.setFontFamily("黑体")
ss.setFontPointSize(18)
txtcruser.setCharFormat(ss)
myplain.setReadOnly(True)
mytags=QPlainTextEdit(window)
tagcursor=mytags.textCursor()
mytags.resize(200,400)
mytags.move(700,200)
mytags.setReadOnly(True)
btn1=QPushButton(window)
btn1.resize(200,100)
btn1.move(0,650)
btn1.setStyleSheet("background-color: white;")
btn2=QPushButton(window)
btn2.resize(200,100)
btn2.move(220,650)
btn2.setStyleSheet("background-color: white;")
btn3=QPushButton(window)
btn3.resize(200,100)
btn3.move(440,650)
btn3.setStyleSheet("background-color: white;")
btn4=QPushButton(window)
btn4.resize(200,100)
btn4.move(660,650)
btn4.setStyleSheet("background-color: white;")
qage=QLabel(window)
window.show()

decision=0
age=0
mytag={0}
die=False
quests_strong=[]
quests_weak=['6','7','8','116','17','18','45','53']
result=[['0','1'],['0','1'],['0','1'],['0','1']]
link=['-1','-1','-1','-1']

def btn_press1():
    global age
    age+=1
    qage.setText("{}".format(age))
    res=result[0]
    if res[0]!='NULL':
        txtcruser.insertBlock()
        txtcruser.insertText(res[0])
        txtcruser.insertBlock()
    if res[1]!='NULL' and  res[1]!="STRONG":
        tagcursor.insertBlock()
        tagcursor.insertText(res[1])
    if res[1]=="STRONG":
        read_event(mydict[str(link[0])])
    elif link[0]!='-1' and link[0]!='NULL':
        quests_weak.append(link[0])
    if res[1]!="STRONG":
        s = random.choice(quests_weak)
        if len(quests_weak) > 5:
            quests_weak.remove(s)
        read_event(mydict[str(s)])
def btn_press2():
    global age
    age+=1
    qage.setText("{}".format(age))
    res=result[1]
    if res[0]!='NULL':
        txtcruser.insertBlock()
        txtcruser.insertText(res[0])
        txtcruser.insertBlock()
    if res[1]!='NULL' and  res[1]!="STRONG":
        tagcursor.insertBlock()
        tagcursor.insertText(res[1])
    if res[1]=="STRONG":
        read_event(mydict[str(link[1])])
    elif link[1] != '-1' and link[1] != 'NULL':
        quests_weak.append(link[1])
    if res[1] != "STRONG":
        s = random.choice(quests_weak)
        if len(quests_weak) > 5:
            quests_weak.remove(s)
        read_event(mydict[str(s)])
def btn_press3():
    global age
    age+=1
    qage.setText("{}".format(age))
    res=result[2]
    if res[0]!='NULL':
        txtcruser.insertBlock()
        txtcruser.insertText(res[0])
        txtcruser.insertBlock()
    if res[1]!='NULL' and  res[1]!="STRONG":
        tagcursor.insertBlock()
        tagcursor.insertText(res[1])
    if res[1]=="STRONG":
        read_event(mydict[str(link[2])])
    elif link[2] != '-1' and link[2] != 'NULL':
        quests_weak.append(link[2])
    if res[1] != "STRONG":
        s = random.choice(quests_weak)
        if len(quests_weak) > 5:
            quests_weak.remove(s)
        read_event(mydict[str(s)])
def btn_press4():
    global age
    age+=1
    qage.setText("{}".format(age))
    res=result[3]
    if res[0]!='NULL':
        txtcruser.insertBlock()
        txtcruser.insertText(res[0])
        txtcruser.insertBlock()
    if res[1]!='NULL' and  res[1]!="STRONG":
        tagcursor.insertText(res[1])
    if res[1]=="STRONG":
        read_event(mydict[str(link[3])])
    elif link[3] != '-1' and link[3] != 'NULL':
        quests_weak.append(link[3])
    if res[1] != "STRONG":
        s = random.choice(quests_weak)
        if len(quests_weak) > 5:
            quests_weak.remove(s)
        read_event(mydict[str(s)])
btn1.clicked.connect(btn_press1)
btn2.clicked.connect(btn_press2)
btn3.clicked.connect(btn_press3)
btn4.clicked.connect(btn_press4)
with open("info.json","r") as a:
    info=a.read()
mydict=json.loads(info)
print(mydict)
def read_event(myinfo):
    global result
    global link
    btn1.setEnabled(True)
    btn2.setEnabled(True)
    btn3.setEnabled(True)
    btn4.setEnabled(True)
    desribtion=myinfo[0]
    choice = myinfo[1].split('$')
    result=list(map(lambda x:x.split('^'),(myinfo[2].split('$') )))
    link = myinfo[3].split('$')
    txtcruser.insertBlock()
    txtcruser.insertText(desribtion)
    txtcruser.insertBlock()
    if choice[0]!="NULL":
        btn1.setText(choice[0])
    else:
        btn1.setEnabled(False)
        btn1.setText("")
    if choice[1]!="NULL":
        btn2.setText(choice[1])
    else:
        btn2.setEnabled(False)
        btn2.setText("")
    if choice[2]!="NULL":
        btn3.setText(choice[2])
    else:
        btn3.setEnabled(False)
        btn3.setText("")
    if choice[3]!="NULL":
        btn4.setText(choice[3])
    else:
        btn4.setEnabled(False)
        btn4.setText("")
    print(choice,result,link)

read_event(mydict['1'])




sys.exit(app.exec_())