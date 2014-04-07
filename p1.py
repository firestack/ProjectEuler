#! /usr/bin/env python3

arr3 = [(i+1)*3 for i in range(1000//3)]
arr5 = [(i+1)*5 for i in range(999//5)]
n = list(set(arr3+arr5))

