# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:09:29 2023

@author: Huawei
"""
n = int(input("Jumlah ="))
for i in range (n, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()