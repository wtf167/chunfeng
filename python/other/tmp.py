# coding:utf-8
import os
import re
import xlrd

dir1 = "/tmp/b"
fns = ['ZD.xls']
for fn in fns:
    pre_name = fn.replace(".xls", "")
    vcf_str = ""
    xls_path = os.path.join(dir1, fn)
    wb = xlrd.open_workbook(filename=xls_path)
    sts = wb.sheet_names()
    st = wb.sheet_by_index(0)
    nrows = st.nrows
    for i in range(0, nrows):
        name = st.cell_value(i, 1).replace("\n", ",")
        name = pre_name + "-" + name
        note_index = 2
        note = str(st.cell_value(i, note_index))
        tel_index = 3
        if st.cell_type(i, tel_index) == 2:
            tels = str(int(st.cell_value(i, tel_index)))
        else:
            tels = st.cell_value(i, tel_index)
        if not tels:
            continue
        tel = ""
        for j in re.split("\s", tels):
            if j:
                tel += f'TEL;CELL:{j}\n'
        print(tel)
        vcf_str += f'''BEGIN:VCARD
N;CHARSET=UTF-8:{name}
{tel}NOTE;CHARSET=UTF-8:{note}
END:VCARD\n'''

    f1 = open(file="/tmp/"+pre_name+".vcf", mode="w", encoding="utf-8")
    f1.write(vcf_str)
    f1.close()