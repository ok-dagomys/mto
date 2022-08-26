import json

import pandas as pd
from docxtpl import DocxTemplate

df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                  index=['row 1', 'row 2'],
                  columns=['col 1', 'col 2'])

doc = DocxTemplate("template.docx")
context = {'table': json.loads(df.to_json(orient='records'))}
doc.render(context)
print('Docx generated')
doc.save("template_final.docx")
