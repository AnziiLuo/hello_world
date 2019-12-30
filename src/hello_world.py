#!/usr/bin/env python
"""
    Created by Anzii.Luo at .
    Description: 
"""

def test(fun):
    def hello_python():
        fun()
        print("--> Hello Python")
    return hello_python


@test
def hello_world():
    print("Hello World!")



if __name__ == "__main__":
    hello_world()
