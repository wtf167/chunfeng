#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def init_graph():
    gs = '''1 2 100 FLAG{
2 3 87 AFQWE
2 4 57 ETKLS
2 5 50 WEIVK
2 6 51 AWEIW
3 7 94 QIECJF
3 8 78 QSXKE
3 9 85 QWEIH
4 13 54 WQOJF
4 14 47 KDNVE
4 15 98 QISNV
5 10 43 AEWJV
5 11 32 QWKXF
5 12 44 ASJVL
6 16 59 ASJXJ
6 17 92 QJXNV
6 18 39 SCJJF
6 23 99 SJVHF
7 19 99 WJCNF
8 20 96 SKCNG
9 20 86 SJXHF
10 21 60 SJJCH
11 21 57 SJHGG
12 22 47 SJCHF
14 10 55 EJFHG
16 17 59 ASJVH
18 12 53 SJFHG
18 24 93 SHFVG
21 22 33 SJFHB
19 25 88 ASHHF
20 25 96 SJVHG
22 25 23 SJVHJ
25 26 75 SDEV}'''
    graph = {str(x): {} for x in range(1, 27)}
    result = {str(x): {} for x in range(1, 27)}
    for i in gs.split('\n'):
        j = i.split(' ')
        graph[j[0]][j[1]] = int(j[2])
        result[j[0]][j[1]] = j[3]

    costs = {}
    costs["2"] = 100
    costs["26"] = float("inf")

    parents = {}
    parents["2"] = "1"
    parents["26"] = None

    global processed
    processed = []

    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs.get(n, float("inf")) > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    p = "26"
    a = []
    while p != '1':
        p = parents[p]
        a.append(p)
        a.append(p)
    a = a[::-1][1:]
    a.append("26")
    for i in range(0, len(a), 2):
        print(result[a[i]][a[i+1]], end="")


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == '__main__':
    init_graph()
