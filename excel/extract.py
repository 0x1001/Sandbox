def example1():
    import xlrd

    excel_file = xlrd.open_workbook("PLKGHM000017.xls")
    first_sheet = excel_file.sheets()[0]

    for cell in first_sheet.col(9):
        print cell.value

def exmaple2():
    import xlrd

    excel_file = xlrd.open_workbook("PLKGHM000017.xls")
    first_sheet = excel_file.sheets()[0]

    for row_idx in range(first_sheet.nrows):
        to_print = ""
        for cell in first_sheet.row(row_idx):
            to_print += str(cell.value) + "    "

        print to_print

if __name__ == "__main__":
    example1()
    exmaple2()