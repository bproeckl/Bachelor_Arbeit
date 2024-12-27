#!/usr/bin/env python

import sys

input = sys.argv[1]
print(input)
with open(input, 'r') as f_in, open('output2.txt', 'w') as f_out:
    content = f_in.read()
    f_out.write(f"Processed: {content}")