import pandas as pd

import cfg

data = pd.read_excel(cfg.src, header=None, index_col=None)
rem_words = ['Ед.\nизм.', 'Наименвание', 'Кол-во']
for word in rem_words:
    data = data.mask(data == word)

data = data[[1, 2, 3]].dropna(axis=0, how='all').reset_index(drop=False)
data.columns = ['Номер', 'Наименование товара', 'Един. изм.', 'Количество']
data['Номер'] = data.index


df = pd.DataFrame(data)
