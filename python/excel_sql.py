# -*- coding:utf-8 -*-

import os
import xlrd

# 取当前路径
cd = os.path.dirname(__file__)
# 在当前目录读取excel
# excel_name = os.path.join(cd, "2022-10-09附件3 共享报表模块初始化统计表-昆仑能源投资（山东）有限公司本部（徐媛媛）.xls")
# print(excel_name)
excel_path = os.path.join(cd, "in")
out_path = os.path.join(cd, "out")
excel_list = [os.path.join(excel_path, f) for f in os.listdir(excel_path)]

for excel_name in excel_list:
    # excel_name = "/tmp/2022-10-09附件3 共享报表模块初始化统计表-昆仑能源投资（山东）有限公司本部（徐媛媛）.xls"
    # 打开excel
    workbook = xlrd.open_workbook(excel_name)
    sheets = workbook.sheet_names()

    # 按索引读取第一个sheet页
    sheet1 = workbook.sheet_by_index(0)
    # 获取单位编号
    dwbh = sheet1.cell_value(3, 1)

    # 按索引读取第三个sheet
    sheet3 = workbook.sheet_by_index(2)
    # 取总行数
    rows = sheet3.nrows
    data = []
    # 开始行
    start_row = 4
    for i in range(start_row, rows):
        # cell_type为2时为float类型需要强转一下
        if sheet3.cell_type(i, 6) == 2:
            bz = str(int(sheet3.cell_value(i, 6)))
        else:
            bz = sheet3.cell_value(i, 6)
        # 数字类型的报表编号强转之后在前面加上1000
        if sheet3.cell_type(i, 1) == 2:
            bbbh = "1000" + str(int(sheet3.cell_value(i, 1)))
        else:
            bbbh = sheet3.cell_value(i, 1)
        if sheet3.cell_type(i, 8) == 2:
            issggy = str(int(sheet3.cell_value(i, 8)))
        else:
            issggy = sheet3.cell_value(i, 8)
        # 标志为1时，加入数组
        if bz == "1":
            data.append((dwbh, bbbh, issggy))

    # sql语句
    pre_sql = "insert into KLGX_RPT_DWXYBB(F_RPT_DWBH,F_RPT_BBBH,F_ISYXJS) values ('{}','{}','{}');"
    # 打开写入文件
    out_path = os.path.join(cd, "out")
    out_name = dwbh + ".txt"
    out_file = os.path.join(out_path, out_name)
    f = open(out_file, "w")
    for j in data:
        f.write(pre_sql.format(j[0], j[1], j[2]))
        f.write("\n")
    # 关闭文件
    f.close()
