hash_table = [[] for _ in range(2)]
 
 
def hash_func(hash_str):
    return len(hash_str) % 2
 
 
def set_value(key, value):
    el = hash_table[hash_func(key)]
    for pair in el:
        if key == pair[0]:
            pair[1] = value
            break
    else:
        el.append([key, value])
 
 
def get_value(key):
    for k, v in hash_table[hash_func(key)]:
        if key == k:
            return v
 
 
set_value("abc", 1)
set_value("zxc", 2)
set_value("fd", 3)
set_value("a", 4)
set_value("d", 5)
set_value("2134", 6)
set_value("142155", 7)
 
set_value("abc", 999999999999)
print(get_value("abc"))
print(get_value("zxc"))
print(get_value("fd"))
print(get_value("a"))
print(get_value("d"))
print(get_value("2134"))
print(get_value("142155"))
print(get_value("142155e"))
