import pytest

from flow import sorting_column


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        context = f.read().split('#')
        arr = []
        for line in context:
            arr.append(line.split())
    dic = {}
    counter = 1
    for line in arr:
        name_test = f"TEST_{counter}:"
        if name_test in line:
            line = line[line.index(name_test) + 1:]
            dic[name_test] = dic.setdefault(name_test, line)
            counter += 1
    return dic


path = 'output.txt'
output_txt = read_file(path)

for k in output_txt:
    output_txt[k] = ' '.join(map(str, output_txt[k]))

test_data = list(zip([1, 2, 3], output_txt.values()))


@pytest.mark.parametrize("num, expected_result", test_data)
def test_sorting_column(num, expected_result):
    assert sorting_column(num) == expected_result
