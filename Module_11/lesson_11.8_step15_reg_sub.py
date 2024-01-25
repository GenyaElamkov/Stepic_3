"""
Комментарии 🌶️🌶️
При написании программ мы нередко оставляем комментарии или строки-документации к функциям. Определим три вида комментариев:

https://stepik.org/lesson/680266/step/15?unit=678924
"""

import re
import sys


text = sys.stdin.read()
# text = re.sub(re.compile('^ *\"\"\"[\w \n]*\"\"\"[\n]', re.MULTILINE), "", text)
# text = re.sub(r'^ *#.*[\n]', "", text, flags=re.MULTILINE)
# text = re.sub(r" *#.*$", "", text, flags=re.MULTILINE)
# print(text)

patterns = [r"(^ *\"\"\"[\w \n]*\"\"\"[\n])", r"(^ *#.*[\n])", r"( *#.*$)"]
for pattern in patterns:
    for match in re.finditer(pattern, text, flags=re.MULTILINE):
        s = match.group()
        text = text.replace(s, " ")
print(text)

import re
import sys

regex = r'\n#.*?$|' \
        r'\s*""".*?"""|' \
        r'\n? *#.*?$'

s = sys.stdin.read()
print(re.sub(regex, '', s, flags=re.S | re.M))