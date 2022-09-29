import json
with open("info.json","r") as a:
    info=a.read()
mydict=json.loads(info)
print(mydict)
print(isinstance(mydict,dict))


#事件格式 编号，字符串描述事件，按钮选择描述,结果,link
def create_events(id,desribtion,choices,result,link):
    mydict[id]=[desribtion,choices,result,link]
    info1 = json.dumps(mydict)
    with open("info.json","w") as a:
        a.write(info1)

def create():
    id=int(input("id:"))
    desc=input("描述")
    choice=""
    for i in range(4):
        choice+=input("按钮事件")+'$'
    choice=choice.rstrip('$')
    res=""
    for i in range(4):
        res+=input("选择结果")+'^'+input("成就")+'$'
    res=res.rstrip('$')
    link=''
    for i in range(4):
        link+=input("关联")+'$'
    link=link.rstrip("$")
    create_events(id,desc,choice,res,link)


def read_event(myinfo):
    desribtion=myinfo[0]
    # choice="123$456$789$333".split('$')
    choice = myinfo[1].split('$')
    # result=list(map(lambda x:x.split('^'),("12^3$45^6$78^9$33^3".split('$') )))
    result=list(map(lambda x:x.split('^'),(myinfo[2].split('$') )))
    link = map(lambda x:int(x),myinfo[3].split('$'))
    print(choice,result,link)

create()




