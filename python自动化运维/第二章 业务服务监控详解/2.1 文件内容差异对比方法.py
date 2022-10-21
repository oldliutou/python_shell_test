'''
通过使用difflib模块实现两个字符串的差异对 比，然后以版本控制风格进行输出。
'''
import difflib
text1 = """text1： #定义字符串1 This module provides classes and functions for comparing sequences. including HTML and context and unified diffs. difflib document v7.4 add string """
text1_lines = text1.splitlines() #以行进行分隔，以便进行对比
text2 = """text2： #定义字符串2 This module provides classes and functions for Comparing sequences. including HTML and context and unified diffs. difflib document v7.5"""
text2_lines = text2.splitlines()
def diff_info():

    d = difflib.Differ()
    diff = d.compare(text1_lines,text2_lines)# 采用compare方 法对字符串进行比较

    print("\n".join(list(diff)))
def html_diff():
    d = difflib.HtmlDiff()
    print(d.make_file(text1_lines,text2_lines))
if __name__ == '__main__':
    html_diff()

