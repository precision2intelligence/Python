# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = s.replace(' ', '%20')  # 如果不写“s=”，则出错。说明使用函数后会新得到一个字符串但是不覆盖原来的，而s的内容是不变的
        # 参数后面直接用方法即可，不要忘了结果的保留，多次错了
        return s


# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ', '%20')  # 直接写两行代码就OK，这是自带的函数，return结果就好

    # 错误的写法


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        for x in s:  # 字符串可以一个一个取字符出来
            if x == ' ':
                x = '20%'  # x只是一个变量，无法赋值回去，可以查看，但不是对原内容的操作了
                # 这里只能查看，这是新定义的变量
        return s