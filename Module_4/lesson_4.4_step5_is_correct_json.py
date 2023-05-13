"""
 Возвращать True, если строка string удовлетворяет формату JSON, или False в противном случае.
"""
import json

def is_correct_json(string: str) -> bool:
    try:
        return bool(json.loads(string))
    except json.decoder.JSONDecodeError:
        return False

    # return res


data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
# print(is_correct_json('number = 17'))

print(is_correct_json(data))