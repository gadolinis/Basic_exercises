import random

d1 = "[---------]\n[         ]\n[    0    ]\n[         ]\n[---------]"
d2 = "[---------]\n[         ]\n[  0   0  ]\n[         ]\n[---------]"
d3 = "[---------]\n[    0    ]\n[    0    ]\n[    0    ]\n[---------]"
d4 = "[---------]\n[  0   0  ]\n[         ]\n[  0   0  ]\n[---------]"
d5 = "[---------]\n[  0   0  ]\n[    0    ]\n[  0   0  ]\n[---------]"
d6 = "[---------]\n[  0   0  ]\n[  0   0  ]\n[  0   0  ]\n[---------]"

seq = [d1, d2, d3, d4, d5, d6]
random.choice(seq)
again = "y"

while again == "y":
    print(random.choice(seq))
    again = input("Please press y, to roll dice again: ")