#!usr/bin/env python
# -*- coding: utf-8 -*-


def spreadsheets_conversion(cell_name):
    """
    The first column has number A, the second — number B, etc.
    till column 26 that is marked by Z. Then there are two-letter
    numbers: column 27 has number AA, 28 — AB, column 52 is marked by AZ.
    After ZZ there follow three-letter numbers, etc.

    The rows are marked by integer numbers starting with 1.
    The cell name is the concatenation of the column and the row numbers.
    Sometimes another numeration system is used: RXCY,
    where X and Y are integer numbers, showing the column and
    the row numbers respectfully.
    edge cases: R795...
    """
    if cell_name.startswith('R') and cell_name[1].isdigit():
        if 'C' not in cell_name:
            row = [i for i in cell_name if i.isdigit()]
            col = [i for i in cell_name if i.isalpha()]

            return 'R' + ''.join(row) + "C" + str(col_to_int(''.join(col)))
        row, col = cell_name.split('C')
        row = row[1:]
        return int_to_col(int(col)) + row

    for index, val in enumerate(cell_name):
        if val.isdigit():
            row = cell_name[index:]
            col = cell_name[:index]
            col = "C" + str(col_to_int(col))
            return "R" + row + col

    col = ''
    for index, val in enumerate(cell_name):
        if val.isalpha():
            col += val
    return col_to_int(col)


def int_to_col(num, base=26):
    """
    Take an integer and return its corresponding column name
    实际上等于将10进制转换成26进制
    """
    alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    col = ''
    while num:
        mod = (num - 1) % 26
        num = int((num - mod) / 26)
        col += alphas[mod]
    return col[::-1]


def col_to_int(col_name):
    """return a base10 integer
    """
    alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    res = [alphas.index(i) + 1 for i in col_name]
    return sum(val * (26 ** index) for index, val in enumerate(res[::-1]))


# print(spreadsheets_conversion("R853"))
# print(spreadsheets_conversion("RZ228"))
# print(spreadsheets_conversion("ZL98"))
# print(col_to_int("RZ"))
# print(int_to_col(494))

params = []
temp = input()
for i in range(int(temp)):
    temp = input()
    params.append(temp)

for i in params:
    print(spreadsheets_conversion(i))
