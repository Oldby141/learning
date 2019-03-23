import xml.etree.ElementTree as ET

new_xml = ET.Element("personinfolist")
personinfo = ET.SubElement(new_xml,"personinfo",attrib={"enrolled":"yes"})
name = ET.SubElement(personinfo,"name")
name.text = "BYF"
age = ET.SubElement(personinfo,"age",attrib={"checked":"no"})
sex = ET.SubElement(personinfo,"sex")
age.text = "56"
personinfo2 = ET.SubElement(new_xml,"personinfo",attrib={"enrolled":"yes"})
name = ET.SubElement(personinfo2,"name")
name.text = "Oldby"
age = ET.SubElement(personinfo2,"age")
sex = ET.SubElement(personinfo2,"sex")
age.text = "23"
sex.text = "man"

et = ET.ElementTree(new_xml) #生成文档对象
et.write("text.xml",encoding="utf-8",xml_declaration=True)
ET.dump(new_xml)