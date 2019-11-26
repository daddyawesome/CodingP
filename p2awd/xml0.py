import xml.etree.ElementTree as ET
data = '''<person>
  <name>Mark</name>
  <phone type="intl">
     +63 916 619 0483
  </phone>
  <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Atrr:',tree.find('email').get('hide'))
