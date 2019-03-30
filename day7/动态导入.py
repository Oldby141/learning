#!_*_coding:utf-8_*_
# from lib import aa
#
# c = aa.C()
# print(c.name)

import importlib
#
# lib = __import__("lib.aa")
# c = lib.aa.C()
# print(c.name)

aa = importlib.import_module("lib.aa")
print(aa.C().name)
assert type(aa.C().name) is str
print("a")