hmap = {}
hmap["11"]="aaa"
hmap["22"]="bbb"
hmap["33"]="ccc"
print(hmap)
# 遍历键值对 key->value
for key, value in hmap.items():
    print(key, "->", value)
# 单独遍历键 key
for key in hmap.keys():
    print(key)
# 单独遍历值 value
for value in hmap.values():
    print(value)