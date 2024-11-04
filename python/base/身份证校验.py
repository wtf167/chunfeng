# -*- coding: utf8 -*-

import pandas as pd

def read_excel(excel_path, col):
    data = pd.read_excel(excel_path, sheet_name="Sheet1", usecols=[col])
    data = data.values.tolist()
    data = [x[0] for x in data]
    return data

"""
身份证校验函数
前17位分别乘[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
17个乘机相加模11
得到的数(0-10)分别对应['1','0','X','9','8','7','6','5','4','3','2']即校验码
"""
def check(data):
    cal = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    valid = ['1','0','X','9','8','7','6','5','4','3','2']
    n = 0
    for sfz in data:
        n += 1
        # 15位身份证号不校验
        if len(sfz) != 18:
            print(n, sfz)
            continue

        sum = 0
        for i in range(17):
            sum += int(sfz[i]) * cal[i]
        index = sum % 11
        if valid[index] != str(sfz[17]).upper():
            print(n, sfz)

if __name__ == '__main__':
    excel_path = ""
    data = read_excel(excel_path, 2)
    check(data)
