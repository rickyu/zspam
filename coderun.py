#encoding: utf-8
from functions import user_register_time
def runcode(code):
    action = {"type":"create_post"}
    g = {"action":action, "result":None, "user_register_time":user_register_time}

    exec  code in g
    print(g["action"])
    print(g.get("result", None))
    print(g.get("a", None))



if __name__ == "__main__":
    code = """

a = 1
if a == 1:
    a = 15
else:
    a = 16
a+10

action["haha"] = "heeh"
result=10
haha=5
ut = user_register_time(10)
if ut > 10:
    
print("action" in globals())
#print(locals())

"""
    runcode(code)

