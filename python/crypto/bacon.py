#!/usr/bin/env python
# -*- coding: utf8 -*-

t = {
    'aaaaa': 'a',
    'aaaab': 'b',
    'aaaba': 'c',
    'aaabb': 'd',
    'aabaa': 'e',
    'aabab': 'f',
    'aabba': 'g',
    'aabbb': 'h',
    'abaaa': 'i',
    'abaab': 'j',
    'ababa': 'k',
    'ababb': 'l',
    'abbaa': 'm',
    'abbab': 'n',
    'abbba': 'o',
    'abbbb': 'p',
    'baaaa': 'q',
    'baaab': 'r',
    'baaba': 's',
    'baabb': 't',
    'babaa': 'u',
    'babab': 'v',
    'babba': 'w',
    'babbb': 'x',
    'bbaaa': 'y',
    'bbaab': 'z'
}

c = "ABBABAABBAAAAABABABAABABBAAAAABAABBAAABAABBBABBAABABBABABAAABABBBAABAABABABBBAABBABAA"
m1 = ""
for i in range(0, len(c), 5):
    a = c[i:i + 5]
    m1 += t.get(a.lower())
print(m1)
