import pandas as pd
import requests

# Not working, saying no table found

#df_list = pd.read_html('wrfk.html')

html = requests.get('https://www.wrkf.org/wrkf-schedule').content
df_list = pd.read_html(html)

for i, df in enumerate(df_list):
    print(df)
