import re

regex_obj = re.compile(r'\ba\w+\b')
result = regex_obj.findall('auto apple art astra assert', pos=3)

print(result)