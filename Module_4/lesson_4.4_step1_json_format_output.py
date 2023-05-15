"""
Вывел содержимое словаря countries, расположив его элементы в
лексикографическом порядке ключей, указав в качестве разделителя пар
ключ-значение строку   -  (пробел дефис пробел), а в качестве
отступов — три пробела.

https://stepik.org/lesson/623073/step/1?unit=618703
"""
import json

countries = {
    "Monaco": "Monaco",
    "Iceland": "Reykjavik",
    "Kenya": "Nairobi",
    "Kazakhstan": "Nur-Sultan",
    "Mali": "Bamako",
    "Colombia": "Bogota",
    "Finland": "Helsinki",
    "Costa Rica": "San Jose",
    "Cuba": "Havana",
    "France": "Paris",
    "Gabon": "Libreville",
    "Liberia": "Monrovia",
    "Angola": "Luanda",
    "India": "New Delhi",
    "Canada": "Ottawa",
    "Australia": "Canberra",
}
print(json.dumps(countries, sort_keys=True, indent="   ", separators=(",", " - ")))
