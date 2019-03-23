import re
print(re.search(".","a\n").group())
print(re.search("^a","dddadd\n"))
print(re.search(".","a\n").group())
print(re.search("^a\d","a1dd123\n"))
print(re.search("^a+\d+","aba123dddadd\n"))
print(re.search("^a.+ a$","addda"))
print(re.search("a[1-9]+a","adda123a"))
print(re.findall("a*","adgeaafeaf"))
print(re.findall("da?","adgeaafeaf"))
print(re.findall("a{2}","adgeaafeaf"))
print(re.findall("a{2,3}","adgeaaaafeaf"))
print(re.findall("a|d","adgeaafeaf"))
print(re.search("abc|ABC","ABC123abc"))
print(re.findall("(abc){2}", "abcabca456c"))#findall和（）有问题
print(re.search("(ab){2}\|","abacabab|"))
print(re.search("\D","asd)&^d"))#匹配非数字
print(re.search("\W","asd)&^d"))#匹配非[A-Za-z0-9]
print(re.search("\w+","a123#f"))#匹配[A-Za-z0-9]
print(re.search("\s+", "ab\tc1\n3"))

print(re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") )#分组匹配‘(?P<name>...)’

print(re.split("\|","a|faf|fa\d|d"))#以匹配到的字符当做列表分隔符

print(re.sub("a","b","dsdsa"))#匹配字符并替换

print(re.search(r"\\+","d\\\\\\ge"))#原生字符串  或\\\\

print(re.search("abc","ABDABCab",flags=re.I))#re.I忽略大小写   re.M多行模式
print(re.search("a","/t/n  /\t\n\r\nba"))
print(re.search("a","/r/na"))

print(re.search(".","\na",flags=re.S))#点任意匹配模式，改变'.'的行为     '.' 默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行