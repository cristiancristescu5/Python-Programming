def process_lists(a: list, b: list):  # 1
    operations = [set(a).union(set(b)),
                  set(a).intersection(set(b)),
                  set(a).difference(set(b)),
                  set(b).difference(set(a))]
    return operations


def prop_to_dict(s: str):  # 2
    return {i: s.count(i) for i in s}


def compare_dicts(dict1, dict2):  # 3
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return dict2 == dict1

    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1:
        if not compare_dicts(dict1[key], dict2[key]):
            return False
    return True


def build_xml_element(tag, content, **attributes):  # 4
    result = f"<{tag}"

    for key, value in attributes.items():
        result += f' {key}="{value}"'
    result += ">"
    result += content
    result += f"</{tag}>"
    return result


def validate_dict(rules: set[tuple], d: dict):  # 5
    dict_rules = {i[0]: i[1:] for i in rules}

    if set(dict_rules.keys()) != d.keys():
        return False

    for key in d.keys():
        if not str(d[key]).startswith(dict_rules[key][0]):
            return False

        if not str(d[key]).endswith(dict_rules[key][2]):
            return False

        if not (str(d[key]).count(dict_rules[key][1]) != 0) \
                and not (str(d[key]).endswith(dict_rules[key][0])):
            return False
    return True


def list_set(l: list):  # 6
    return len(set(l)), len(l) - len(set(l))


def sets_to_dict(*list_tuples: set):  # 7
    d = {}
    sl = list(list_tuples)
    for i in range(len(sl)):
        for j in range(i + 1, len(sl)):
            set1 = sl[i]
            set2 = sl[j]
            d[f"{set1} | {set2}"] = set1 | set2
            d[f"{set1} & {set2}"] = set1 & set2
            d[f"{set1} - {set2}"] = set1 - set2
            d[f"{set2} - {set1}"] = set2 - set1
    return d


def loop(d: dict):  # 10
    keys = set(d.keys())
    visited = []
    start = d['start']
    visited.append(start)
    while len(visited) < len(keys):
        start = d[start]
        if visited.count(start) == 1:
            return visited
        visited.append(start)
    return []


def pos_args_keys(*args, **pos):  # 11
    count = 0;
    for i in args:
        if i in pos.values():
            count += 1
    return count


print(pos_args_keys(1, 2, 3, 4, x=1, y=2, z=3, w=5))
print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
print(sets_to_dict({1, 2}, {2, 3}))
print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                    {"key1": "come inside, it's too cold out", "key2": "start this is middle not valid winter"}))
print(process_lists([1, 2, 3, 4, 5, 6], [2, 3, 4, 7, 8, 9, 10]))
print(prop_to_dict("Ana has apples"))
print(compare_dicts({'a': 1, 'b': [1, 2, 3], 'c': ['a', 5, 6]}, {'a': 1, 'c': ['a', 5, 6], 'b': [1, 2, 3]}))
print(build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))
print(list_set([1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 7, 7, 8, 9]))
