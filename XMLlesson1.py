import xml.etree.ElementTree as ET
data = '''<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>'''
#This is the XML data
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))
#We call it tree because XML data is stored like a tree diagram