#!/usr/bin/env python3


import xlwt, re


wb = xlwt.Workbook()
#Style for CRQ
font0 = xlwt.Font()
font0.colour_index = 2
font0.bold = True
style0 = xlwt.XFStyle()
style0.font = font0
#Style for Notes
font1 = xlwt.Font()
font1.bold = True
style1 = xlwt.XFStyle()
style1.font = font1
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = xlwt.Style.colour_map['light_orange']
style1.pattern = pattern



ws = wb.add_sheet("Test_Sheet")


list_of_lines = []
f = open("file.txt", 'r')
for line in f.readlines():
    pattern_empty = re.match("^$", line)
    if line != "" and not pattern_empty:
        list_of_lines.append(line.replace('\n',''))
f.close()
print(list_of_lines)

for i in range(0,len(list_of_lines)):
    pattern_colour = re.match ("^CRQ.*|^RLM/CRQ.*", list_of_lines[i])
    pattern_background = re.match(".*sheet notes:", list_of_lines[i])
    if list_of_lines[i] != '':
        if pattern_colour:
            ws.col(0).width = (len(list_of_lines[i])*367)
            ws.write(i,0,list_of_lines[i],style0)
        elif pattern_background:
            ws.write(i,0,list_of_lines[i],style1)
        else:
            ws.write(i,0,list_of_lines[i])


wb.save("alex.xls")
