# import json
#
# import pandas as pd
# from docxtpl import DocxTemplate
#
# df = pd.DataFrame([['a', 'b'], ['c', 'd']],
#                   index=['row 1', 'row 2'],
#                   columns=['col 1', 'col 2'])
#
# doc = DocxTemplate("template.docx")
# context = {'table': json.loads(df.to_json(orient='records'))}
# doc.render(context)
# print('Docx generated')
# doc.save("template_final.docx")

# import os, sys  # Standard Python Libraries
# import xlwings as xw  # pip install xlwings
# from docxtpl import DocxTemplate  # pip install docxtpl
#
# # -- Documentation:
# # python-docx-template: https://docxtpl.readthedocs.io/en/latest/
#
# # Change path to current working directory
# os.chdir(sys.path[0])
#
#
# def main():
#     wb = xw.Book.caller()
#     sht_panel = wb.sheets["Sheet1"]
#     # -- Get values from Excel
#
#     doc = DocxTemplate("template.docx")
#     context = sht_panel.range("B2").options(dict, expand="table", numbers=int).value
#     doc.render(context)
#     print('Docx generated')
#     doc.save("template_final.docx")
#
#
# if __name__ == "__main__":
#     xw.Book("warehouse.xlsx").set_mock_caller()
#     main()

from docxtpl import DocxTemplate

tpl = DocxTemplate('dynamic_table_tpl.docx')

context = {
    'col_labels': ['fruit', 'vegetable', 'stone', 'thing'],
    'tbl_contents': [
        {'label': 'yellow', 'cols': ['banana', 'capsicum', 'pyrite', 'taxi']},
        {'label': 'red', 'cols': ['apple', 'tomato', 'cinnabar', 'doubledecker']},
        {'label': 'green', 'cols': ['guava', 'cucumber', 'aventurine', 'card']},
    ]
}

tpl.render(context)
tpl.save('dynamic_table.docx')
