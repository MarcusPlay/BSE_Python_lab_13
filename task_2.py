#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать функцию, вычисляющую среднее гармоническое своих аргументов.
# Если функции передается пустой список аргументов, то она должна возвращать значение None.


def garmonic_mean(*args):
    if len(args) == 0:
        return None
    
    ans = 0
    for i in args:
        ans += 1/i
    
    return (len(args)/ans)


if __name__=="__main__":
    a = list(map(int, input("Введите значения через пробел:\n").split()))
    print(garmonic_mean(*a))

