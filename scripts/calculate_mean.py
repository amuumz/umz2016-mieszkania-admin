#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) < 2:
    print "usage: {} NUM_LINES < train.tsv > out.tsv".format(sys.argv[0])
    exit()

price_sum = 0.0
n = 0
for line in sys.stdin:
    price_sum += float(line.split("\t", 1)[0])
    n += 1

price_mean = price_sum / n

for _ in range(int(sys.argv[1])):
    print "{:.4f}".format(price_mean)
