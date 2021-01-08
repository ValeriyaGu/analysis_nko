import pandas as pd

nkoOriginalBD = pd.read_csv('НКО с сайтами.csv', sep=';')

print(nkoOriginalBD.columns)
