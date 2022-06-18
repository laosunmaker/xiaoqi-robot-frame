import ast
###黑白名单,列表形式保存#
with open("../config/blacklist.txt","r") as f:
    b_str=f.read()
    f.close()
    blacklist=ast.literal_eval(b_str)
    print("[*]黑名单:",blacklist)
with open("../config/owner.txt","r") as f:
    o_str=f.read()
    f.close()
    owner=ast.literal_eval(o_str)
    print("[*]管理名单:",owner)
def blacklist_add(text):
    blacklist.append(str(text))#向黑名单内写数据
    with open("../config/blacklist.txt","w") as f: #向文件内写数据
        f.write(str(blacklist))
        f.close()
        print(blacklist)
def blacklist_del(text):
    blacklist.remove(str(text))#向黑名单内删除数据
    with open("../config/blacklist.txt","w") as f: #向文件内写数据
        f.write(str(blacklist))
        f.close()
        print(blacklist)
def owner_add(text):  
    owner.append(str(text))
    with open("../config/owner.txt","w") as f: #向文件内写数据
        f.write(str(owner))
        f.close()
        print(owner)
def owner_del(text):
    owner.remove(str(text))
    with open("../config/owner.txt","w") as f: #向文件内写数据
        f.write(str(owner))
        f.close()
        print(owner)
    
    
