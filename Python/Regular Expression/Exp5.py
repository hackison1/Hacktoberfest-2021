
import re

string = '39801 356, 2102 1111'

pattern = '(\d{3}) (\d{2})'


match = re.search(pattern, string) 

if match:
  print(match.group())
else:
  print("pattern not found")