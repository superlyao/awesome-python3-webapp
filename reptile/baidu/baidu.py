from bs4 import BeautifulSoup
import re
# 根据html网页字符串创建beautifulSoup
soup = BeautifulSoup('', 'html.parser', from_encoding='utf-8')
# 方法: find_all(name, attrs, string)
# 查找所有a标签
soup.find_all('a')
# 查找所有a标签，连接符合/view/123.html的连接
soup.find_all('a', href='/view/123.html')
# 正则 支持模糊匹配
soup.find_all('a', href=re.compile(r'/view/123.html'))
# 查找所有div标签, class为abc, 文字为python的节点
soup.find_all('div', class_='abc', string='python')
