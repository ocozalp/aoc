import math

s = raw_input()
a = 0.0
g = 0.0
for c in s:
    if c == 'A' or c == 'T':
        a += 1.0
    else:
        g += 1.0

s = [float(f) for f in raw_input().split()]

for ss in s:
    print g * math.log10(ss/2) + a *  math.log10((1-ss)/2),