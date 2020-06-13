# -*- coding:utf8 -*-

def fab(n):
    return 1 if n<1 else n*fab(n-1)

if __name__ == '__main__':
    n = int(input("Enter a num:"))
    print(fab(n))

