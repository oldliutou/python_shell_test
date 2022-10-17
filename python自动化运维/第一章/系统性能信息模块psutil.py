import psutil

mem = psutil.virtual_memory()
print("内存总量为：%s" %(mem.total))
print("内存可用为：%s" %mem.available)