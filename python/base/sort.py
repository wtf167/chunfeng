#!/usr/bin/python3
# -*- coding:UTF-8 -*-


# 冒泡排序
def bubbleSort(param):
    for i in range(len(param) - 1):
        for j in range(len(param) - 1 - i):
            if param[j] > param[j + 1]:
                param[j], param[j + 1] = param[j + 1], param[j]
    return param


# 选择排序
def selectSort(param):
    for i in range(len(param)):
        min = i
        for j in range(i + 1, len(param)):
            if (param[min] > param[j]):
                min = j
        param[i], param[min] = param[min], param[i]
    return param


# 插入排序
def insertionSort(p):
    for i in range(1, len(p)):
        j = i - 1
        key = p[i]
        while j >= 0 and key < p[j]:
            p[j + 1] = p[j]
            j -= 1
        p[j + 1] = key
    return p


def main():
    test = [5, 167, 60, 40, 50, 20, 10, 30, 2]
    print(bubbleSort(test))
    print(selectSort(test))
    print(insertionSort(test))


if __name__ == '__main__':
    main()
