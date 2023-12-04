#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать функцию, вычисляющую среднее геометрическое своих аргументов.
# Если функции передается пустой список аргументов, то она должна возвращать значение None.

def geometric_mean(*args):
    if len(args) == 0:
        return None
    
    ans = 1
    for i in args:
        ans *= i
    return (ans)**(1/(len(args)))


if __name__=="__main__":
    a = list(map(int, input("Введите значения через пробел:\n").split()))
    print(geometric_mean(*a))
