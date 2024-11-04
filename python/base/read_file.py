# -*- coding: utf8 -*-

import pandas as pd

"""
读取excel内容返回list
"""
def read_excel(excel_path, col):
    data = pd.read_excel(excel_path, sheet_name="Sheet1", usecols=[col])
    data = data.values.tolist()
    data = [x[0] for x in data]
    return data


if __name__ == '__main__':
    data = read_excel("/tmp/test.xlsx", 2)
    print(data)