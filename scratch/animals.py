# -*- coding: utf-8 -*-

import json
import logging
import time

def gradegen():
    print([100,100])
    return -1

def main(name, grades=gradegen):
    print("world")
    myint = 1231231312
    myfloat = 0.4
    mystring = """
    stuff
    stuff on a new line
    last line"""

    print(f"{myint} -- {myfloat} --{mystring}")
    print(r"Hello\t\tHello")
    mystring = f"{myint} -- {myfloat} --{mystring}"

    print(f"{name}: {grades}")

    gradegen()
    grades()


def datastructure():
    print('-'*40)
    # Lists
    a = [1,2,2,3, "hello"]
    print(a)

    # ranges
    print(a[1:3])

    print(a[-1])

    print(a[::-1])
    print(a[::2])
    print(a[100:523:-2])
    
    print(list(range(5,10)))

    def mycount():
        for counter in a:
            print(f"<{counter}>")
            yield counter
    print(list(mycount()))

    # sets
    myset = {1,2,3,4,4,"gello"}
    myset = set()
    print(myset)

    # dictionary
    mydict = {}
    mydict = dict()
    mydict = {"one": 1,
              "two": 2,
              3: "three"}
    print(mydict)

    print(mydict["one"])
    print(mydict.get("one"))
    print(mydict.get("three", 3.0))
    print(mydict.get(3))

    print(set([1,2,3]).intersection([3,4,5]))

    bigset = set()
    #1 in bigset

    import collections
    from collections import Counter

    # Counter
    c = Counter()
    c = Counter('aassdsadsdaasdas')
    print(c)
    c = Counter(apples=4, oranges=5)
    print(c)

def listcomprehensions():

    print('-'*40)
    # mylist = [ expression for item in iterableif filter]

    a = [4,6,7,3,2]
    b = [x for x in a]
    print(b)
    b = [x for x in a if x > 5]
    print(b)
    b = [x**2 for x in a if x > 5]
    print(b)

    a = ["Christan", "Caliah", "Vanisia", "Calln", "Cevan"]
    b = [x for x in a if x[0]=='C']
    b = [x for x in a if x.startswith("C")]
    print(b)

    a = [1,2,3,4,5]
    b = [10,20,30,40]

    values = []
    for ai in a:
        for bi in b:
            values.append(f'{ai*bi}')
    print(values)

    c = [f'{ai*bi}' for ai in a for bi in b]
    c = {f'{ai*bi}' for ai in a for bi in b} # Set comp
    c = { f'{ai}*{bi}':f'{ai*bi}' for ai in a for bi in b} # dict comp
    print(c)


if __name__ == '__main__':
    # something
    print("Hello")
    # main("Leanna", [100,98,99])
    gg = lambda x: x*2 
    #main("Leanna", gradegen)

    #datastructure()
    listcomprehensions()
