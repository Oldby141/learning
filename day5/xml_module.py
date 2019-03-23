import xml.etree.ElementTree as ET

tree = ET.parse("xml.xml")###从xml文件中读取，用getroot获取根节点，根节点也是Element对象
root = tree.getroot()
print(root.tag)

#遍历xml文档
for child in root:
    print(child.tag,child.attrib)#att-属性
    for i in child:
        print(i.tag,i.text,i.attrib)

#只遍历year结点
for i in root.iter("year"):
    print(i.tag,i.text)