#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import binascii


with open('/tmp/in', 'rb') as fr:
    s = fr.read()
with open('/tmp/out', 'wb') as f:
    f.write(binascii.unhexlify(s))
