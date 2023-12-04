#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Реализуйте функцию calculate, которая принимает различные арифметические операции
# и переменное число операндов в виде именованных аргументов. Поддерживаемые операции могут включать 
# сложение, вычитание, умножение и деление.


def calculate(**kwargs):
    result = None

    if 'operation' in kwargs and 'operands' in kwargs:
        operation = kwargs['operation']
        operands = kwargs['operands']

    match operation:
        case 'add':
            result = sum(operands)
        case 'subtract':
            result = operands[0] - sum(operands[1:])
        case 'multiply':
            result = 1
            for operand in operands:
                result *= operand
        case 'divide':
            if all(operands[1:]):
                result = operands[0] / operands[1]

    return result

if __name__ == "__main__":
    operation = input("Введите какую операцию хотите сделать:\nadd, subtract, multiply, divide\n$ ")
    operands = list(map(int, input("Введите значения через пробел:\n").split()))
    result = calculate(operation=operation, operands=operands)
    print("Результат:", result)
