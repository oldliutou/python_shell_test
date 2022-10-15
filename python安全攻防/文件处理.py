
s = "Hello World!!!!"
f = open("demo.txt","a")
#model = w 是写模式 ；a 是追加写模式；r是读模式；r+是读写模式

f.write(s)
f.close()

with open("demo.txt","a") as f:
    f.write("hello python!")
    f.close()