# -*- coding: utf-8 -*-

def normalize(name):
    return str.capitalize(name)

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)