#!/usr/bin/python3

i = []
with open('input','r') as f:
    for line in f:
        l = line.split()
        i.append((l[0], l[2], l[4]))

ends = {}
for line in i:
    if line[0] not in ends.keys():
        ends[line[0]] = len(ends.keys())
    if line[1] not in ends.keys():
        ends[line[1]] = len(ends.keys())
print(ends)

m = []
for c in range(len(ends.keys())):
    m.append([0] * len(ends.keys()))

for line in i:
    print(ends[line[0]])
    print(ends[line[1]])
    m[ends[line[0]]][ends[line[1]]] = int(line[2])
    m[ends[line[1]]][ends[line[0]]] = int(line[2])
print(m)

import itertools

ct = 0
def p_len(path):
    global ct
    ct += 1
    ln = 0
    for i in range(len(path)-1):
        ln += m[path[i]][path[i+1]]
    return ln

minn = None
maxn = None
perms = list(itertools.permutations(list(ends.values())))
print(len(perms))
for path in perms:
    l = p_len(path)
    if minn is None or l < minn:
        minn = l
    if maxn is None or l > maxn:
        maxn = l
print('Min:', minn)
print('Max:', maxn)
