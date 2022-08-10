# import hashlib
# for i in  range(100000):
#     md5_value = hashlib.md5(str(i).encode()).hexdigest()
#     if(md5_value[1]==md5_value[14] and md5_value[14]==md5_value[17]):
#         if((int(md5_value[1])+int(md5_value[14])+int(md5_value[17]))/int(md5_value[1])==int(md5_value[31])):
#
#             print(md5_value)
#
# # md5_value = hashlib.md5(str("asdsaf").encode()).hexdigest()
#
#coding: utf-8
#啊韬
import hashlib
dic = '0123456789qazwsxedcrfvtgbyhnujmikolp'
md5 = hashlib.md5(dic.encode()).hexdigest()
for a in dic:
    for b in dic:
        t = str(a)+str(b)
        md5 = hashlib.md5(t.encode()).hexdigest()
#print md5
#print md5[1:2]
#print md5[14:15]
#print md5[17:18]
        if md5[1:2] == md5[14:15] and md5[14:15]== md5[17:18]:
            if ((int(md5[1]) + int(md5[14]) + int(md5[17])) / int(md5[1]) == int(
                    md5[31])):
                print (t)
                print (md5)
                print (md5[1:2])
                print (md5[14:15])
                print (md5[17:18])