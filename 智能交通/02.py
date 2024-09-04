import math

count = int(input())
if math.trunc(count/32767) == count/32767:
    print("{:.1f}".format(float(count/32767)))
else:
    print("{:.5f}".format(float(count/32767)))
