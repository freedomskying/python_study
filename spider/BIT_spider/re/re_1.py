import re

match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(match.group(0))

match = re.match(r'[1-9]\d{5}', '100081 BIT')
if match:
    print(match.group(0))

match = re.findall(r'[1-9]\d{5}', '100081 BIT TSU100084')
if match:
    print(match.group(0))