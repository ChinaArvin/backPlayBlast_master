#coding:utf-8
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

# import json
# print json.dumps(d)


# 需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。
# 所以如果你要构建一个需要大量 OrderedDict 实例的数据结构的时候
# （比如读取 100,000 行 CSV 数据到一个 OrderedDict 列表中去），
# 那么你就得仔细权衡一下是否使用 OrderedDict 带来的好处要大过额外内存消耗的影响。