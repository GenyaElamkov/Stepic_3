"""
Модуль shelve.

https://stepik.org/lesson/737724/step/1?unit=739371
"""

import shelve

FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"

with shelve.open(FILENAME) as states:
    state = states.get("Brussels", "Undefined")
    print(state)

with shelve.open(FILENAME) as states:
    key = "Brussels"
    if key in states:
        print(states[key])


with shelve.open(FILENAME) as states:
    for key in states:
        print(key," - ", states[key])