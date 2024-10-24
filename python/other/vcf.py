a = ["name1_123_456_789"]
b = [x.split("_") for x in a]
vcf_str = ""
for i in b:
    tel = ""
    for j in i[1:]:
        tel += f'TEL;CELL:{j}\n'
    name = i[0]
    note = i[-1]
    vcf_str += f'''BEGIN:VCARD
N:{name}
{tel}NOTE:{note}
END:VCARD'''
print(vcf_str)